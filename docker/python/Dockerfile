FROM python:3.8-alpine

ENV APP_PATH /opt/app

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

WORKDIR $APP_PATH

RUN apk update
RUN apk add --no-cache gcc build-base linux-headers sqlite
RUN rm -rf /var/lib/apk/lists/*

COPY ./requirements.txt $APP_PATH/

RUN pip install --no-cache-dir -r $APP_PATH/requirements.txt

CMD ["uwsgi","--ini","/opt/app/uwsgi.ini"]
