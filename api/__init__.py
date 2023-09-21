from flask import Flask
from config import Config
from .database import DatabaseConnection
from .routes.usuarios_bp import usuarios_bp

def init_app():
    app = Flask (__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    app.config.from_object(Config)
    DatabaseConnection.set_config(app.config)
    app.register_blueprint(usuarios_bp)

    
    return app