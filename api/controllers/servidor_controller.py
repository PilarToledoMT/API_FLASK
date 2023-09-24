from ..models.servidor_model import ServidorModel
from flask import request,jsonify

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
        

            
