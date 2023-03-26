FROM python:3.10

RUN mkdir -p /usr/src/app/
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-dev

COPY . .


