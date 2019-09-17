FROM python:3.7.4

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "--no-install-recommends", "apt-utils"]
RUN ["apt-get", "install", "-y", "gettext"]
RUN ["mkdir", "/app"]
RUN ["mkdir", "/app/sample_dynamodb"]

WORKDIR /app
COPY sample_dynamodb /app/sample_dynamodb
COPY requirements.txt /app/
COPY manage.py /app/

RUN pip install -r requirements.txt


EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
