import os
import string
import random
import re
from django.contrib.auth.hashers import make_password

def agency_brand_path(instance, filename):
    # Obtener la extensión del archivo
    ext = filename.split('.')[-1]
    # Construir el nombre del archivo: name_membership.ext
    filename = f"{instance.name}_{instance.membership}.{ext}"
    # Devolver la ruta completa para almacenar el archivo
    return os.path.join('brands', filename)



def generate_temp_password(length=8):
    # Caracteres que se utilizarán para generar la contraseña temporal
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generar una contraseña temporal aleatoria
    temp_password = ''.join(random.choice(characters) for _ in range(length))

    hashed_temp_pasword = make_password(temp_password)

    return temp_password, hashed_temp_pasword


def validate_phone_number(phone):
    # Define una expresión regular para validar un número de teléfono sin código de país
    phone_pattern = re.compile(r'^\d{1,15}$')

    # Intenta hacer coincidir el número de teléfono con la expresión regular
    match = phone_pattern.match(phone.replace(' ', ''))  # Quita los espacios si los hubiera

    if match:
        # Devuelve True si el número de teléfono es válido
        return True
    else:
        # Devuelve False
        return False
