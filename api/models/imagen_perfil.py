from ..database import DatabaseConnection
class ImagenPerfil:
    def __init__(self, id_imagen=None,imagen=None):
        self.id_imagen=id_imagen
        self.imagen=imagen

    @classmethod
    def get_imagen(cls, id_imagen):
        query="SELECT imagen_perfil.id_imagen, imagen_perfil.imagen FROM chat_master.imagen_perfil WHERE imagen_perfil.id_imagen=%s;"
        params= id_imagen,
        result= DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return ImagenPerfil(
                id_imagen=result[0],
                imagen=result[1]
            )
        else:
            return None

    @classmethod
    def get_imagenes(cls):
        query="SELECT id_imagen, imagen FROM chat_master.imagen_perfil;"
        result= DatabaseConnection.fetch_all(query)
        if result is not None:
            return result
        else:
            return None

    @classmethod
    def create_imagen(cls, imagen):
        query ="INSERT INTO chat_master.imagen_perfil(imagen) VALUES (%s);"
        params=(imagen.imagen,)
        DatabaseConnection.execute_query(query, params)
        return True
    
    @classmethod
    def update_imagen(cls, imagen):
        query="UPDATE chat_master.imagen_perfil SET imagen=%s WHERE id_imagen=%s;"
        params=(imagen.imagen,)
        DatabaseConnection.execute_query(query,params)
        return True

    @classmethod
    def delete_imagen(cls, id_imagen):
        query="DELETE FROM chat_master.imagen_perfil WHERE imagen_perfil.id_imagen=%s;"
        params= id_imagen, 
        DatabaseConnection.execute_query(query, params)
        return True
        