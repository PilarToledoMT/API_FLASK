from ..database import DatabaseConnection
class ImagenPerfil:
    def __init__(self, id_imagen,imagen):
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