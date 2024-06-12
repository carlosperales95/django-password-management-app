source pass_manage_venv/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver