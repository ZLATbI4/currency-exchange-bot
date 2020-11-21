#!/bin/bash

docker build -t curbot .
docker run --restart=unless-stopped -d --name curbot curbot
