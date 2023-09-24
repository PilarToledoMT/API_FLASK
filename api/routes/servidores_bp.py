from flask import Blueprint
from ..controllers.servidor_controller import ServidorController

servidores_bp = Blueprint('servidores_bp', __name__)

servidores_bp.route('/servidores/<int:id_servidor>', methods = ['GET'])(ServidorController.get_server_controller)
servidores_bp.route('/servidores', methods = ['GET'])(ServidorController.get_all_servers_controller)