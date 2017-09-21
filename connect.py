import sys
import settings
import pymysql.cursors
import requests
import json
if settings.lambda_deploy:
    import pg8000
else:
    import psycopg2

def slack_alert(name, slack_webhook_url = settings.slack_webhook_url):
    message = "db-status {} connection error: {}".format(name,sys.exc_info())
    text = json.dumps({ 'text' : message })
    print(text)
    if settings.slack_alerts:
        r = requests.post(slack_webhook_url, data = text)

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
            slack_alert(psql['name'])
            
    else:
        try:
            con = psycopg2.connect(dbname = psql['db'],
                                    host = psql['host'], 
                                    port = psql['port'], 
                                    user = psql['user'], 
                                    password = psql['pwd'])
            con.close()
        except:
            slack_alert(psql['name'])

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
        slack_alert(mysql['name'])