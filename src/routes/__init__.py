from .homeRoute import home_bp
from .authRoutes import auth_bp
from .adminRoutes import admin_bp

def init_routes(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')