FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python
RUN pip install -r requirements.txt

COPY . /usr/app
ENTRYPOINT python /usr/app/src/helloWorld.py