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
        query = "SELECT nombre_servidor FROM NombreBd.NombreTabla WHERE id_servidor=%s;" 
        params = server.id_servidor
        DatabaseConnection.fetch_one(query,params)

    @classmethod
    def get_all_servers (cls):
        query = "SELECT nombre_servidor FROM NombreBd.NombreTabla;"
        DatabaseConnection.fetch_all(query)

    @classmethod
    def exists(cls, server):
        query = "SELECT nombre_servidor FROM NombreBd.NombreTabla WHERE id_servidor=%s;"
        params = server.id_servidor,
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return True
        return False

    @classmethod
    def create_server(cls, server):
        query = "INSERT INTO NombreBd.NombreTabla (nombre_servidor) VALUES (%s);"
        params = server.nombre_servidor
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def change_server_name(cls, server):
        query = "UPDATE NombreBd.NombreTabla SET nombre_servidor WHERE id_servidor=%s;"
        params = server.id_servidor
        DatabaseConnection.execute_query(query,params)

    @classmethod
    def delete_server (cls, server):
        query = "DELETE FROM NombreBd.NombreTabla WHERE id_servidor = %s"
        params = server.id_servidor,
        DatabaseConnection.execute_query(query, params)
