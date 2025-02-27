Esta es una API REST básica desarrollada con Django y Django-Rest-Framework, se puede utilizar para hacer pruebas y verificar la implementación de una API REST al inicio de un proyecto, tanto con uso de una clave de autenticación como sin esta, a continuación se muestra como hacer peticiones a la API mediante la herramienta de red **curl** para interactuar con la API desde una terminal:

Nota: Los comandos curl listados a continuación se emplean desde un sistema operativo Linux, sin embargo, se agregará la versión del comando compatible con windows para ser ejecutado desde Windows PowerShell

# Interactuar con una API REST utilizando curl

Este documento proporciona instrucciones sobre cómo interactuar con una API REST utilizando la herramienta curl en la línea de comandos. Cubriremos cómo crear, actualizar y eliminar datos, tanto con autenticación mediante clave API como sin ella.

Requisitos Previos

-     Tener curl instalado en tu sistema.
-     Conocer la URL base de la API (en este caso, http://localhost:8000/).
-     Conocer los endpoints específicos de la API y los datos que espera.
-     Tener la Api-Key en caso de que la API lo requiera.

## Crear Datos en la API

#### Sin Autenticación (Si la API lo Permite)

Algunas APIs permiten la creación de datos sin autenticación. Si este es el caso, puedes usar el siguiente comando:

```
curl -H 'Content-Type: application/json' \
-d '{"id_card": 12345678, "name": "nombre_completo"}' \
-X POST http://localhost:8000/
```

Elementos del comando:

-     -H 'Content-Type: application/json': Indica que los datos enviados están en formato JSON.
-     -d '{"id_card": 12345678, "name": "nombre_completo"}': Contiene los datos que se enviarán a la API.
-     -X POST: Especifica que se está realizando una solicitud POST, utilizada para crear nuevos recursos.
-     http://localhost:8000/: Es la URL del endpoint de la API.

#### Versión windows
```
curl -H "Content-Type: application/json" -d "{\"id_card\": 12345678, \"name\": \"nombre_completo\"}" -X POST http://localhost:8000/
```

#### Con Autenticación (Clave API)

Si la API requiere autenticación, debes incluir la clave API en la solicitud:
```
curl -H 'Content-Type: application/json' \
-H "Authorization: Api-Key #############################" \
-d '{"id_card": 12345678, "name": "nombre_completo"}' \
-X POST http://localhost:8000/
```

- -H "Authorization: Api-Key #############################": Incluye la clave API en la cabecera de autorización.

#### Versión windows

```
curl -H "Content-Type: application/json" -H "Authorization: Api-Key #############################" -d "{\"id_card\": 12345678, \"name\": \"nombre_completo\"}" -X POST http://localhost:8000/
```


## Actualizar Datos

Para actualizar datos existentes, utiliza el método PUT y especifica el ID del recurso que deseas actualizar:

#### Sin Autenticación

```
curl -H 'Content-Type: application/json' \
-d '{"id_card": 12345678, "name": "nombre_completo"}' \
-X PUT http://localhost:8000/1/
```
- -X PUT: Especifica que se está realizando una solicitud PUT, utilizada para actualizar recursos existentes.
- http://localhost:8000/1/: La URL incluye el ID del recurso (1 en este caso).
- Importante: Asegúrate de incluir la barra diagonal (/) al final del endpoint.

#### Versión windows

```
curl -H "Content-Type: application/json" -d "{\"id_card\": 12345678, \"name\": \"nombre_completo\"}" -X PUT http://localhost:8000/1/
```

#### Con Autenticación (Clave API)

```
curl -H 'Content-Type: application/json' \
-H "Authorization: Api-Key #############################" \
-d '{"id_card": 12345678, "name": "nombre_completo"}' \
-X PUT http://localhost:8000/1/
```

#### Versión windows

```
curl -H "Content-Type: application/json" -H "Authorization: Api-Key #############################" -d "{\"id_card\": 12345678, \"name\": \"nombre_completo\"}" -X PUT http://localhost:8000/1/
```

## Eliminar Datos

Para eliminar un recurso, utiliza el método DELETE y especifica el ID del recurso:

#### Sin Autenticación

```
curl -X DELETE http://localhost:8000/1/
```

Nota: Este comando funciona tanto para Linux como para Windows

#### Con Autenticación (Clave API)

```
curl -H "Authorization: Api-Key #############################" \
-X DELETE http://localhost:8000/1/
```

#### Versión windows

```
curl -H "Authorization: Api-Key #############################" -X DELETE http://localhost:8000/1/
```

Adicionalmente cabe mencionar que si utilizas **VScode** como editor de código puedes emplear la extensión llamada **REST CLIENT** para enviar enviar solicitudes HTTP a un endpoint directamente desde VScode.
