from ..models.imagen_perfil import ImagenPerfil
from flask import request, jsonify
class ImagenPerfilController:
    @classmethod 
    def get_imagen(cls, imagen):
        imagen_instance=ImagenPerfil.get_imagen(imagen)
        if imagen_instance:
            response_data={
                "id_imagen":imagen_instance.id_imagen,
                "imagen": imagen_instance.imagen
            }
            return jsonify (response_data),200
        else:
            return {
                "msg": "No se encontro la imagen"
            },404
        
    @classmethod
    def get_imagenes(cls):
        lista_imagenes=ImagenPerfil.get_imagenes()
        imagenes=[]
        for imagen in lista_imagenes:
            imagenes.append({
                "id_imagen":imagen[0],
                "imagen":imagen[1]
            })
        response={"imagenes_perfil":imagenes}
        return jsonify(response),200

    @classmethod
    def create_imagen(cls):
        imagen_parametro = request.args.get('imagen')
        if imagen_parametro:
            imagen = ImagenPerfil(imagen=imagen_parametro)
            ImagenPerfil.create_imagen(imagen)
            return {"msg":"Imagen creada con exito"},200
        else:
            return {'msg':"No se pudo crear la imagen de perfil"}, 400

    @classmethod
    def update_imagen(cls, id_imagen):
        imagen_instance=ImagenPerfil.get_imagen(id_imagen)
        imagen=ImagenPerfil(
            id_imagen=imagen_instance.id_imagen, 
            imagen= request.args.get("imagen")
        )
        if ImagenPerfil.update_imagen (imagen):
            return {"msg": "Imagen modificada con exito"},201
        else:
            return{"msg":"No se pudo modificar la imagen"}

    @classmethod
    def delete_imagen(cls, id_imagen):
        if ImagenPerfil.delete_imagen(id_imagen):
            return {"msg":"Imagen eliminada"},204
        else:
            return {"msg":"No se pudo eliminar la imagen"}


    