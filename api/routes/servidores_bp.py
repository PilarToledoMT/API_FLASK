from flask import Blueprint
from ..controllers.servidor_controller import ServidorController

servidores_bp = Blueprint('servidores_bp', __name__)

servidores_bp.route('/servidores/<int:id_servidor>', methods = ['GET'])(ServidorController.get_server_controller)
servidores_bp.route('/servidores', methods = ['GET'])(ServidorController.get_all_servers_controller)
servidores_bp.route('/servidores', methods = ['POST'])(ServidorController.create_server_controller)
servidores_bp.route('/servidores/<int:id_servidor>', methods = ['PUT'])(ServidorController.update_server_controller)
servidores_bp.route('/servidores/<int:id_servidor>', methods = ['DELETE'])(ServidorController.delete_server_controller)
servidores_bp.route('/servidor/<int:id_usuario>', methods = ['GET'])(ServidorController.mostrar_servidores_usuario)