from ..models.servidor_model import ServidorModel
from flask import request,jsonify,json

class ServidorController:

    @classmethod
    def get_server_controller(cls,id_servidor):
        server_instance = ServidorModel.get_server_model(id_servidor)
        if server_instance:
            response_data = {
                'id_servidor':server_instance[0],
                'nombre_servidor':server_instance[1],
                'imagen_servidor':server_instance[2]
                }
            return jsonify(response_data), 200
        else:
            return {'msg': 'No se encontró el servidor'}, 404
        
    @classmethod
    def get_all_servers_controller (cls):
        server_instance = ServidorModel.get_all_servers_model()
        if server_instance:
            lista_servidores = []
            for servidor in server_instance:
                response = {
                    'id_servidor':servidor[0],
                    'nombre_servidor':servidor[1],
                    'imagen_servidor':servidor[2]
                }
                lista_servidores.append(response)
            return jsonify(lista_servidores),200
        else:
            return {'mensaje':'no se encontro servidor'}
        
    @classmethod
    def create_server_controller (cls):
        data = request.json
        servidor_instance = ServidorModel(
            nombre_servidor=data.get('nombre_servidor'),
            imagen_servidor=data.get('imagen_servidor')
        )
        ServidorModel.create_server_model(servidor_instance)
        return {'message': 'Servidor creado con exito'}, 200

    @classmethod
    def update_server_controller(cls, id_servidor):
        data = request.json
        if ServidorModel.exists(id_servidor):
            servidor_instance = ServidorModel(
                id_servidor=id_servidor,
                nombre_servidor=data.get('nombre_servidor'),
                imagen_servidor=data.get('imagen_servidor')
            )
            ServidorModel.update_server_model(servidor_instance)
            return {'mensaje': 'Nombre del servidor actualizado con éxito'}, 200
        else:
            return {'mensaje': 'No se encontró el servidor '}, 400
        
    @classmethod
    def delete_server_controller(cls, id_servidor):
        if ServidorModel.delete_server_model(id_servidor):
            return {'mensaje': 'Servidor eliminado con éxito'}, 204
        else:
            return {'mensaje': 'No se pudo eliminar el servidor'}, 500
        