This Python 3.6 script tries to connect to databases and sends a Slack alert with error text if it fails.

## Setup

* Create a Python 3.6 virtualenv: `virtualenv -p /path/to/python3.6 venv`
* Activate the virtualenv: `source venv/bin/activate`
* Install requirements: `pip install -r requirements.txt`
* Create a settings file and fill it out: `cp settings.py.example settings.py`
* Run script with `python check_dbs.py`

## TODO:

* Add support for email and SMS alerts.