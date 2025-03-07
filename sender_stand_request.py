import configuration
import data
import requests

# Función para enviar una solicitud POST y crear un usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.header)  # inserta los encabezados

user_response = post_new_user(data.user_body) # guardar la respuesta de la función
print(user_response.status_code)

# Función para crear un kit de un usuario determinado
def post_new_client_kit(kit_body, auth_token):
    headers = data.header.copy()  # copia el header de data
    headers ["Authorization"] = f"Bearer {auth_token}"  # Agrega el auth_token dinámico a la nueva copia de header

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # inserta la dirección URL completa
                         json= kit_body,  # inserta el cuerpo de solicitud
                         headers=headers)  # inserta los encabezados)


