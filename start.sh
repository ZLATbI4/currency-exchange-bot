#!/bin/bash

# if container not exists or stopped
if [ ! "$(docker ps -q -f name=curbot)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=curbot)" ]; then
        # cleanup
        docker rm curbot -f
        docker system prune -f
    fi
    # run your container
    docker build -t curbot .
    docker run --restart=unless-stopped -d --name curbot curbot
fi
# if container exists
if [ "$(docker ps -q -f name=curbot)" ]; then
  # cleanup
  docker stop curbot
  docker rm curbot -f
  docker rmi curbot -f
  docker system prune -f
  # run your container
  docker build -t curbot .
  docker run --restart=unless-stopped -d --name curbot curbot
fi