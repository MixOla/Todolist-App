FROM python:3.10-slim

ENV PYTHONBUFFERED 1

WORKDIR /app

RUN pip install "poetry==1.1.13"

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi --no-root

COPY todolist/ .

EXPOSE 8000

CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']
