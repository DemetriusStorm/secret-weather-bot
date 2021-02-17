# Secret Weather Bot project

Secret weather bot - is a Telegram bot for displaying the weather in your city.

## Install & Run
1. Clone repo from github `git clone https://github.com/DemetriusStorm/secret-weather-bot.git`
2. Create venv
3. Install requirements `pip install -r requirements.txt`
4. Create `settings.py` and insert this code block:
```buildoutcfg
API_KEY = 'API key for your bot'
PROXY_URL = 'proxy URL'
PROXY_USERNAME = 'proxy username'
PROXY_PASSWORD = 'proxy password'
USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']
```
5. Run bot command: `python bot.py`
