opt?=

install:
	python3 -m pip install --user pipenv
	pipenv install

run:
	pipenv run python manage.py runserver

migrations:
	pipenv run python manage.py makemigrations

migrate:
	pipenv run python manage.py migrate


test:
	pipenv run python manage.py test -v2

pytest:
	pipenv run python -m pytest $(opt) .

