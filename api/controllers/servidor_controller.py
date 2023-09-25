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
        data_instance = ServidorModel(
            nombre_servidor = data.get('nombre_servidor'),
            imagen_servidor = data.get('ruta_servidor')
        )

        if ServidorModel.exists_nombre(data_instance.nombre_servidor):
            return {'mensaje':'El nombre ya existe'}, 400
        else:
            servidor_nuevo = ServidorModel(**data)
            ServidorModel.create_server_model(servidor_nuevo)
            return {'message': 'Servidor creado con exito'}, 200
        
    @classmethod
    def change_server_name_controller(cls, id_servidor):
        data = request.json
        nuevo_nombre_servidor = data.get('nombre_servidor')

        if not ServidorModel.exists_nombre(nuevo_nombre_servidor):
            return {'mensaje': 'El nombre del servidor proporcionado no existe'}, 400

        if ServidorModel.change_server_name_model(id_servidor, nuevo_nombre_servidor):
            return {'message': 'Servidor modificado con éxito'}, 200
        else:
            return {'mensaje': 'Error al modificar el servidor'}, 500
        

            
