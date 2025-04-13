from decouple import config

class Config():
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True
    MARIADB_HOST = config('MARIADB_HOST')
    MARIADB_USER = config('MARIADB_USER')
    MARIADB_PASSWORD = config('MARIADB_PASSWORD')
    MARIADB_DB = config('MARIADB_DB')
    MARIADB_PORT = config('MARIADB_PORT')
    
config = {
    'development': DevelopmentConfig
}