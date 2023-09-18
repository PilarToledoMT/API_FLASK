from ..database import DatabaseConnection

class servidor:
    def __init__ (self, nombre_servidor=None, id_servidor=None):
        self.nombre_servidor = nombre_servidor
        self.id_servidor = id_servidor

    #def serialize (self):??
    '''toma un objeto de la clase servidor y lo convierte en una representación serializada en forma 
    de diccionario, ya que es fácilmente procesable o transferible.
    '''
    @classmethod
    def get_server (cls, server):
        query = "SELECT servidores.nombre_servidor FROM chat_master.servidores WHERE servidores.id_servidor=%s;" 
        params = server.id_servidor
        DatabaseConnection.fetch_one(query,params)

    @classmethod
    def get_all_servers (cls):
        query = "SELECT servidores.id_servidor, servidores.nombre_servidor FROM chat_master.servidores;"
        result = DatabaseConnection.fetch_all(query)
        if result is not None:
            return result
        return None

    @classmethod
    def exists(cls, server):
        query = "SELECT servidores.nombre_servidor FROM chat_master.servidores WHERE servidores.id_servidor=%s;"
        params = server.id_servidor,
        result = DatabaseConnection.fetch_one(query, params)

    @classmethod
    def create_server(cls, server):
        query = "INSERT INTO chat_master.servidores (servidores.nombre_servidor) VALUES (%s);"
        params = server.nombre_servidor
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def change_server_name(cls, server):
        query = "UPDATE chat_master.servidores SET servidores.nombre_servidor WHERE servidores.id_servidor=%s;"
        params = server.id_servidor
        DatabaseConnection.execute_query(query,params)

    @classmethod
    def delete_server (cls, server):
        query = "DELETE FROM chat_master.servidores WHERE servidores.id_servidor = %s"
        params = server.id_servidor,
        DatabaseConnection.execute_query(query, params)
