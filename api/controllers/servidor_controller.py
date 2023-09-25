from ..models.servidor_model import ServidorModel
from flask import request,jsonify

class ServidorController:

    @classmethod
    def get_server_controller(cls,id_servidor):
        server_instance = ServidorModel.get_server_model(id_servidor)
        if server_instance:
            response_data = {
                'id_servidor': server_instance.id_servidor,
                'nombre_servidor': server_instance.nombre_servidor,
                'imagen_servidor': server_instance.imagen_servidor
            }
            return jsonify(response_data), 200
        else:
            return {'msg': 'No se encontró el producto'}, 404