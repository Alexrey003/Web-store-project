#Libraries
from flask import Flask

# Modules
from database.db_mariadb import db_connect
from config import config
from routes import init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])
    
    init_routes(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()