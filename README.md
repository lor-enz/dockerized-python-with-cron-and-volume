# dockerized-python-with-cron-and-volume


The docker image is set up to recurringly run main.py on a cronjob and which appends a line to a file in the volume.

## Running the docker container

    docker run -d --name dockerized-python-with-cron-and-volume \
     -v /hostmachine/path/config:/config \
     -e TZ=Europe/Berlin \
     dockerized-python-with-cron-and-volume

Or use this for docker compose
```
version: '3'
services:
  dockerized-python-with-cron-and-volume:
    image: dockerized-python-with-cron-and-volume
    container_name: dockerized-python-with-cron-and-volume
    environment:
      - TZ=Europe/Berlin
    volumes:
      - /hostmachine/path/config:/config
    restart: unless-stopped

```
### Docker Volumes

- **/config** is the container path where the output csv file is saved

## Development

### Docker

Navigate to the project directory and build the docker image with 
    
    docker build -t dockerized-python-with-cron-and-volume .

### Run python locally

    python3 src/main.py

