import psycopg2 # redshift
import sys
import settings
import pymysql.cursors


def connect_redshift(redshift = settings.redshift):
    try:
        con = psycopg2.connect(dbname = redshift['db'],
                                host = redshift['host'], 
                                port = redshift['port'], 
                                user = redshift['user'], 
                                password = redshift['pwd'])
        print (con)
        con.close()
    except:
        print ("{} connection error: {}".format(redshift['name'],sys.exc_info()))


def connect_mysql(mysql):
    try:
        con = pymysql.connect(host=mysql['host'],
                              user=mysql['user'],
                              password=mysql['pwd'],
                              db=mysql['db'],
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
        print(con)
        con.close()
    except:
        print ("{} connection error: {}".format(mysql['name'],sys.exc_info()))

# connect_redshift()
connect_mysql(settings.ak_read_replica_shared)
connect_mysql(settings.signon_read_replica)


# List of dbs to connect to:

# ak read replica 1
# ak read replica 2
# petitions read replica

