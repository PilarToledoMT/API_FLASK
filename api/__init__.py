from flask import Flask
from flask_cors import CORS
from config import Config
from .database import DatabaseConnection
from .routes.usuarios_bp import usuarios_bp
from .routes.imagen_perfil_bp import imagen_perfil_bp
from .routes.servidores_bp import servidores_bp
from .routes.mensajes_bp import mensajes_bp

def init_app():
    app = Flask (__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    app.config.from_object(Config)
    DatabaseConnection.set_config(app.config)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(imagen_perfil_bp)
    app.register_blueprint(servidores_bp)
    app.register_blueprint(mensajes_bp)

    CORS(app)
    
    return app