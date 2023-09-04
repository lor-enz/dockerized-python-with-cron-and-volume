FROM python:3.10-slim

# Uncomment to set timezone reliably at build time
#ENV TZ=Europe/Berlin
#RUN apt-get -y install tzdata
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get -y install cron vim
WORKDIR /app
# copy crontab file in the cron directory and sourcecode to /app
COPY crontab /etc/cron.d/crontab
COPY src /app 
# install python dependencies
RUN pip3 install -r /app/requirements.txt
# give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/crontab
# apply cron job
RUN /usr/bin/crontab /etc/cron.d/crontab
# create cron log file (is this necessary? is it even used?)
RUN touch /var/log/cron.log
# create script log file
RUN touch /app/script.log

# run crond as main process of container
CMD ["cron", "-f"]


