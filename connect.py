import psycopg2
import sys
import settings
import pymysql.cursors
import requests
import json


def connect_psql(psql):
    try:
        con = psycopg2.connect(dbname = psql['db'],
                                host = psql['host'], 
                                port = psql['port'], 
                                user = psql['user'], 
                                password = psql['pwd'])
        con.close()
    except:
        message = "{} connection error: {}".format(psql['name'],sys.exc_info())
        if settings.slack_alerts:
            post_to_slack_channel(message)


def connect_mysql(mysql):
    try:
        con = pymysql.connect(host=mysql['host'],
                              user=mysql['user'],
                              password=mysql['pwd'],
                              db=mysql['db'],
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
        con.close()
    except:
        message = "{} connection error: {}".format(mysql['name'],sys.exc_info())
        if settings.slack_alerts:
            post_to_slack_channel(message)


def post_to_slack_channel(message, slack_webhook_url=settings.slack_webhook_url):
    text = json.dumps({ 'text' : message })
    print(text)
    r = requests.post(slack_webhook_url, data = text)