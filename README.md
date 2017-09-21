This Python 3.x script tries to connect to databases and sends a Slack alert with error text if it fails.

## Setup

* Create a Python 3.x virtualenv: `virtualenv -p /path/to/python3 venv`
* Activate the virtualenv: `source venv/bin/activate`
* Install requirements: `pip install -r requirements.txt`
* Create a settings file and fill it out: `cp settings.py.example settings.py`
* Run script with `python check_dbs.py`

## Deploy to AWS Lambda with zappa

* Check out the zappa branch
* `pip install zappa==0.44.3`
* set up your AWS creds that allow you to create s3 buckets
* `zappa init` and answer the questions to create your zappa_settings.json file. Modular path to function is `check_dbs.main`
* `zappa deploy production` or whatever the name of your stage is

## TODO:

* Add support for email and SMS alerts.