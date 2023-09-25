from flask import Blueprint
from ..controllers.mensajes_controller import MensajesController

mensajes_bp = Blueprint('mensajes_bp', __name__)

mensajes_bp.route('/mensajes/<int:id_canal>', methods = ['GET'])(MensajesController.get_mensajes)

mensajes_bp.route('/mensajes', methods = ['POST'])(MensajesController.create_mensaje)

mensajes_bp.route('/mensajes/<int:id_mensaje>', methods = ['DELETE'])(MensajesController.delete_mensaje)