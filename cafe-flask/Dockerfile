FROM ubuntu:latest
FROM python:3.7.2

# Ubuntu dependencies
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# python dependencies
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_ENV "development"
ENV FRONTEND_IP "http://104.156.227.73:8080"
ENTRYPOINT ["python"]
CMD ["app.py"]
