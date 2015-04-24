runserver:
	venv/bin/python manage.py runserver 0.0.0.0:8000

pep8:
	pep8 --exclude=*migrations* --max-line-length=119 --show-source  test_app/

pyflakes:
	pylama --skip=*migrations* -l pyflakes test_app/
