import os

def agency_brand_path(instance, filename):
    # Obtener la extensión del archivo
    ext = filename.split('.')[-1]
    # Construir el nombre del archivo: name_membership.ext
    filename = f"{instance.name}_{instance.membership}.{ext}"
    # Devolver la ruta completa para almacenar el archivo
    return os.path.join('static', 'brands', filename)