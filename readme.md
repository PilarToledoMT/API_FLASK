<p align="center">
<img src=https://drive.google.com/uc?export=view&id=1DACQJ8zp_qxoB3LBfQnb8A8RUzUIj_QF alt="Banner">
</p>
<h3 align="center">Trabajo Integrador Final - API FLASK</h3>

---

<p align="center"> Como trabajo final de la materia Programación II del Primer Año de la Tecnicatura en Desarrollo de Software, en concordancia con los contenidos desarrollados durante el cursado, recibimos por parte de la cátedra, las consignas y lineamientos para desarrollar una aplicación web, con caracteristicas y funcionalidades similares a la plataforma Discord. 
<br> 
</p>

---

## 📝 Tabla de Contenidos
- [Consigna](#problem_statement)
    - [Objetivo](#our_goals)
    - [Requerimientos Generales](#requirements)
    - [Modelo](#database)
    - [Requerimientos Tecnicos](#tech_req)
- [Instalación/Ejecucion](#getting_started)
- [Tecnologias](#tech_stack)
- [Autor](#authors)

## 🧐 Consigna <a name = "problem_statement"></a>

### Nuestro objetivo 🎯 <a name = "our_goals"></a>
Nuestro objetivo consiste en desarrollar una aplicación web, que consta de una API, definida en el Backend, que será consumida por el Frontend. Dicha aplicación debe permitir registrar usuarios, los cuales podrán crear o
unirse a uno o más servidores. Un servidor es un espacio que puede contener usuarios y a su vez canales. Un canal puede ser creado dentro de un servidor en concreto, y únicamente por un
usuario perteneciente a dicho servidor. Cada canal define el nombre de un único chat, el cual es un registro histórico de los mensajes enviados por los usuarios.

### Requerimientos generales 📖 <a name = "requirements"></a>

El requerimiento general que será transversal a todo el desarrollo del proyecto será la implementación de todas las funcionalidades básicas para poder **crear usuarios, servidores, canales y mensajes, poder listarlos, según la acción requerida y almacenar toda la información en la base de datos**. Dichas funcionalidades son:

- 1. Crear usuarios, para lo cual se solicitará el nombre del usuario, contraseña, y cualquier otro dato que considere necesario. La imagen de perfil sólo podrá elegirse posteriormente a la creación del usuario.
- 2. Iniciar la sesión de un usuario. En caso de que este no exista, deberá indicarse dicho hecho y sugerir que se registre en la aplicación.
- 3. Una vez iniciada una sesión, se deben mostrar tres columnas en la pantalla principal:
    - a. Una primera columna debe mostrar un listado con los servidores a los que el usuario pertenece. Si no pertenece a ningún servidor, entonces mostrará un mensaje indicando esto. Por defecto, ningún servidor estará seleccionado. Sin embargo, al seleccionar uno, se deberá cargar una segunda columna con los canales que posea ese servidor. Además, esta columna debe tener un botón para crear un servidor nuevo.
    - b. La segunda columna debe mostrar un listado de los canales del servidor seleccionado, si no tiene ningún canal creado muestra un mensaje indicándolo. Por defecto , ningún canal estará seleccionado. Sin embargo, al seleccionar uno, se deberá cargar una tercera columna con los mensajes del chat de ese canal. Además, esta columna debe tener un botón para crear un canal nuevo.
    - c. La tercera columna mostrará los mensajes ordenados cronológicamente, con el más reciente en la parte inferior del
chat. Si no hay ningún mensaje en el chat mostrará un mensaje indicando este hecho. Por supuesto, esta columna debe contar con un cuadro de texto para escribir un nuevo mensaje.
- 4. Los mensajes de un chat sólo pueden ser modificados o eliminados por el usuario que los ha creado.
- 5. Debe contar con un componente que permita mostrar el perfil del usuario logueado. En el perfil del usuario se podrán actualizar los datos personales del usuario, incluyendo la imagen del mismo.
- 6. Adicionalmente, la aplicación deberá implementar manejadores de errores personalizados para los siguientes casos:
    - a. 400, Bad Request.
    - b. 404, Not Found.
    - c. 403, Forbidden. Para aquellas peticiones donde no se tenga permisos de acceso o modificación. Por ejemplo, al intentar eliminar un mensaje del chat de otro usuario.
    - d. 500, Server Error.
- 7. La aplicación deberá contar con un buscador de servidores (se buscará por el nombre del servidor). En este componente se mostrarán todos los servidores que coincidan con la búsqueda realizada, para cada resultado se debe mostrar el nombre del servidor, la descripción del servidor (si la tuviera) y la cantidad de usuarios registrados en él (siempre tiene al
menos un usuario registrado, quien lo creó).
- 8. Se deberá administrar la sesión de un usuario, es decir, registramos la información de un usuario inicie una sesión, y el acceso a los endpoints de la API REST diseñada deberá estar restringida sólo a usuarios logueados.
- 9. Documentar el proyecto (archivo README) indicando todo lo que hay que hacer para ponerlo en marcha, además de todas las funcionalidades disponibles.

### Modelo 💾 <a name = "database"></a>
<br>

![modelo](https://drive.google.com/uc?export=view&id=1CPI9vS8Txh8ZjWEI8XypqpZwVqsZVaZ4)

### Requerimientos técnicos ⛏️ <a name = "tech_req"></a>
- Utilización de Entornos Virtuales.
- Bases de datos MySQL gestionada a través de Workbench para almacenar datos.
- Utilización de la extensión CORS, gestión de variables de entorno mediante el módulo Dotenv.
- Framework Flask para el desarrollo de la REST API que pueda consumir la interfaz mediante fetching, haciendo uso del
patrón de diseño MVC.
- Desarrollo de una interfaz de usuarios, implementada con HTML, CSS y Javascript. 
- Utilizar Notion (opcional) como plataforma colaborativa de trabajo en equipo.
- Utilizar GitHub como repositorio del código del proyecto.

## 🏁 Instalación/Ejecución <a name = "getting_started"></a>

Crear entorno virtual

```bash
python -m venv env
```

Activar entorno

```bash
.\env\Scripts\activate
```

Clonar el repositorio API_FLASK

```bash
git clone https://github.com/PilarToledoMT/API_FLASK.git
```

Clonar el repositorio FRONTEND

```bash
git clone https://github.com/PilarToledoMT/FRONTEND.git
```

Instalar dependencias

```bash
pip install -r requirements.txt
```
Iniciar server

```bash
python manage.py runserver
```

## ⛏️ Tecnologias <a name = "tech_stack"></a>

- Python                3.11.4
- blinker                1.6.2
- click                  8.1.6
- colorama               0.4.6
- Flask                  2.3.2
- Flask-Cors             4.0.0
- itsdangerous           2.1.2
- Jinja2                 3.1.2
- MarkupSafe             2.1.3
- mysql-connector-python 8.0.33
- pip                    23.1.2
- protobuf               3.20.3
- python-dotenv          1.0.0
- setuptools             65.5.0
- Werkzeug               2.3.6

## ✍️ Autores <a name = "authors"></a>
- [Pilar Toledo](https://github.com/PilarToledoMT)
- [María Dolores Costa](https://github.com/mariadcb)
- [Rafael López Morales](https://github.com/raffalopez21)
- [Leonardo Franco Villegas Costa](https://github.com/leovillegas94)

<p align="center">
<img src=https://drive.google.com/uc?export=view&id=1XE5HCVdjWq7C4xGh7LROoqFOgFeoOzhl alt="Banner">
</p>
***
