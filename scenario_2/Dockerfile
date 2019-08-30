FROM python:3.7-slim

ENV REFRESH_RATE 5 

COPY ./src /code
WORKDIR /code

ENTRYPOINT echo "*** Container started from image ***" && python -u main.py