"""Handlers functions."""

from glob import glob
from random import choice
from utils import get_smile, play_random_number, main_keyboard


def greet_user(update, context):
    """Greet func for /start message."""
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text('Hello! {0}'.format(
        context.user_data['emoji']),
        reply_markup=main_keyboard(),
    )


def talk_to_me(update, context):
    """Return echo user message."""
    context.user_data['emoji'] = get_smile(context.user_data)
    user_message = update.message.text
    update.message.reply_text('{0} {1}'.format(
        user_message,
        context.user_data['emoji'],
    ))


def guess_number(update, context):
    """Get user number."""
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_number(user_number)
        except (TypeError, ValueError):
            message = 'Enter an integer!'
    else:
        message = 'Enter a number..'
    update.message.reply_text(message, reply_markup=main_keyboard())


def send_cat_picture(update, context):
    """Choose random image from list."""
    cat_images_list = glob('images/cat*.jp*g')
    random_cat_image = choice(cat_images_list)
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(random_cat_image, 'rb'),
        reply_markup=main_keyboard(),
    )


def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coordinates = update.message.location
    update.message.reply_text('Your coordinates {0} {1}'.format(
        coordinates,
        context.user_data['emoji'],
    ), reply_markup=main_keyboard())
