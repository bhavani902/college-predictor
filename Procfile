web:gunicorn CCMS.wsgi --log-file -
web: gunicorn hellodjango.wsgi
web:python myApp.py runserver 0.0.0.0:$PORT

gunicorn -b :5000 --access-logfile - --error-logfile - build:app