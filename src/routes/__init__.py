from .homeRoute import home_bp

def init_routes(app):
    app.register_blueprint(home_bp)