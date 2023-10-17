FROM python:3.10-slim-buster

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev
  # cleaning up unused files
  # && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . /app

CMD pytest -v -s tests/