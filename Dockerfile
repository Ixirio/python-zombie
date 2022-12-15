FROM python:3-alpine AS builder

WORKDIR /app

EXPOSE 5000

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD python app.py
