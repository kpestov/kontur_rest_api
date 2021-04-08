FROM python:3.8

# set work directory
WORKDIR /usr/src/storage

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install dependencies
COPY ./requirements.txt /usr/src/storage/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# copy project
COPY . .
