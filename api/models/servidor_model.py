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
        if result is not None:
            return ServidorModel(
                id_servidor=result[0],
                nombre_servidor=result[1],
                imagen_servidor=result[2]
            )
        else:
            return None
    
    '''@classmethod
    def get_all_servers (cls):
        query = "SELECT servidores.id_servidor, servidores.nombre_servidor, servidores.imagen_servidor FROM chat_master.servidores;"
        result = DatabaseConnection.fetch_all(query)
        if result is not None:
            return result
        return None

    @classmethod
    def exists(cls, servidor):
        query = "SELECT servidores.nombre_servidor FROM chat_master.servidores WHERE servidores.id_servidor=%s;"
        params = servidor,
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return True
        return False

    @classmethod
    def create_server(cls, servidor):
        query = "INSERT INTO chat_master.servidores (servidores.nombre_servidor, servidores.imagen_servidor) VALUES (%s,%s);"
        params = servidor, 
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def change_server_name(cls, servidor):
        query = "UPDATE chat_master.servidores SET servidores.nombre_servidor WHERE servidores.id_servidor=%s;"
        params = servidor,
        DatabaseConnection.execute_query(query,params)

    @classmethod
    def delete_server (cls, servidor):
        query = "DELETE FROM chat_master.servidores WHERE servidores.id_servidor = %s"
        params = servidor,
        DatabaseConnection.execute_query(query, params)
    '''