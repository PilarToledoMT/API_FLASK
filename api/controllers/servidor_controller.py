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
            return jsonify({'msg': 'No se encontró el servidor'}), 404
        
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
            return jsonify({'mensaje':'no se encontro servidor'}),404
        
    @classmethod
    def create_server_controller (cls):
        data = request.json
        servidor_instance = ServidorModel(
            nombre_servidor=data.get('nombre_servidor'),
            imagen_servidor=data.get('imagen_servidor')
        )
        if ServidorModel.existsByName(servidor_instance.nombre_servidor):
            return jsonify({'mensaje':'el nombre del servidor ya se encuentra en la base de datos'}),404
        else:
            ServidorModel.create_server_model(servidor_instance)
            return jsonify({'message': 'Servidor creado con exito'}), 200

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
            return jsonify({'mensaje': 'Nombre del servidor actualizado con éxito'}), 200
        else:
            return jsonify({'mensaje': 'No se encontró el servidor '}), 400
        
    @classmethod
    def delete_server_controller(cls, id_servidor):
        if ServidorModel.delete_server_model(id_servidor):
            return jsonify({'mensaje': 'Servidor eliminado con éxito'}), 204
        else:
            return jsonify({'mensaje': 'No se pudo eliminar el servidor'}), 500
    
    @classmethod
    def mostrar_servidores_usuario(cls, id_usuario):
        servidores = ServidorModel.get_servidores_usuario(id_usuario)
        if servidores:
            lista_servidores = []
            for servidor in servidores:
                response = {
                    'id_servidor':servidor[0],
                    'nombre_servidor':servidor[1],
                    'imagen_servidor':servidor[2]
                }
                lista_servidores.append(response)
            return jsonify(lista_servidores),200
        else:
            return jsonify({'mensaje':'no se encontro servidor'}), 404
        

    @classmethod
    def search_servers_by_name_controller(cls):
        data = request.json
        buscar_servidor = data.get('nombre_servidor')
        print(buscar_servidor)
        
        if buscar_servidor:
            server = ServidorModel.get_server_by_name(buscar_servidor)
            print(server)
            if server:
                response = {
                    #'id_servidor': server[0],
                    'nombre_servidor': server[0]
                    #'imagen_servidor': server[2]
                }
                return jsonify(response), 200
            else:
                return {'msg': 'No se encontraron servidores que coincidan con el término de búsqueda'}, 404
        else:
            return {'msg': 'Proporciona un término de búsqueda válido'}, 400

    @classmethod
    def get_servers_by_partial_name(cls):
        data=request.json
        partial_name = data.get('partial_name')

        if not partial_name:
            return jsonify({'error': 'Debe ingresar un nombre'}), 400

        results = ServidorModel.get_servers_by_partial_name(partial_name)

        if not results:
            return jsonify({'message': 'No se encontraron servidores con el nombre parcial proporcionado'}), 404

        # Formatear los resultados para obtener todos los nombres de servidores que coinciden
        list_servers = [result[0] for result in results]
        
        return jsonify({'servers': list_servers}), 200
