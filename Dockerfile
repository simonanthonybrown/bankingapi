FROM python:3.11

WORKDIR /banking_api

COPY ./requirements.txt ./banking_api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./banking_api/requirements.txt

COPY .app /banking_api/app

RUN python banking_api/app/db_create.py

RUN uvicorn main:app --reload --port 30004