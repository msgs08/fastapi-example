The simplest example of using FastApi framework

Inspired by: https://fastapi.tiangolo.com/

### Targets
* Dockerize

### Dependencies:
* SQLAlchemy

### Database:
* SqlLite

### Create a virtual environment
```bash
python -m venv env
source ./env/bin/activate
```

### Setup env variables
create a file `.env` similar to `.env.example` via command
```bash
cp .env.example .env
```
then update the file `.env`


## Run server via shell
```shell
uvicorn main:app --reload
```


## Run server via Docker
```shell
# build image
sudo docker build -t fastapi-items-example .

# run container
sudo docker run -d --name fastapi-items-example -p 80:80 fastapi-items-example
```
