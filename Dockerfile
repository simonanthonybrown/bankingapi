FROM python:3.11

WORKDIR /banking_api

COPY ./requirements.txt ./banking_api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./banking_api/requirements.txt

