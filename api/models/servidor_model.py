from ..database import DatabaseConnection

class ServidorModel:
    def __init__ (self, id_servidor=None, nombre_servidor=None, imagen_servidor=None):
        self.id_servidor = id_servidor
        self.nombre_servidor = nombre_servidor
        self.imagen_servidor = imagen_servidor

    @classmethod
    def get_server_model (cls, id_servidor):
        query = "SELECT servidores.id_servidor, servidores.nombre_servidor, servidores.imagen_servidor FROM chat_master.servidores WHERE servidores.id_servidor=%s;" 
        params = id_servidor,
        result = DatabaseConnection.fetch_one(query,params)
        return result
        
    @classmethod
    def get_server_by_name(cls, nombre_servidor):
        query = "SELECT servidores.id_servidor, servidores.nombre_servidor, servidores.imagen_servidor FROM chat_master.servidores WHERE servidores.nombre_servidor = %s;" 
        params = (nombre_servidor,)
        result = DatabaseConnection.fetch_one(query, params)
        return result

    @classmethod
    def get_all_servers_model (cls):
        query = "SELECT servidores.id_servidor, servidores.nombre_servidor, servidores.imagen_servidor FROM chat_master.servidores;"
        result = DatabaseConnection.fetch_all(query)
        return result
        
    @classmethod
    def exists(cls, id_servidor):
        query = "SELECT servidores.nombre_servidor FROM chat_master.servidores WHERE servidores.id_servidor=%s;"
        params = id_servidor,
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return True
        return False

    @classmethod
    def create_server_model(cls,servidor):
        query = "INSERT INTO chat_master.servidores (servidores.id_servidor, servidores.nombre_servidor, servidores.imagen_servidor) VALUES (%s,%s,%s);"
        params = servidor.id_servidor, servidor.nombre_servidor, servidor.imagen_servidor,
        result = DatabaseConnection.execute_query(query,params)
        return result


    @classmethod
    def update_server_model(cls, servidor):
        query = "UPDATE chat_master.servidores SET servidores.nombre_servidor=%s, servidores.imagen_servidor=%s WHERE servidores.id_servidor=%s;"
        params = servidor.nombre_servidor, servidor.imagen_servidor, servidor.id_servidor
        result = DatabaseConnection.execute_query(query, params)
        return result  
    
    @classmethod
    def delete_server_model (cls, id_servidor):
        query = "DELETE FROM chat_master.servidores WHERE servidores.id_servidor = %s"
        params = id_servidor,
        DatabaseConnection.execute_query(query, params)
        return True