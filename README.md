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

configuration file: [.run/UvicornServer.run.xml](.run/UvicornServer.run.xml)

## Run  via Docker
Some variables
```
DB=fastapi-example-db
NET=fastapi-example
```

Create the network
```
docker network create $NET
```

Run MySQL Container
```
docker run -d \
     --network $NET --network-alias mysql \
     -v $DB:/var/lib/mysql \
     -e MYSQL_ROOT_PASSWORD=secret \
     -e MYSQL_DATABASE=$DB \
     --name $DB \
     mysql:5.7
```


For test connection to MySQL DB
```
docker exec -it <mysql-container-id> mysql -u root -p $DB
```

Build App image
```
sudo docker build -t fastapi-example-app .
```
Or you can just pull an image
```shell
docker pull ghcr.io/mtdor/fastapi-api-example:latest
```
note: you should be logged in



Run the App
```
docker run -d --name fastapi-example-app -p 8000:80 \
   --network fastapi-example \
   -e MYSQL_HOST=mysql \
   -e MYSQL_USER=root \
   -e MYSQL_PASSWORD=secret \
   -e MYSQL_DB=fastapi_api_example \
   fastapi-example-app
```
note: for running pulled image its name should be changed to: "ghcr.io/mtdor/fastapi-api-example:latest"


## CI: Docker Build Image
[build-publish-image.yml](./.github/workflows/build-publish-image.yml)

Inspired by: https://fastapi.tiangolo.com/