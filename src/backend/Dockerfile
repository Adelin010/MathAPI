FROM python:3.13.3-slim

WORKDIR /backend

COPY ./app/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

EXPOSE 8000

CMD [ "fastapi", "dev", "main.py" ]