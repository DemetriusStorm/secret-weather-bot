"""Simple Telegram bot."""

import logging
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import (
    greet_user,
    guess_number,
    send_cat_picture,
    user_coordinates,
    talk_to_me,
)

# Logging basic config
logging.basicConfig(filename='bot.log', level=logging.INFO)

# Settings for proxy-server
PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD,
    },
}


def main():
    my_bot = Updater(settings.API_KEY, request_kwargs=PROXY)
    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))

    dp.add_handler(
        MessageHandler(Filters.regex('^(Gemme a cat)$'), send_cat_picture))
    dp.add_handler(
        MessageHandler(Filters.location, user_coordinates)
    )
    dp.add_handler(
        MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')

    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()
