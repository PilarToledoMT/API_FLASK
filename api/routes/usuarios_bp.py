from flask import Blueprint
from ..controllers.usuario_controller import UsuarioController
usuarios_bp=Blueprint("usuario_bp",__name__)
usuarios_bp.route("/usuarios/<string:email>", methods=["GET"])(UsuarioController.get_usuario)
usuarios_bp.route("/usuarios",methods=["GET"])(UsuarioController.get_usuarios)
usuarios_bp.route("/usuarios",methods=["POST"])(UsuarioController.create_usuario)
usuarios_bp.route("/usuarios/<string:email>", methods=["PUT"])(UsuarioController.update_usuario)
usuarios_bp.route("/usuarios/<int:id_usuario>", methods=["DELETE"])(UsuarioController.delete_usuario)
usuarios_bp.route("/login", methods = ['POST'])(UsuarioController.login)