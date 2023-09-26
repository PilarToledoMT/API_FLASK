from ..models.usuarios import Usuarios
from ..models.imagen_perfil import ImagenPerfil
from flask import request, jsonify, session
class UsuarioController:
    @classmethod
    def get_usuario(cls, email):
        usuario_instance= Usuarios.get_usuario(email)
        imagen_instance= ImagenPerfil.get_imagen(id_imagen=usuario_instance.id_imagen)
        if usuario_instance:
            response_data={
                "id_usuario":usuario_instance.id_usuario, 
                "nombre_usuario": usuario_instance.nombre_usuario,
                "nombre": usuario_instance.nombre,
                "apellido":usuario_instance.apellido,
                "email":usuario_instance.email,
                "contrasenia": usuario_instance.contrasenia,
                "imagen_perfil": {"id_imagen":usuario_instance.id_imagen, 
                                    "imagen": imagen_instance.imagen}
            }
            return jsonify(response_data),200
        else:
            return {"msg":"No se encontró el usuario"},400
    @classmethod
    def get_usuarios(cls):
        lista_usuarios=Usuarios.get_usuarios()
        usuarios=[]
        for usuario in lista_usuarios:
            imagen=ImagenPerfil.get_imagen(usuario[6])
            usuarios.append({
                "id_usuario":usuario[0],
                "nombre_usuario":usuario[1],
                "nombre":usuario[2],
                "apellido":usuario[3],
                "email": usuario[4],
                "contrasenia":usuario[5],
                "imagen_perfil":{"id_imagen":imagen.id_imagen,
                                    "imagen":imagen.imagen}
            })
        response= {"usuarios":usuarios}
        return jsonify(response),200
    
    @classmethod 
    def create_usuario(cls):
        usuario=Usuarios(
            nombre_usuario=request.args.get("nombre_usuario"),
            nombre=request.args.get("nombre"),
            apellido=request.args.get("apellido"),
            email=request.args.get("email"),
            contrasenia=request.args.get("contrasenia"),
            id_imagen=request.args.get("id_imagen")
        )
        Usuarios.create_usuario(usuario)
        return {"msg":"Usuario creado"},200
    
    @classmethod
    def update_usuario(cls,id_usuario):
        usuario_instance=Usuarios.get_usuario(id_usuario)
        usuario=Usuarios(
            id_usuario=usuario_instance.id_usuario,
            nombre_usuario=request.args.get("nombre_usuario"),
            nombre=request.args.get("nombre"),
            apellido=request.args.get("apellido"),
            email=request.args.get("email"),
            contrasenia=request.args.get("contrasenia"),
            id_imagen=request.args.get("id_imagen")
        )
        if Usuarios.update_usuario(usuario):
            return {"msg":"Usuario modificado"},200
        else:
            return {"msg":"No se pudo modificar el usuario"}

    @classmethod
    def delete_usuario(cls, id_usuario):
        if Usuarios.delete_usuario(id_usuario):
            return {"msg":"Usuario eliminado"}, 200
        else:
            return{"msg":"No se pudo eliminar el usuario"}

    @classmethod
    def login(cls):
        if request.method == 'POST':
            try:
                email = request.form['email']
                contrasenia = request.form['contrasenia']
                usuario_model = Usuarios()
                usuario = usuario_model.login(email, contrasenia)
                
                if usuario:
                    session['id_usuario'] = usuario[0]
                    return {'msg': 'Inicio de sesión exitoso'}, 200
                else:
                    return {'msg': "Credenciales incorrectas"}, 401
            except KeyError:
                return {'msg': 'Campo "email" faltante en la solicitud'}, 400