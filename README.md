![Docker Image CI](https://github.com/mtdor/fastapi-api-example/actions/workflows/build-publish-image.yml/badge.svg)


## Objectives!
* CRUD
* Dockerize

## Entry Points!
* http://127.0.0.1:80/docs
* http://127.0.0.1:80/redoc

## Prerequisites!
Python 3.6+
* Uvicorn
* FastAPI
* SQLAlchemy
*Previously was used PyJWT. But it was updated to use Python-jose instead as it provides all the features from PyJWT plus some extras that you might need later when building integrations with other tools.*
* python-jose[cryptography]
*PassLib is a great Python package to handle password hashes.
With passlib, you could even configure it to be able to read passwords created by Django, a Flask security plug-in or many others.*
* passlib[bcrypt]
* SqlLite
```shell
pip install uvicorn[standard] fastapi[all] python-jose[cryptography] passlib[bcrypt] pytest
```

## Run server via Shell

### Create a virtual environment
```bash
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

### Setup ENV variables
Create a file `.env` or just copy and update example `.env.dev_example`
```shell
uvicorn api.main:app --reload
```

## Run server via PyCharm
1) Create virtual environments
2) Add Configurations

![plot](./doc/pycharm_settings.png)

take a look configuration file: [.run/UvicornServer.run.xml](.run/UvicornServer.run.xml)

Versions:
* [docker+mysql](https://github.com/mtdor/fastapi-example/tree/mysql)

Inspired by: https://fastapi.tiangolo.com/