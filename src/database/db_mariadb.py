import mariadb
from config import config


def db_connect():
    try:
        db_config = config['development']()
        conn = mariadb.connect(
            host=db_config.MARIADB_HOST,
            user=db_config.MARIADB_USER,
            password=db_config.MARIADB_PASSWORD,
            database=db_config.MARIADB_DB,
            port=int(db_config.MARIADB_PORT),
        )
        print("Connected to MariaDB")
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        exit(1)