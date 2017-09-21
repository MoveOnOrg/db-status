This Python 3.6 script tries to connect to databases and sends a Slack alert with error text if it fails. Note: Python3.6 is compatible with AWS Lambda deployment. If you're not deploying to AWS Lambda, any other verson of Python3 will do.

## Setup

* Create a Python 3.6 virtualenv: `virtualenv -p /path/to/python3.6 venv`
* Activate the virtualenv: `source venv/bin/activate`
* Create a settings file and fill it out: `cp settings.py.example settings.py`.
* If you want to deploy the script to lambda, set `lambda_deploy = True` and `pip install -r requirements-lambda.txt`
* Else, leave `lambda_deploy = False` and `pip install -r requirements-nolambda.txt`
* Run script with `python check_dbs.py`

## Deploy to AWS Lambda with zappa

* in settings.py, set `lambda_deploy = True`
* copy zappa_settings.json.example to zappa_settings.json and fill it out
* set up your AWS creds that allow you to create s3 buckets, and add your target s3 bucket to zappa_settings.json
* `zappa deploy production` or whatever the name of your stage is

## TODO:

* Add support for email and SMS alerts.