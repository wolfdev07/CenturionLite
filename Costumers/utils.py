import os
import random
import string
from datetime import date
from django.utils import timezone

# Generar token aleatorio
def generate_token(length=11):
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Cambiar nombre de archivo
def save_deeds(instance, filename):
    today = timezone.now().date()
    user = instance.propertie.user.username  # Nombre de usuario asociado al propietario
    token = generate_token()

    # Separar la extensión del nombre del archivo original
    name, ext = os.path.splitext(filename)

    # Formar el nuevo nombre de archivo
    new_filename = f"{today}-{user}-{token}{ext}"
    return os.path.join('media', 'documents', 'deeds', new_filename)


def save_id_document(instance, filename):
    today = timezone.now().date()
    user = instance.lessor.user.username
    token = generate_token()

    name, ext = os.path.splitext(filename)

    new_filename = f"{today}-{user}-{token}{ext}"

    return os.path.join('media', 'documents', 'id', new_filename)


def save_acount_lessor(instance, filename):
    today = timezone.now().date()
    user = instance.lessor.user.username
    token = generate_token()

    name, ext = os.path.splitext(filename)

    new_filename = f"{today}-{user}-{token}{ext}"

    return os.path.join('media', 'documents', 'bank_data_lessor', new_filename)


def save_proof_address(instance, filename):
    today = timezone.now().date()
    user = instance.lessor.user.username
    token = generate_token()

    name, ext = os.path.splitext(filename)

    new_filename = f"{today}-{user}-{token}{ext}"

    return os.path.join('media', 'documents', 'proof_address', new_filename)