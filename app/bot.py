import os
from telebot import TeleBot, types
from app import app


bot = TeleBot(os.environ.get('TOKEN'))
emoji = '\U0001F335\U0001F335\U0001F335\n\n'
commands = ['/start', '/help', '/place', '/my_devices', '/buy', '/rent']

from app.commands import start, help, place, my_devices, rent, buy


@bot.message_handler(content_types=['text'])
def wrong_input(message):
    user = message.chat.id
    user_message = message.text.lower().strip()
    all_commands = [command.command for command in bot.get_my_commands()]
    if user_message not in all_commands:
        bot.send_message(user, f'{emoji}There is no such command')
    else:
        if user_message == 'start':
            start.start(message)
        elif user_message == 'help':
            help.help_func(message)
        elif user_message == 'place':
            place.place(message)
        elif user_message == 'my_devices':
            my_devices.my_devices(message)
        elif user_message == 'rent':
            rent.rent(message)
        elif user_message == 'buy':
            buy.buy(message)
