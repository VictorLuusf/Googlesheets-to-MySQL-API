

  <h3 align="center">From Googlesheets to MySQL</h3>

  <p align="center">
    An interest method of getting your data from Google Analytics and Google Search Console into MySQL
    <br />
    <a href="https://github.com/VictorLuusf/Googlesheets-to-MySQL-API"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/VictorLuusf/Googlesheets-to-MySQL-API">View Demo</a>
    ·
    <a href="https://github.com/VictorLuusf/Googlesheets-to-MySQL-API">Report Bug</a>
    ·
    <a href="https://github.com/VictorLuusf/Googlesheets-to-MySQL-API">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)






<!-- ABOUT THE PROJECT -->
## About The Project

A long time ago, I worked at a startup that asked me to figure out how to get data from 157 client Google Analytics and Google Search Console accounts. Each one was owned by a separate client and they each set theirs up differently. 

### Built With

* [csv](https://docs.python.org/3/library/csv.html)
* [io](https://docs.python.org/3/library/io.html?highlight=io#module-io)
* [os.path](https://docs.python.org/3/library/os.path.html?highlight=os%20path#module-os.path)
* [pickle](https://docs.python.org/3/library/pickle.html?highlight=pickle#module-pickle)
* [tempfile](https://docs.python.org/3/library/tempfile.html?highlight=tempfile#module-tempfile)
* [traceback](https://docs.python.org/3/library/traceback.html?highlight=traceback#module-traceback)
* [mysql.connector](https://www.w3schools.com/python/python_mysql_getstarted.asp)
* [google.auth.transport.requests](https://google-auth.readthedocs.io/en/latest/reference/google.auth.transport.requests.html)
* [google_auth_oauthlib.flow](https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html)
* [googleapiclient.discovery](https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-module.html)
* [googleapiclient.http](https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.http-module.html)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Make sure you have these packages installed below. You will need to run these in terminal if you are on Mac or commpand prompt if you are on Windows.

* pipenv install
```sh
pipenv install
```
* mysql-connector-python
```sh
pip install mysql-connector-python
```
* google-api-python-client
```sh
pip install google-api-python-client
```
* google-auth-httplib2
```sh
pip install google-auth-httplib2
```
* google-auth-oauthlib
```sh
pip install google-auth-oauthlib
```

### Installation

1. Enable on the Drive API
```sh
https://developers.google.com/drive/api/v3/quickstart/python 
```
2. Download the client configuration file and put it in the same folder as the python script

3. Make sure you have installed everything in the prerequisites section. You will need to use terminal if you're on Mac or Command Prompt if you are using Windows

4. Once you are certain you have installed everything, will need to update the database connection information in the GALANDPAGE.py (Lines 26 to 29)
```sh
DB_Host = ''
DB_USERNAME = ''
DB_PASSWORD = ''
DB_NAME = ''
```
5. You should also update the name of the Datatables you want to feed the data into. (Line 31)
```sh
DATATABLES = ['GA_LANDING_PAGE']
```
6. You should also update column names and values listed in line 88. For each column you add or remove, you will need to remove a %s from the values. (Line 88)
```sh
"INSERT INTO GA_LANDING_PAGE (GA_HOSTNAME, LANDING_PAGE, DATE, USERS, SESSIONS, AVG_SESSION_DURATION, TOTAL_EVENTS) VALUES (%s, %s, %s, %s, %s, %s, %s)"
```


<!-- USAGE EXAMPLES -->
## Usage

Using this Python script, I was able to pull Google Analytics and Google Search Console data from 157 clients accounts and into our MySQL database for reporting and analytical purposes. This represented about ten million plus rows of data on a daily basis.

The limitation on this script in it's current form is that I ran six different ones to feed the data tables in the MySQL database. I thought about creating another .py file to have it run each script in sequential order without having to type out all six in terminal.
