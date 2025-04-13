# Libraries
from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

# Modules
from database.db_mariadb import db_connect
from config import config
from routes import init_routes
from models.users import User  # User con UserMixin

# Login Manager
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])

    # Inicializar login manager
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Ruta a la que redirige si no estás logueado

    # Cargar usuario por ID desde la base de datos
    @login_manager.user_loader
    def load_user(user_id):
        db = db_connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        return User.get(user_data) if user_data else None

    # Inicializar rutas
    init_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
