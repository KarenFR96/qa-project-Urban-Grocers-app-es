header = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

def get_kit_body(name):
    return {
        "name": name #Devueve un diccionario con la clave "name" y su valor name (variable)
    }

kit_body = get_kit_body("Mi conjunto - kit")


