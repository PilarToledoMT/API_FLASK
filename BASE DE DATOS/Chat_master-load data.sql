USE chat_master;
INSERT INTO chat_master.imagen_perfil (imagen) VALUES ("../assets/user.png");
INSERT INTO chat_master.imagen_perfil (imagen) VALUES ("../assets/avatar1.jpg");
INSERT INTO chat_master.imagen_perfil (imagen) VALUES ("../assets/avatar2.jpg");
INSERT INTO chat_master.imagen_perfil (imagen) VALUES ("../assets/avatar3.jpg");
INSERT INTO chat_master.imagen_perfil (imagen) VALUES ("../assets/avatar4.jpg");
INSERT INTO chat_master.imagen_perfil (imagen) VALUES ("../assets/avatar5.jpg");
INSERT INTO chat_master.imagen_perfil (imagen) VALUES ("../assets/avatar6.jpg");

INSERT INTO chat_master.usuarios(nombre_usuario, nombre, apellido, email, contrasenia, id_imagen) VALUES ("PilarToledoMT", "Pilar", "Toledo", "plrtoledo@gmail.com", "pilarto123", 4);
INSERT INTO chat_master.usuarios(nombre_usuario, nombre, apellido, email, contrasenia, id_imagen) VALUES ("mariadcb", "Maria", "Costa", "mdcostab@gmail.com", "mariac123", 7);
INSERT INTO chat_master.usuarios(nombre_usuario, nombre, apellido, email, contrasenia, id_imagen) VALUES ("raffalopez21", "Rafael", "Lopez", "raffalopez@gmail.com", "raffalo123", 2);
INSERT INTO chat_master.usuarios(nombre_usuario, nombre, apellido, email, contrasenia, id_imagen) VALUES ("leovillegas94", "Leonardo", "Villegas", "leonardovillegascosta@gmail.com", "leovc123", 2);

INSERT INTO chat_master.servidores(nombre_servidor, imagen_servidor) VALUES ("Literatura Fantástica", "../assets/literatura.png");
INSERT INTO chat_master.servidores(nombre_servidor, imagen_servidor) VALUES ("Programación Web", "../assets/programacion.png");

INSERT INTO chat_master.usuario_servidor(id_usuario, id_servidor) VALUES (1,1);
INSERT INTO chat_master.usuario_servidor(id_usuario, id_servidor) VALUES (1,2);
INSERT INTO chat_master.usuario_servidor(id_usuario, id_servidor) VALUES (2,1);
INSERT INTO chat_master.usuario_servidor(id_usuario, id_servidor) VALUES (2,2);
INSERT INTO chat_master.usuario_servidor(id_usuario, id_servidor) VALUES (3,1);
INSERT INTO chat_master.usuario_servidor(id_usuario, id_servidor) VALUES (3,2);
INSERT INTO chat_master.usuario_servidor(id_usuario, id_servidor) VALUES (4,1);
INSERT INTO chat_master.usuario_servidor(id_usuario, id_servidor) VALUES (4,2);

INSERT INTO chat_master.canales(nombre_canal, id_servidor) VALUES ("#Club de lectura", 1);
INSERT INTO chat_master.canales(nombre_canal, id_servidor) VALUES ("#Escritores emergentes", 1);
INSERT INTO chat_master.canales(nombre_canal, id_servidor) VALUES ("#Recomendaciones", 1);
INSERT INTO chat_master.canales(nombre_canal, id_servidor) VALUES ("#Preguntas técnicas", 2);
INSERT INTO chat_master.canales(nombre_canal, id_servidor) VALUES ("#Proyectos compartidos", 2);
INSERT INTO chat_master.canales(nombre_canal, id_servidor) VALUES ("#Recursos útiles", 2);

INSERT INTO chat_master.mensajes(mensaje, fecha_hora, id_usuario, id_canal) VALUES ("Hola a todos! soy nuevo en este club de lectura. Alguién ha leído alguna obra de Sanderson?", NOW(), 1, 1);
INSERT INTO chat_master.mensajes(mensaje, fecha_hora, id_usuario, id_canal) VALUES ("Hola, yo leí El Archivo de las Tormentas", NOW(), 2, 1);
INSERT INTO chat_master.mensajes(mensaje, fecha_hora, id_usuario, id_canal) VALUES ("Hola a todos! Yo soy un gran fan de Sanderson!", NOW(), 3, 1);
INSERT INTO chat_master.mensajes(mensaje, fecha_hora, id_usuario, id_canal) VALUES ("Hola a todos! Acabo de publicar una obra, y quiero compartir algunos detalles", NOW(), 4, 2);
INSERT INTO chat_master.mensajes(mensaje, fecha_hora, id_usuario, id_canal) VALUES ("Hola, podés contar de que se trata?", NOW(), 1, 2);
INSERT INTO chat_master.mensajes(mensaje, fecha_hora, id_usuario, id_canal) VALUES ("De qué género se trata tu obra?", NOW(), 2, 2);