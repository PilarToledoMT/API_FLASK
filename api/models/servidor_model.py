from ..database import DatabaseConnection

class ServidorModel:
    def __init__ (self, nombre_servidor=None, id_servidor=None, imagen_servidor=None):
        self.nombre_servidor = nombre_servidor
        self.id_servidor = id_servidor
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
    def exists_nombre(cls, nombre_servidor):
        query = "SELECT servidores.nombre_servidor FROM chat_master.servidores WHERE servidores.nombre_servidor=%s;"
        params = nombre_servidor,
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return True
        return False

    @classmethod
    def create_server_model(cls,product):
        query = "INSERT INTO chat_master.servidores (servidores.nombre_servidor, servidores.imagen_servidor) VALUES (%s,%s);"
        params = product.nombre_servidor, product.imagen_servidor,
        result = DatabaseConnection.execute_query(query,params)
        return result


    @classmethod
    def update_server_name(cls, current_name, new_name):
        if cls.exists_nombre(new_name):
            return False  

        server_instance = cls.get_server_by_name(current_name)
        if server_instance:
            query = "UPDATE chat_master.servidores SET nombre_servidor = %s WHERE id_servidor = %s"
            params = (new_name, server_instance[0])  
            DatabaseConnection.execute_query(query, params)

            return True  
        else:
            return False
    
    @classmethod
    def delete_server (cls, servidor):
        query = "DELETE FROM chat_master.servidores WHERE servidores.id_servidor = %s"
        params = servidor,
        DatabaseConnection.execute_query(query, params)
    