#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import print_function

import csv
import io
import os.path
import pickle
import tempfile
import traceback

import mysql.connector
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from mysql.connector import errorcode

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

DB_HOST = ''
DB_USERNAME = ''
DB_PASSWORD = ''
DB_NAME = ''

DATATABLES = ['GA_LANDING_PAGE']


def init_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)


def get_all_sheets(service):
    sheets = service.files().list(
        pageSize=1000,
        fields="nextPageToken, files(id, name)",
        q="mimeType='application/vnd.google-apps.spreadsheet'").execute()
    return sheets.get('files', [])


def download_csv(service, sheet_id):
    request = service.files().export_media(fileId=sheet_id,
                                           mimeType='text/csv')
    with io.BytesIO() as fh:
        downloader = MediaIoBaseDownload(fh, request, chunksize=1024 * 1024)

        done = False
        while done is False:
            status, done = downloader.next_chunk()
            if status:
                print("Download %d%%." % int(status.progress() * 100))
        print("Download sheet id {} complete!".format(sheet_id))

        return fh.getvalue().decode().splitlines()


def main(config):
    service = init_service()
    sheets = [
        x['id'] for x in get_all_sheets(service) if x['name'] in DATATABLES
    ]
    cnx = mysql.connector.connect(**config)
    cur = cnx.cursor()
    stmt_insert_url_impressions = "INSERT INTO GA_LANDING_PAGE (GA_HOSTNAME, LANDING_PAGE, DATE, USERS, SESSIONS, AVG_SESSION_DURATION, TOTAL_EVENTS) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    for sheet in sheets:
        try:
            content = download_csv(service, sheet)
            reader = csv.reader(content, delimiter=",")
            header = next(reader, None)
            if header is None:
                continue

            rows = tuple(tuple([x for x in row]) for row in reader)
            if len(header) == 7:
                cur.executemany(stmt_insert_url_impressions, rows)
                cnx.commit()
        except:
            # Just for debug
            traceback.print_exc()

    cur.close()
    cnx.close()


if __name__ == '__main__':
    config = {
        'host': DB_HOST,
        'user': DB_USERNAME,
        'port': 3306,
        'password': DB_PASSWORD,
        'database': DB_NAME,
        'charset': 'utf8',
        'use_unicode': True,
        'get_warnings': True,
    }

    main(config)

