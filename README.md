# full-stack-django-react

You will need 4 CMDs open:
1) Frontend:
   1. Install the needed dependencies with `npm install`
   2. Start the app with `npm start`

2) Backend:
   1. Install the needed dependencies with `pip install -r requirements.txt`
   2. Migrate the database with `python manage.py migrate`
   3. Start the server with `python manage.py runserver`

3) Rabbitmq:
   1. Run `rabbitmq-server` 
 
4) Celery:
   1. Run `celery -A api worker -l info -P eventlet` 
