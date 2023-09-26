from ..database import DatabaseConnection
class Usuarios:
    def __init__(self,id_usuario=None, nombre_usuario=None,nombre=None,apellido=None,email=None,contrasenia=None,id_imagen=None):
        self.id_usuario = id_usuario
        self.nombre_usuario=nombre_usuario
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.contrasenia=contrasenia
        self.id_imagen=id_imagen
    
    @classmethod 
    def get_usuario(self, email):
        query="SELECT usuarios.id_usuario, usuarios.nombre_usuario, usuarios.nombre, usuarios.apellido, usuarios.email, usuarios.contrasenia, usuarios.id_imagen FROM chat_master.usuarios WHERE usuarios.email=%s;"
        params=email,
        result= DatabaseConnection.fetch_one(query,params)
        if result is not None:
            return Usuarios(
                id_usuario=result[0],
                nombre_usuario=result[1],
                nombre=result[2],
                apellido=result[3],
                email=result[4],
                contrasenia=result[5],
                id_imagen=result[6]
            )
        else:
            return None
    
    @classmethod
    def get_usuarios(self):
        query="SELECT id_usuario, nombre_usuario, nombre, apellido, email, contrasenia, id_imagen FROM chat_master.usuarios;"
        result=DatabaseConnection.fetch_all(query)
        if result is not None:
            return result
        else:
            return None

    @classmethod
    def update_usuario(self, usuario):
        query="UPDATE chat_master.usuarios SET nombre_usuario=%s, nombre=%s, apellido=%s, email=%s, contrasenia=%s, id_imagen=%s WHERE id_usuario = %s;"
        params=(usuario.nombre_usuario, usuario.nombre, usuario.apellido, usuario.email, usuario.contrasenia, usuario.id_imagen, usuario.id_usuario)
        DatabaseConnection.execute_query(query, params)
        return True
    
    @classmethod
    def create_usuario(self, usuario):
        query="INSERT INTO chat_master.usuarios(nombre_usuario, nombre, apellido, email, contrasenia, id_imagen) VALUES(%s, %s, %s, %s, %s, %s);"
        params=(usuario.nombre_usuario, usuario.nombre, usuario.apellido, usuario.email, usuario.contrasenia, usuario.id_imagen)
        DatabaseConnection.execute_query(query, params)
        return True

    @classmethod
    def delete_usuario(self, id_usuario):
        query="DELETE FROM chat_master.usuarios WHERE usuarios.id_usuario=%s;"
        params=id_usuario, 
        DatabaseConnection.execute_query(query, params)
        return True
    
    @classmethod
    def is_registered(cls, usuario):
        query = "SELECT id_usuario FROM chat_master.usuarios WHERE email = %(email)s and contrasenia = %(contrasenia)s"
        params = usuario.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)
        
        if result is not None:
            return True
        return False