"""
Simple Telegram bot
"""
import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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


# Greet func for /start message
def greet_user(update, context):
    update.message.reply_text('Hello!')
    # Debugger info
    # print(update)


def talk_to_me(update, context):
    user_message = update.message.text
    update.message.reply_text(user_message)


def main():
    my_bot = Updater(settings.API_KEY,
                     request_kwargs=PROXY,
                     )
    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')

    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()
