# Imagen oficial de Python
FROM python:3.12

# Definición directorio de trabajo dentro del contenedor
WORKDIR /app

# Archivos del proyecto al contenedor
COPY . /app/

# Dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Puerto 8000
EXPOSE 8000

# Iniciar Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
