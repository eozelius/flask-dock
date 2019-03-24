FROM ubuntu:latest
FROM python:3.7.2
FROM node:lts-alpine

# Ubuntu dependencies
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# python dependencies
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python --version

# Vue dependencies


EXPOSE 5000

ENV FLASK_ENV development
# ENTRYPOINT ["python"]
# CMD ["app.py"]
CMD ["python", "app.py"]