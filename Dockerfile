FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8080"]
