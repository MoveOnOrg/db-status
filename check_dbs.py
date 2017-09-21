from connect import connect_psql, connect_mysql
import settings

def main():
    for key, database in settings.databases.items():
        if database['type'] == 'mysql':
            connect_mysql(database)
        elif database['type'] == 'psql':
            connect_psql(database)

if __name__ == "__main__":
    main()