FROM python:3.7.7-buster

RUN mkdir -p /home/app

RUN adduser app

ENV PYTHONDONTWRITEBYTECODE=0
ENV PYTHONUNBUFFERED=0

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# RUN apt-get update
# RUN apt-get install netcat libpq-dev -y

COPY requirements/requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY entrypoint.prod.sh /home/app/web/entrypoint.prod.sh
RUN chmod +x /home/app/web/entrypoint.prod.sh

COPY . $APP_HOME

RUN chown -R app:app $APP_HOME

USER app

ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]
