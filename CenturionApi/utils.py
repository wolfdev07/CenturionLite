import secrets
import requests
import json
import random
from heyoo import WhatsApp
from config.settings import TOKEN_WA


def set_username(first_name, last_name):
    # Combina los nombres aleatoriamente
    nombres = [first_name, last_name]
    random.shuffle(nombres)
    
    # Une los nombres combinados con '@centurion'
    nombre_completo = ''.join(nombres) + '@centurion'
    
    return nombre_completo



def create_costumer_membership():
    new_membership = 'C' + secrets.token_hex(3).upper()[:6]

    return new_membership


def send_message(data):

    brokername=data['brokername']
    name=data['name']
    user=data['user']
    password=data['password']
    link='https://'


    token = TOKEN_WA
    id_number_send = '166555139881376'
    number_receiver = data['phone_complete']
    


    if data['is_lessor']:
        message = (
            f"Hola, {name}. Tu asesor inmobiliario {brokername}, te ha "
            f"registrado con éxito, por favor, llena tu información, será importante para el proceso "
            f"de renta de tu propiedad.\n"
            f"USUARIO: {user}\n"
            f"PASSWORD: {password}\n"
            f"Ingresa a: {link}"
        )
    else:
        message = (
            f"Hola, {name}. Has recibido este mensaje porque tu asesor inmobiliario {brokername}, "
            f"te ha registrado con éxito, por favor ingresa para completar tu solicitud de arrendamiento.\n"
            f"USUARIO: {user}\n"
            f"PASSWORD: {password}\n"
            f"Link: {link}"
        )


    messenger = WhatsApp(token, id_number_send)

    messenger.send_message(message, number_receiver)

    return True




def send_message_api(data):
    brokername = data['brokername']
    name = data['name']
    user = data['user']
    password = data['password']
    link = 'un link'

    id_number_send = '166555139881376'
    number_receiver = data['phone_complete']

    if data['is_lessor']:
        message = (
            f"Hola, {name}. Tu asesor inmobiliario {brokername}, te ha "
            f"registrado con éxito, por favor, llena tu información, será importante para el proceso "
            f"de renta de tu propiedad.\n"
            f"USUARIO: {user}\n"
            f"PASSWORD: {password}\n"
            f"Ingresa a: {link}"
        )
    else:
        message = (
            f"Hola, {name}. Has recibido este mensaje porque tu asesor inmobiliario {brokername}, "
            f"te ha registrado con éxito, por favor ingresa para completar tu solicitud de arrendamiento.\n"
            f"USUARIO: {user}\n"
            f"PASSWORD: {password}\n"
            f"Ingresa a: {link}"
        )

    # Construir el cuerpo del mensaje JSON para enviar
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number_receiver,
        "type": "text",
        "text": { 
        "preview_url": True,
        "body": message
        }
    }

    # Configurar las cabeceras de la solicitud
    headers = {
        'Authorization': f'Bearer {TOKEN_WA}',
        'Content-Type': 'application/json'
    }

    # Enviar la solicitud POST con los datos a la URL de Facebook
    url = f'https://graph.facebook.com/v17.0/{id_number_send}/messages'
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Comprobar el código de estado de la respuesta
    if response.status_code == 200:
        print(f"se envio el pinche mensaje {number_receiver}")
        print(password)
        return True
    else:

        print(f"NOOOO SE ENVIO EL MENSAJE")
        print(f"{response.status_code}")
        return False



def send_message_template(data):
    brokername = data['brokername']
    name = data['name']
    user = data['user']
    password = data['password']
    link = 'https://'

    id_number_send = '166555139881376'
    number_receiver = data['phone_complete']

    if data['is_lessor']:
        message = (
            f"Hola, {name}. Tu asesor inmobiliario {brokername}, te ha "
            f"registrado con éxito, por favor, llena tu información, será importante para el proceso "
            f"de renta de tu propiedad.\n"
            f"USUARIO: {user}\n"
            f"PASSWORD: {password}\n"
            f"Ingresa a: {link}"
        )
    else:
        message = (
            f"Hola, {name}. Has recibido este mensaje porque tu asesor inmobiliario {brokername}, "
            f"te ha registrado con éxito, por favor ingresa para completar tu solicitud de arrendamiento.\n"
            f"USUARIO: {user}\n"
            f"PASSWORD: {password}\n"
            f"Link: {link}"
        )

    # Construir el cuerpo del mensaje JSON para enviar
    payload = {
        "messaging_product": "whatsapp",
        "to": number_receiver,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {
                "code": "en_US"
            }
        }
    }

    # Configurar las cabeceras de la solicitud
    headers = {
        'Authorization': f'Bearer {TOKEN_WA}',
        'Content-Type': 'application/json'
    }

    # Enviar la solicitud POST con los datos a la URL de Facebook
    url = f'https://graph.facebook.com/v17.0/{id_number_send}/messages'
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Comprobar el código de estado de la respuesta
    if response.status_code == 200:
        print(f"se envio el pinche mensaje {number_receiver}")
        print(password)
        print(message)
        return True
    else:

        print(f"NOOOO SE ENVIO EL MENSAJE")
        print(f"{response.status_code}")
        print(password)
        print(message)
        return False