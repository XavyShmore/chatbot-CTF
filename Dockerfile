FROM python:3.13.0-alpine
RUN apk upgrade
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r /app/requirements.txt
COPY . /app
RUN python db.py

EXPOSE 5000

ENTRYPOINT ["uwsgi", "--socket", "0.0.0.0:5000", "--protocol=http", "-w", "main:app", "-p", "8"]
