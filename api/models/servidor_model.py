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
        query = "SELECT servidores.nombre_servidor FROM chat_master.servidores WHERE servidores.nombre_servidor = %s;" 
        params = (nombre_servidor,)
        result = DatabaseConnection.fetch_one(query, params)
        return result
    
    @classmethod
    def get_servers_by_partial_name(cls, partial_name):
        query = "SELECT servidores.nombre_servidor FROM chat_master.servidores WHERE servidores.nombre_servidor LIKE %s;"
        # Usamos % antes y después de partial_name para buscar nombres que contengan la cadena dada.
        params = ('%' + partial_name + '%',)
        results = DatabaseConnection.fetch_all(query, params)
        return results


    @classmethod
    def get_all_servers_model (cls):
        query = "SELECT servidores.id_servidor, servidores.nombre_servidor, servidores.imagen_servidor FROM chat_master.servidores;"
        result = DatabaseConnection.fetch_all(query)
        return result
        
    @classmethod
    def existsByID(cls, id_servidor):
        query = "SELECT servidores.nombre_servidor FROM chat_master.servidores WHERE servidores.id_servidor=%s;"
        params = id_servidor,
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return True
        return False

    @classmethod
    def existsByName(cls, nombreservidor):
        query = "SELECT servidores.nombre_servidor FROM chat_master.servidores WHERE servidores.nombre_servidor=%s;"
        params = nombreservidor,
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
        # Eliminar registros relacionados en la tabla mensajes
        query_delete_relations_mensajes = "DELETE FROM chat_master.mensajes WHERE id_canal IN (SELECT id_canal FROM chat_master.canales WHERE id_servidor = %s);"
        params_delete_relations_mensajes = (id_servidor,)
        DatabaseConnection.execute_query(query_delete_relations_mensajes, params_delete_relations_mensajes)

        # Eliminar registros relacionados en la tabla canales
        query_delete_relations_canales = "DELETE FROM chat_master.canales WHERE id_servidor = %s;"
        params_delete_relations_canales = (id_servidor,)
        DatabaseConnection.execute_query(query_delete_relations_canales, params_delete_relations_canales)

        # Eliminar registros relacionados en usuario_servidor
        query_delete_relations_usuario_servidor = "DELETE FROM chat_master.usuario_servidor WHERE id_servidor = %s;"
        params_delete_relations_usuario_servidor = (id_servidor,)
        DatabaseConnection.execute_query(query_delete_relations_usuario_servidor, params_delete_relations_usuario_servidor)

        query = "DELETE FROM chat_master.servidores WHERE servidores.id_servidor = %s"
        params = id_servidor,
        DatabaseConnection.execute_query(query, params)
        return True
    
    @classmethod
    def get_servidores_usuario(cls, id_usuario):
        DatabaseConnection.execute_query("USE chat_master;")
        query = """SELECT servidores.id_servidor, servidores.nombre_servidor, servidores.imagen_servidor
                    FROM chat_master.usuario_servidor
                    JOIN servidores ON usuario_servidor.id_servidor = servidores.id_servidor
                    WHERE chat_master.usuario_servidor.id_usuario = %s"""
        params = id_usuario,
        result = DatabaseConnection.fetch_all(query, params)
        return result