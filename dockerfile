FROM python:3.8
ENV PYTHONUNBUFFERED 2

RUN mkdir /arcerojas

WORKDIR /arcerojas
COPY . /arcerojas

RUN python -m pip install -r requirements.txt


