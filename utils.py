"""Service functions."""

import settings

from emoji import emojize
from random import randint, choice
from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_smile(user_data):
    """Get emoji from emoji-dict."""
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def play_random_number(user_number):
    """Play game guess number."""
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


def main_keyboard():
    return ReplyKeyboardMarkup([
        ['Gemme a cat',
         KeyboardButton('My coordinates', request_location=True)]
    ])
