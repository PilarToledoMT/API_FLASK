from ..models.canal_model import Canal
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
        print('HOLA MUNDO')
        canales_list = Canal.get_canales()
        canales = []
        for canal in canales_list:
            canales.append({
                'id_canal': canal[0],
                'nombre_canal': canal[1],
                'id_servidor': canal[2]
                })
        return {'canales': canales}, 200
    