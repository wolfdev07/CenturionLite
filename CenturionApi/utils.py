import secrets
import requests


def create_costumer_membership():
    new_membership = 'C' + secrets.token_hex(3).upper()[:6]

    return new_membership


def send_wa_credentials(data):

    brokername=data['brokername']
    name=data['name']
    user=data['user']
    password=data['password']
    link='https://'
    phone = f"{data['code_country']}1{data['phone']}"
    is_lessor = data['is_lessor']


    if is_lessor:

        message = (
            f"Hola, {name}. Tu asesor inmobiliario {brokername}, te ha "
            f"registrado con éxito, por favor, llena tu información, será importante para el proceso "
            f"de renta de tu propiedad.\n"
            f"usuario: {user}\n"
            f"contraseña: {password}\n"
            f"Ingresa a: {link}"
        )

    else:

        message = (
            f"Hola, {name}. Has recibido este mensaje porque tu asesor inmobiliario {brokername}, "
            f"te ha registrado con éxito, por favor ingresa para completar tu solicitud de arrendamiento.\n"
            f"usuario: {user}\n"
            f"contraseña: {password}\n"
            f"Link: {link}"
        )


    # Preparar el payload en formato JSON
    payload = {
        "message": message,
        "phone": phone
    }

    print(payload)
    url = "http://127.0.0.1:3001/lead"

    response = requests.post(url,  json=payload)

    if response.status_code == 200:
        print(message)
        return True
    else:

        return False