#!/bin/bash
docker-compose/wait-for-postgres.sh

echo 'creating db'
poetry run python {{cookiecutter.package_name}}/manage.py db_create
echo 'upgrading db'
poetry run python {{cookiecutter.package_name}}/manage.py db upgrade
echo 'starting server'
poetry run gunicorn -w 2 --bind 0.0.0.0:5000 "{{cookiecutter.package_name}}.app:create_app()"
