# Usa la imagen base de Debian
FROM python:3-buster

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip3 install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos al contenedor
COPY . .

# Expone el puerto en el que se ejecuta la aplicación Django
EXPOSE 8000

# Comando para ejecutar la aplicación con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]