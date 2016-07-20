default: build

build:
	docker-compose build

run:
	docker-compose stop django  # for restart cases, when already running
	docker-compose up

run-detached:
	docker-compose up -d

restart-django-detached:
	docker-compose stop django
	docker-compose up -d django

stop:
	docker-compose stop

migrate:
	docker-compose exec django ./manage.py migrate

migrations:
	docker-compose exec django ./manage.py makemigrations

apply_migrations: migrations migrate

# execute bash in the currently running container
django_exec_bash:
	docker-compose exec django bash

# run new django container, with bash, and remove it after usage
django_run_bash:
	docker-compose run --rm --no-deps django bash

django_shell:
	docker-compose exec django ./manage.py shell_plus

logs:
	docker-compose logs -f --tail=500

start-pg:
# start existing pg container
	docker-compose up pg_database