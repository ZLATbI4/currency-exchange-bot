## Telegram-bot for getting 'fresh' currencies rates

### How it works?
All data parses from secret website
then saves to database. User will get message with the best currency rates in Ukrainian banks!

### How to run on your environment? 
> requirements : linux os (or mac), installed Docker

Get an API token for your bot, and insert into Dockerfile inside `TELEGRAM_API_TOKEN="here"`

Than run the `start.sh` script as `root` user and enjoy!

chat command list:  
 * `/start` - info message
 * `/all_usd` - 🇺🇸 USD current rate for all banks  
 * `/all_eur` - 🇪🇺 EUR current rate for all banks  
 * `/all_gbp` - 🇬🇧 GBP current rate for all banks  
 * `/all_pln` - 🇵🇱 PLN current rate for all banks  
 * `/top_usd` - 🇺🇸 USD current rate for TOP 10 banks  
 * `/top_eur` - 🇪🇺 EUR current rate for TOP 10 banks  
 * `/top_gbp` - 🇬🇧 GBP current rate for TOP 10 banks  
 * `/top_pln` - 🇵🇱 PLN current rate for TOP 10 banks  