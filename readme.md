### configure below virtual environment

uvicorn app.main:app
py -3 -m venv venv
venv\scripts\activate
venv\scripts\deactivate

### configure alembic migrations

alembic init alembic

alembic revision -m "create posts table"

alembic current

alembic upgrade c5951cc9a962

alembic revision -m "add content column to posts table"

alembic current

alembic heads

alembic upgrade 40e0011fd47e or alembic upgrade head

alembic downgrade c5951cc9a962

alembic revision -m "add user table" 

alembic current

alembic history

alembic upgrade head

alembic revision -m "add foregin-key to posts table"

alembic upgrade head

alembic revision -m "add last few columns to posts table"

alembic upgrade +1

alembic downgrade c5951cc9a962

alembic revision --autogenerate -m "auto-vote"

alembic revision --autogenerate -m "added phone numbers to users table"




### install below package

pip install fastapi[all]
pip install psycopg2
pip install sqlalchemy
pip install passlib[bcrypt]
pip install python-jose[cryptography]
pip install pydantic-settings
pip install alembic

pip install -r requirements.txt


### go through below documentation to know more

https://fastapi.tiangolo.com/tutorial/

https://www.psycopg.org/docs/

https://docs.pydantic.dev/latest/api/base_model/

https://alembic.sqlalchemy.org/en/latest/api/ddl.html#module-alembic.ddl

### CORS policy

fetch('http://localhost:8000/').then(res => res.json()).then(console.log)


### install git

git init
git add --all
git commit -m "initial commit"
git config --global user.email "helal@gmail.com"
git config --global user.name "M Helal Uddin"
git commit -m "initial commit"
git branch -M main
git remote add origin <url>
git push -u origin main


### install heroku at windows

heroku login

heroku create fastapi-m-helal

git remote

git push heroku main

git add --all

git commit -m "added procfile"

git push heroku main

heroku logs -t


### it will not take any charge
heroku addons:create heroku-postgresql:hobby-dev # hobby-dev is no longer exist

heroku addons:create heroku-postgresql:essential-0

postgresql-flexible-37991

heroku addons:info postgresql-flexible-37991

heroku addons:docs heroku-postgresql

heroku apps --help

heroku ps --help

heroku ps:restart


heroku run "alembic upgrade head"

heroku ps:restart



