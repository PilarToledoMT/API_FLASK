from flask import Blueprint
from ..controllers.canal_controller import CanalController

canal_bp = Blueprint('canal_bp', __name__)

canal_bp.route('/', methods = ['GET'])(CanalController.home)
canal_bp.route('/canal', methods = ['GET'])(CanalController.get_canales)
canal_bp.route('/canal/<int:id_servidor>', methods = ['GET'])(CanalController.get_canales_por_servidor)
canal_bp.route('/canal', methods = ['POST'])(CanalController.create_canal)