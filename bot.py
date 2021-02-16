"""
Simple Telegram bot
"""
import logging
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint, choice
from glob import glob
from emoji import emojize

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


def get_smile():
    smile = choice(settings.USER_EMOJI)
    smile = emojize(smile, use_aliases=True)
    return smile


def greet_user(update, context):
    """
    Greet func for /start message.
    :param update:
    :param context:
    :return:
    """
    update.message.reply_text('Hello! {0}'.format(get_smile()))


def talk_to_me(update, context):
    """

    :param update:
    :param context:
    :return:
    """
    user_message = update.message.text
    update.message.reply_text('{0} {1}'.format(get_smile(), user_message))
    # print(update)


def guess_number(update, context):
    """

    :param update:
    :param context:
    :return:
    """
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_number(user_number)
        except (TypeError, ValueError):
            message = 'Enter an integer!'
    else:
        message = 'Enter a number..'
    update.message.reply_text(message)


def play_random_number(user_number):
    """

    :param user_number:
    :return:
    """
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = 'Your number is {0}, my number is {1}, you win!'.format(
            user_number,
            bot_number,
        )
    elif user_number == bot_number:
        message = 'Your number is {0}, my number is {1}, draw!'.format(
            user_number,
            bot_number,
        )
    else:
        message = 'Your number is {0}, my number is {1}, you lose!'.format(
            user_number,
            bot_number,
        )
    return message


def send_cat_picture(update, context):
    """

    :param update:
    :param context:
    :return:
    """
    cat_images_list = glob('images/cat*.jp*g')
    random_cat_image = choice(cat_images_list)
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(random_cat_image, 'rb'),
    )


def main():
    my_bot = Updater(settings.API_KEY,
                     request_kwargs=PROXY,
                     )
    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')

    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()
