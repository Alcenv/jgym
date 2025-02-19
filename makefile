.PHONY: build up down logs shell migrate superuser

# Imagen de Docker
build:
	docker-compose build

# Levantamiento de los contenedores
up:
	docker-compose up -d

# Detenimiento de los contenedores
down:
	docker-compose down

# Logs del contenedor web
logs:
	docker-compose logs -f web

# Entrada a la shell del contenedor web
shell:
	docker-compose exec web sh

# Aplicación migraciones de Django
migrate:
	docker-compose exec web python manage.py migrate

# Creacion de un superusuario de Django
superuser:
	docker-compose exec web python manage.py createsuperuser
