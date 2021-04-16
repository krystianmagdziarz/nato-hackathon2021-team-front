FROM python:3.7.7-buster

RUN mkdir -p /home/app
RUN adduser app
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
# copy project
COPY . $APP_HOME
WORKDIR $APP_HOME/hospitalfollowup
# chown all the files to the app user
RUN chown -R app:app $APP_HOME
RUN pip3 install --upgrade pip
RUN pip3 install  -r requirements.txt
USER app