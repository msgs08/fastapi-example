FROM python:3.8

# create new dir and use it as workdir
WORKDIR /code

# As this file doesn't change often, Docker will detect it and use the cache for this step
COPY ./.env /code/.env
COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

# put this near the end, to optimize the container image build times
COPY ./api /code/api

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]

