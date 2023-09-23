from ..models.mensajes import Mensajes
from flask import jsonify, request

class MensajesController:
    @classmethod
    def get_mensajes(cls, id_canal):
        lista_mensajes = Mensajes.get_mensajes(id_canal)
        mensajes = []
        for mensaje in lista_mensajes:
            mensajes.append({
                'id_mensaje': mensaje[0],
                'mensaje': mensaje[1],
                'fecha_hora': mensaje[2],
                'id_usuario': mensaje[3],
                'id_canal': mensaje[4]
            })
        
        response = {
            'mensajes': mensajes
        }
        
        return jsonify(response), 200
    
    @classmethod
    def create_mensaje(cls):
        mensajes = Mensajes(
            mensaje = request.args.get('mensaje'),
            fecha_hora = request.args.get('fecha_hora'),
            id_usuario = request.args.get('id_usuario'),
            id_canal = request.args.get('id_canal')
        )
        Mensajes.create_mensaje(mensajes)
        return {'msg': 'Mensaje creado exitosamente'}, 200

    @classmethod
    def delete_mensaje(cls, id_mensaje):
        if Mensajes.delete_mensaje(id_mensaje):
            return {'msg': 'Mensaje eliminado'}, 204
        else:
            return {'msg': 'No se pudo eliminar el mensaje'}