from ..models.canal import Canal
from flask import request, jsonify

class CanalController:
    @classmethod
    def home(cls):
        return{'msg': 'Estas en el home'}


    @classmethod
    def get_canal(cls, id_canal):
        canal_instance = Canal.get_canal(id_canal)
        if canal_instance:
            response_data = {'id_canal': canal_instance.id_canal,
                            'nombre_canal': canal_instance.nombre_canal,
                            'id_servidor': canal_instance.id_servidor
                            }  
            return jsonify(response_data), 200
        else:
            return {'msg': 'No se encontró el canal'}, 404
        
    @classmethod
    def get_canales(cls):
        canales_list = Canal.get_canales()
        canales = []
        for canal in canales_list:
            canales.append({
                'id_canal': canal[0],
                'nombre_canal': canal[1],
                'id_servidor': canal[2]
                })
        return {'canales': canales}, 200
    
    @classmethod
    def get_canales_por_servidor(cls, id_servidor):
        canales_list = Canal.get_canales()
        canales_por_servidor = []
        for canal in canales_list:
            if canal[2] == id_servidor:
                canales_por_servidor.append({
                    'id_canal': canal[0],
                    'nombre_canal': canal[1],
                    'id_servidor': canal[2]
                    })
        if canales_por_servidor is not None:     
            return {'canales por servidor': canales_por_servidor}, 200
        else:
            return {'msg': 'Este servidor no posee ningún canal, por favor crea uno'}
    
    @classmethod
    def create_canal(cls):
        canal = Canal(
            nombre_canal = request.args.get('nombre_canal'),
            id_servidor = request.args.get('id_servidor')
        )
        Canal.create_canal(canal)
        return {'msg': 'Canal creado con exito'}, 200

    