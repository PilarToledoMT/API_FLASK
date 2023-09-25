from ..models.servidor_model import ServidorModel
from flask import request,jsonify,json

class ServidorController:

    @classmethod
    def get_server_controller(cls,id_servidor):
        server_instance = ServidorModel.get_server_model(id_servidor)
        if server_instance:
            response_data = {
<<<<<<< HEAD
                'id_servidor': server_instance.id_servidor,
                'nombre_servidor': server_instance.nombre_servidor,
                'imagen_servidor': server_instance.imagen_servidor
            }
=======
                'id_servidor':server_instance[0],
                'nombre_servidor':server_instance[1],
                'imagen_servidor':server_instance[2]
                }
>>>>>>> 79dff22d6821aa28142977aeec1ccb89a4626a2c
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
    def change_server_name_controller(cls):
        data = request.json
        new_name = data.get('nuevo_nombre')
        current_name = data.get('nombre_actual')  # Assuming the current name is provided in the JSON data

        # Use the ServidorModel method to update the server's name
        success = ServidorModel.update_server_name(current_name, new_name)

        if success:
            return {'mensaje': 'Nombre del servidor actualizado con éxito'}, 200
        else:
            return {'mensaje': 'No se encontró el servidor con el nombre actual proporcionado o el nuevo nombre ya existe'}, 400