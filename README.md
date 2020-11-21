## Telegram-bot for getting 'fresh' currencies rates

### How it works?
All data parses from https://finance.i.ua
than saves to database. User will get top 10 most popular or from 50 banks with the best price!

### How to run on your environment? 
> requirements : linux os (or mac), installed Docker

Get an API token for your bot, and insert into Dockerfile inside `TELEGRAM_API_TOKEN="here"`

Than run the `start.sh` script as `root` user and enjoy!