[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/OHZj2eyN)
# Project-6-Brevets-REST

Reimplement the RUSA ACP control time calculator with flask,
ajax, MongoDB and REST.

## Objectives:

* Create well-defined APIs that serves different
  resources in different representations.
* Design multiple web-services where one can consume information
  from the other.

## Dependencies:

* Designed for Unix, mostly interoperable on Linux or macOS.
  May also work on Windows, but no promises. A Linux
  virtual machine may work. You may want to test on shared
  server (if available).
* You must install [docker](https://www.docker.com/products/docker-desktop/).

## Instructions:

* You have a minimal implementation of Docker compose in
  DockerRestAPI folder, using which you can create REST
  API-based services (as demonstrated in class).
* You will reuse *your* code from project 5. Recall:
  you created the following functionalities.
  1. Two buttons <kbd>Submit</kbd> and <kbd>Display</kbd>
    in the page where you have control times.
  2. On clicking the <kbd>Submit</kbd> button, the control
    times were be entered into the database.
  3. On clicking the <kbd>Display</kbd> button, the entries
    from the database were be displayed in a new page.
  4. You also handled error cases appropriately.
* This project has four main parts for you to implement. 
  Change the values for `<host>` and `<port>` according to
  your machine, and use the web browser to check the results.

  * **[PART-1]** You will design RESTful service to expose what is
    stored in MongoDB. Specifically, you'll use the example
    given in DockerRestAPI folder, and create the following three
    basic APIs:
      * `http://<host:port>/listAll` should return all open and
        close times in the database.
      * `http://<host:port>/listOpenOnly` should return open
        times only.
      * `http://<host:port>/listCloseOnly` should return close
        times only.

  * **[PART-2]** You will design two different representations: one
    in csv and one in json. For the above three basic APIs, JSON
    should be your default representation. 
      * `http://<host:port>/listAll/csv` should return all open
         and close times in CSV format.
      * `http://<host:port>/listOpenOnly/csv` should return open
         times only in CSV format.
      * `http://<host:port>/listCloseOnly/csv` should return close
         times only in CSV format.

      * `http://<host:port>/listAll/json` should return all open
         and close times in JSON format.
      * `http://<host:port>/listOpenOnly/json` should return open
         times only in JSON format.
      * `http://<host:port>/listCloseOnly/json` should return close
         times only in JSON format.

  * **[PART-3]** You will add a query parameter to get top "k"
    open and close times. For examples,
      * `http://<host:port>/listOpenOnly/csv?top=3` should return top 3
         open times only (in ascending order) in CSV format.
      * `http://<host:port>/listOpenOnly/json?top=5` should return top 5
         open times only (in ascending order) in JSON format.
      * `http://<host:port>/listCloseOnly/csv?top=6` should return top 6
         close times only (in ascending order) in CSV format
      * `http://<host:port>/listCloseOnly/json?top=4` should return top 4
         close times only (in ascending order) in JSON format

  * **[PART-4]** You'll also design consumer programs (e.g., in
    jQuery) to use the service that you expose. "website" inside
    DockerRestAPI is an example of that. It uses PHP. You're
    welcome to use either PHP or jQuery to consume your services.
    NOTE: your consumer program should be in a different container
    like example in DockerRestAPI.

* We provided the same files found in project-4 here under the
  [brevets'](brevets) directory. Please note that the directory does
  not have a `credentials.ini` file. You have to provide it yourself for
  the application to work as it used to be. Also, you have to copy all
  the files you worked on from projects 4 & 5 (`acp_times.py`,
  `flask_brevets.py`, `brevets.html`, and `docker-compose.yml`) to
  this project before you start.

## Data Samples

The sample data files ([sample-data.json](data-samples/sample-data.json),
[sample-data.csv](data-samples/sample-data.csv), and [sample-data-pivoted.csv](data-samples/sample-data-pivoted.csv))
provide JSON and CSV format that you could follow for your exports.

### JSON
```json
{
   "brevets":[
      {
         "distance":200,
         "begin_date":"01/01/2024",
         "begin_time":"00:00",
         "controls":[
            {
               "km":0,
               "mi":0,
               "location":"Starting Point",
               "open":"01/01/2024 00:00",
               "close":"01/01/2024 01:00"
            },
            {
               "km":100,
               "mi":62.1,
               "location":null,
               "open":"01/01/2024 02:56",
               "close":"01/01/2024 06:40"
            },
            {
               "km":150,
               "mi":93.2,
               "location":"Second Checkpoint",
               "open":"01/01/2024 04:25",
               "close":"01/01/2024 10:00"
            },
            {
               "km":200,
               "mi":124.3,
               "location":"Last Checkpoint",
               "open":"01/01/2024 05:53",
               "close":"01/01/2024 13:30"
            }
         ]
      },
      {
         "distance":1000,
         "begin_date":"01/01/2024",
         "begin_time":"00:00",
         "controls":[
            {
               "km":0,
               "mi":0,
               "location":"begin",
               "open":"01/01/2024 00:00",
               "close":"01/01/2024 01:00"
            },
            {
               "km":1000,
               "mi":621.4,
               "location":"finish line",
               "open":"01/01/2024 09:05",
               "close":"01/01/2024 03:00"
            }
         ]
      }
   ]
}
```

### CSV
```csv
brevets/distance,brevets/begin_date,brevets/begin_time,brevets/controls/0/km,brevets/controls/0/mi,brevets/controls/0/location,brevets/controls/0/open,brevets/controls/0/close,brevets/controls/1/km,brevets/controls/1/mi,brevets/controls/1/location,brevets/controls/1/open,brevets/controls/1/close,brevets/controls/2/km,brevets/controls/2/mi,brevets/controls/2/location,brevets/controls/2/open,brevets/controls/2/close,brevets/controls/3/km,brevets/controls/3/mi,brevets/controls/3/location,brevets/controls/3/open,brevets/controls/3/close
200,1/1/24,0:00,0,0,Starting Point,1/1/24 0:00,1/1/24 1:00,100,62.1,,1/1/24 2:56,1/1/24 6:40,150,93.2,Second Checkpoint,1/1/24 4:25,1/1/24 10:00,200,124.3,Last Checkpoint,1/1/24 5:53,1/1/24 13:30
1000,1/1/24,0:00,0,0,begin,1/1/24 0:00,1/1/24 1:00,1000,621.4,finish line,1/1/24 9:05,1/1/24 3:00,,,,,,,,,,
```

## Credentials file (credentials.ini)

The credentials file should have the following information.
```ini
# Configuration of brevets calculator.
[DEFAULT]
author=Your Name Here
repo=git@github.com:username/project-name.git
quid=411******

# the port you used within compose to map the host to the API
# container for example, if the port is "5001:5000", then the
# PORT key should be 5001
PORT=5000
DEBUG = False

# See https://flask.palletsprojects.com/en/3.0.x/quickstart/#sessions
# about how to generate a secret key
SECRET_KEY = Replace this with random string; os.urandom can make one

# the host name for your database service.
HOSTNAME= Replace this with the host name you use

# here provide the name of your mongo collection where you link 
# your APIs
COLLECTION= Replace this with the name of the mongo collection
```

## Grading Rubric

* **[20 Points]** A working `Dockerfile` and `docker-compose.yml` files.
* **[30 Points]** Basic APIs (found in PART-1) work as expected.
* **[30 Points]** Representations (found in PART-2) work as expected.
* **[20 Points]** Query parameter-based APIs (found in PART-3) work as expected.

## Bonus Points

* **[30 Points]** Consumer program (found in PART-4) works as expected.
