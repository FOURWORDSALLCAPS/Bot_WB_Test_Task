FROM python:3.13.1-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

COPY ../pyproject.toml pyproject.toml

RUN poetry install --only main

COPY app app

EXPOSE 8000/tcp

CMD uvicorn app.main:app \
    --host "0.0.0.0" \
    --port 8000 \
    --workers ${WORKERS} \
    --log-level ${LOG_LEVEL}
