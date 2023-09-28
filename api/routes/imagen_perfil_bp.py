from flask import Blueprint
from ..controllers.imagen_perfil_controller import ImagenPerfilController

imagen_perfil_bp=Blueprint("imagen_perfil_bp", __name__)

imagen_perfil_bp.route("/imagenes/<int:id_imagen>", methods=["GET"])(ImagenPerfilController.get_imagen)

imagen_perfil_bp.route("/imagenes", methods=["GET"])(ImagenPerfilController.get_imagenes)

imagen_perfil_bp.route("/imagenes", methods=["POST"])(ImagenPerfilController.create_imagen)

imagen_perfil_bp.route("/imagenes/<int:id_imagen>", methods=["PUT"])(ImagenPerfilController.update_imagen)

imagen_perfil_bp.route("/imagenes/<int:id_imagen>", methods=["DELETE"])(ImagenPerfilController.delete_imagen)