from ..database import DatabaseConnection

class Mensajes:
    def __init__(self, id_mensaje = None, mensaje = None, fecha_hora = None, id_usuario = None, id_canal = None):
        self.id_mensaje = id_mensaje
        self.mensaje = mensaje
        self.fecha_hora = fecha_hora
        self.id_usuario = id_usuario
        self.id_canal = id_canal
    
    @classmethod
    def get_mensaje(cls, id_mensaje):
        query = "SELECT chat_master.id_mensaje, chat_master.mensaje, chat_master.fecha_hora, chat_master.id_usuario, chat_master.id_canal FROM chat_master.mensajes WHERE mensajes.id_mensaje = %s;"
        params = id_mensaje,
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Mensajes(
                id_mensaje = result[0],
                mensaje = result[1],
                fecha_hora = result[2],
                id_usuario = result[3],
                id_canal = result[4]
            )
        else:
            return None
    
    @classmethod
    def get_mensajes(cls, id_canal):
        query = "SELECT id_mensaje, mensaje, fecha_hora, id_usuario, id_canal FROM chat_master.mensajes WHERE mensajes.id_canal = %s ORDER BY fecha_hora ASC;"
        params = (id_canal,)
        result = DatabaseConnection.fetch_all(query, params)
        if result is not None:
            return result
        else:
            return None
    
    @classmethod
    def create_mensaje(self, mensaje):
        query = "INSERT INTO chat_master.mensajes(mensaje, fecha_hora, id_usuario, id_canal) VALUES(%s, %s, %s, %s);"
        params = (mensaje.mensaje, mensaje.fecha_hora, mensaje.id_usuario, mensaje.id_canal)
        DatabaseConnection.execute_query(query, params)
        return True
    
    @classmethod
    def delete_mensaje(self, id_mensaje):
        query = "DELETE FROM chat_master.mensajes WHERE mensajes.id_mensaje = %s;"
        params = id_mensaje,
        DatabaseConnection.execute_query(query, params)
        return True
    
    @classmethod
    def update_mensaje(self, mensaje):
        query = "UPDATE chat_master.mensajes SET mensaje = %s, fecha_hora = %s, id_usuario = %s, id_canal = %s WHERE id_mensaje = %s;"
        params = (mensaje.mensaje, mensaje.fecha_hora, mensaje.id_usuario, mensaje.id_canal)
        DatabaseConnection.execute_query(query, params)
        return True