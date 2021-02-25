# base image
FROM python:3.8.3-alpine

# set a directory for the app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH=/usr/src/app:$PATH

# install dependencies
COPY ./requirements.txt .
RUN \
 apk add --no-cache python3 postgresql-libs libxml2-dev libxslt-dev dos2unix && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 pip install --upgrade pip && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# copy & run entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
RUN dos2unix /entrypoint.sh
RUN chmod +x /entrypoint.sh

# copy project
COPY . .