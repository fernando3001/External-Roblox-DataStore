# Conexión de Base de Datos Externa para Juegos de Roblox

Este proyecto consiste en una API desarrollada con Flask que permite conectar una base de datos externa a juegos de Roblox. Utiliza MongoDB como base de datos para almacenar información de los usuarios del juego.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python y pip instalados en tu sistema.
3. Instala las dependencias necesarias.
4. Configura tu conexión a MongoDB en tu archivo modificando la variable `uri` con tu URL de MongoDB.

## Uso

1. Ejecuta la aplicación Flask.
2. La API estará disponible en tu LocalHost.
   
## Endpoints

- `GET /users/?user_id={user_id}`: Obtiene información de un usuario específico.
- `POST /users/`: Crea un nuevo usuario.
- `PUT /users/{user_id}`: Actualiza la información de un usuario existente.

Para más detalles sobre los parámetros y respuestas de cada endpoint, consulta el código fuente en `app.py`.

## Integración con Roblox

Para integrar esta API con tu juego de Roblox, puedes utilizar las funciones de red de Roblox para realizar solicitudes HTTP a los endpoints proporcionados por la API. Puedes utilizar las solicitudes GET, POST y PUT para interactuar con la base de datos y gestionar los datos de los usuarios de tu juego.

## Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, sigue estos pasos:

## Licencia

Este proyecto está bajo la licencia MIT.

## Contacto

Si tienes alguna pregunta o sugerencia sobre este proyecto, no dudes en ponerte en contacto conmigo a través de mi discord: fkooo.
