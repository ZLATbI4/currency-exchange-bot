#!/bin/bash

TOKEN=$(cat .env | grep TELEGRAM_API_TOKEN= | cut -d '=' -f2)

if [[ $TOKEN == "" ]]; then
  echo "Please enter your telegram bot token into '.env' file like that TELEGRAM_API_TOKEN=1795139420:AAFFcdHqc_sW8b_Mb56NpO_sCzk"
else
  echo "USING TOKEN: $TOKEN"
  docker-compose up --build -d
fi
