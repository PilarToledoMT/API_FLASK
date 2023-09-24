from flask import Flask
from config import Config
from .database import DatabaseConnection
from .routes.servidores_bp import servidores_bp

def init_app():
    app = Flask (__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    app.config.from_object(Config)

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(servidores_bp)
    
    return app