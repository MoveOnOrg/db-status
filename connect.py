import sys
import settings
import pymysql.cursors
import requests
import json
if settings.lambda_deploy:
    import pg8000
else:
    import psycopg2

def connect_psql(psql):
    if settings.lambda_deploy:
        try:
            con = pg8000.connect(database = psql['db'],
                                    host = psql['host'], 
                                    port = psql['port'], 
                                    user = psql['user'], 
                                    password = psql['pwd'])
            con.close()
        
        except:
            message = "db-status {} connection error: {}".format(psql['name'],sys.exc_info())
            if settings.slack_alerts:
                post_to_slack(message)
    else:
        try:
            con = psycopg2.connect(dbname = psql['db'],
                                    host = psql['host'], 
                                    port = psql['port'], 
                                    user = psql['user'], 
                                    password = psql['pwd'])
            con.close()
        except:
            message = "db-status {} connection error: {}".format(psql['name'],sys.exc_info())
            if settings.slack_alerts:
                post_to_slack(message)


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
        message = "db-status {} connection error: {}".format(mysql['name'],sys.exc_info())
        if settings.slack_alerts:
            post_to_slack(message)


def post_to_slack(message, slack_webhook_url=settings.slack_webhook_url):
    text = json.dumps({ 'text' : message })
    print(text)
    r = requests.post(slack_webhook_url, data = text)