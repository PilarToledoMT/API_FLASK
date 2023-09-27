CREATE DATABASE chat_master;
USE chat_master;
CREATE TABLE servidores(
	id_servidor INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, 
    nombre_servidor VARCHAR (100),
    imagen_servidor VARCHAR (200)
    )ENGINE=InnoDB;

CREATE TABLE imagen_perfil(
	id_imagen INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    imagen VARCHAR(100)
    ) ENGINE= InnoDB;

CREATE TABLE usuarios(
	id_usuario INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    nombre_usuario VARCHAR(100),
    nombre VARCHAR(100),
    apellido VARCHAR (100),
    email VARCHAR(100),
    contrasenia VARCHAR(50),
    id_imagen INT NOT NULL, 
    CONSTRAINT fk_id_imagen FOREIGN KEY(id_imagen)
    REFERENCES imagen_perfil(id_imagen)
    ) ENGINE=InnoDB;

CREATE TABLE usuario_servidor(
	id_usuario_servidor INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, 
    id_usuario INT NOT NULL,
    id_servidor INT NOT NULL,
    CONSTRAINT fk_usuario FOREIGN KEY (id_usuario)
    REFERENCES usuarios (id_usuario),
    CONSTRAINT fk_servidor FOREIGN KEY (id_servidor)
    REFERENCES servidores (id_servidor)
    ) ENGINE=InnoDB;

CREATE TABLE canales( 
	id_canal INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
	nombre_canal VARCHAR(100),
	id_servidor INT NOT NULL,
	CONSTRAINT fk_servidor_can FOREIGN KEY (id_servidor)
	REFERENCES servidores (id_servidor)
    ) ENGINE=InnoDB;
    
CREATE TABLE mensajes(
	id_mensaje INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    mensaje VARCHAR(500),
    fecha_hora DATETIME,
    id_usuario INT NOT NULL,
    id_canal INT NOT NULL,
    CONSTRAINT fk_usuario_msj FOREIGN KEY(id_usuario)
    REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_canal FOREIGN KEY (id_canal)
    REFERENCES canales(id_canal)
    )ENGINE=InnoDB;

    



    