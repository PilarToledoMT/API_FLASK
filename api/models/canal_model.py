from ..database import DatabaseConnection

class Canal:
    def __init__(self, id_canal, nombre_canal, id_servidor):
        self.id_canal = id_canal
        self.nombre_canal = nombre_canal
        self.id_servidor = id_servidor
        
    @classmethod
    def get_canal(cls, id_canal):
        query = "SELECT canales.id_canal, canales.nombre_canal, canales.id_servidor FROM chat_master.canales WHERE canales.id_canales = %s;"
        params = id_canal,
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Canal(
                id_canal = result[0],
                nombre_canal = result[1],
                id_servidor = result[2]
            )
        else:
            return None
        
    @classmethod
    def get_canales(cls):
        query = "SELECT canales.id_canal, canales.nombre_canal, canales.id_servidor FROM chat_master.canales;"
        result = DatabaseConnection.fetch_all(query)
        if result is not None:
            return result
        else:
            return None


        
    @classmethod
    def create_canal(cls, canal):
        query = "INSERT INTO chat_master.canales(nombre_canal, id_servidor) VALUES(%s, %s);"
        params = (canal.nombre_canal, canal.id_servidor)
        DatabaseConnection.execute_query(query, params)
        return True

