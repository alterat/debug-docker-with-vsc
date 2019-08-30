FROM python:3.7-slim

ENV REFRESH_RATE 5 

COPY ./main.py /code/main.py
COPY ./requirements.txt /code/requirements.txt
WORKDIR /code

RUN pip install -r requirements.txt

ENTRYPOINT echo "*** Container started from image ***" && python -u main.py