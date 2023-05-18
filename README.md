# controlled_vocab_example

small example of an idea for a django vocab microservice. This currently runs with django and sqlite with a single model to repersent a single vocabulary category, but more can be added.

The Django Admin dashboard provides a nice interface for admins to create, search, update, and delete vocabulary words.

for the API we could have anything with `/controlled-vocabulary` go to the django microservice

for production, I would recommend [PostgreSQL](https://www.postgresql.org/)


## Steps to run
1. `git clone`
2. `python -m venv .\venv`
3. activate venv
4. pip install django
5. the sqlite db already exists and if you want to use it 
    1. You can also use your own db by configuring the settings.py
    2. You can also delete the sqlite db and run `makemigrations` and `migrate`
7. `python manage.py runserver` 
