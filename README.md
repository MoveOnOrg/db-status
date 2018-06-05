This Python 3.6 script tries to connect to databases and sends a Slack alert with error text if it fails.

## Setup

* Create a Python 3.6 virtualenv: `virtualenv -p /path/to/python3 venv`
* Activate the virtualenv: `source venv/bin/activate`
* Install requirements: `pip install -r requirements.txt`
* Create a settings file and fill it out: `cp settings.py.example settings.py`
* Run script with `python check_dbs.py`

## Deploy

* `pip install pip==9.0.3`, since zappa requires an older version of pip
* `cp zappa_settings.json.example zappa_settings.py`, fill in `s3_bucket` with a unique bucket name, and change anything else you want.
* `zappa deploy production`

## TODO:

* Add support for email and SMS alerts.
