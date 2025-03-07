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

#Función para pruebas positivas
def positive_assert(kit_body):
    auth_token = get_new_user_token() #obtener el token valido

    if not auth_token: #Si auth_token no tiene un valor válido (es None, "" o False),
        print ("no se puede obtener el token, no se puede ejecutar la prueba")
        return #detener la ejecución de la función

    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 201 # valida que el codigo de la solictud sea 201
    response_json = response.json() # convierte la respuesta de la solicitud(JSON) en un diccionario Python

    assert response_json["name"] == kit_body["name"] #valida que el atributo name del diccionario nuevo response_json sea igual al atributo name del diccionario kit_body

    print (f"Prueba exitosa: {kit_body['name']} fue creado correctamente.")

#Función para pruebas negativas
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()  # obtener el token valido

    if not auth_token:  # Si auth_token no tiene un valor válido (es None, "" o False),
        print("no se puede obtener el token, no se puede ejecutar la prueba")
        return  # detener la ejecución de la función

    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 400  # valida que el codigo de la solictud sea 400

    print(f"Prueba negativa exitosa: {kit_body['name']} fue rechazado correctamente con código 400.")

#Pruebas positivas
def test_create_kit_1_letter_in_name():
    positive_assert(kit_body = { "name": "a"})

def test_allow_number_of_characters():
    positive_assert(kit_body = { "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"})

def test_special_characters_allowed():
    kit_body = {"name": "№%@,"}
    positive_assert(kit_body)

def test_blank_spaces_allowed():
    positive_assert(kit_body = { "name": " A Aaa " })

def test_numbers_allowed():
    positive_assert(kit_body = { "name": "123" })

#Pruebas negativas
def test_the_number_of_characters_are_less_than_the_allowed_amount_0():
    negative_assert_code_400(kit_body = { "name": "" })

def test_the_number_of_characters_are_more_than_the_allowed_amount_512():
    negative_assert_code_400(kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"})

def test_the_parameter_is_not_included_in_the_request():
    negative_assert_code_400(kit_body = { })

def test_the_parameter_is_a_number():
    negative_assert_code_400(kit_body = { "name": 123 })