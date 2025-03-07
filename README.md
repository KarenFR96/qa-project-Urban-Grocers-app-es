# 🛠️ QA Project: Urban Grocers App

Este proyecto tiene como objetivo realizar pruebas de API automatizadas para la aplicación **Urban Grocers**. Se implementan **pruebas funcionales** para la creación de usuarios y kits, asegurando que los requisitos del sistema sean validados correctamente.

---
## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- **`configuration.py`**: Contiene las configuraciones básicas como la URL del servidor y las rutas para crear usuarios y kits.
- **`data.py`**: Define los datos de prueba, como los encabezados de las solicitudes, el cuerpo del usuario y una función para generar el cuerpo del kit.
- **`sender_stand_request.py`**: Contiene funciones para enviar solicitudes HTTP a la API, incluyendo la creación de usuarios y kits.
- **`create_kit_name_kit_test.py`**: Contiene las funciones de prueba para validar la creación de kits, incluyendo pruebas positivas y negativas.
