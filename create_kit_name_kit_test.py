import data
import sender_stand_request
from sender_stand_request import user_response

#Obtener el token del usuario creado
def get_new_user_token():
    if user_response.status_code == 201:
        auth_token = user_response.json().get("authToken")  # Obtener el token
        print(f"Usuario creado con el token: {auth_token}")
        return auth_token
    else:
        print("Error al crear usuario:", user_response.text)
        return None # Se devuelve None si hay un error


# Crear el kit con el token del usuario
def create_kit_with_new_user_token():
    auth_token = get_new_user_token() #obtener el token antes de crear el kit
    kit_response = None #Inicialización de la variable previo a su uso

    if auth_token: #Verificación del token antes de continuar
        kit_response = sender_stand_request.post_new_client_kit(data.kit_body, auth_token) #creación del kit
        print("Kit creado con exito:", kit_response.json()) # Imprimir la respuesta del servidor
    else:
        print("No se pudo crear el kit porque no se obtuvo un token valido")

    return kit_response