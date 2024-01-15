FROM python:3.11

WORKDIR /banking_api

COPY ./requirements.txt ./banking_api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./banking_api/requirements.txt

COPY ./app /banking_api/app

RUN python ./app/db_create.py

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]