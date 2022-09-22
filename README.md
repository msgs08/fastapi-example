### The simplest example of using FastAPI framework

![Docker Image CI](https://github.com/mtdor/fastapi-items-example/actions/workflows/build-publish-image.yml/badge.svg)


### Objectives
* CRUD
* Dockerize

### Requirements:
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
```shell
uvicorn api.main:app --reload
```
### Create a virtual environment
```bash
python -m venv env
source ./env/bin/activate
```

### Setup env variables
create a file `.env` similar to `.env.example` via command
```bash
cp .env.dev_example .env
```
then update the file `.env`

## Run server via Docker
```shell
# build image
sudo docker build -t fastapi-items-example .

# run container
sudo docker run -d --name fastapi-items-example -p 80:80 fastapi-items-example
```

## Run server via PyCharm
1) Create virtual environments
2) Add Configurations

![plot](./doc/pycharm_settings.png)

configuration file: [.run/UvicornServer.run.xml](.run/UvicornServer.run.xml)

## CI: Docker Build Image
[build-publish-image.yml](./.github/workflows/build-publish-image.yml)

### Pull Image
```shell
docker pull ghcr.io/mtdor/fastapi-items-example:latest
```



Inspired by: https://fastapi.tiangolo.com/