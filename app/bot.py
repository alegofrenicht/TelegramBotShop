import os
from telebot import TeleBot, types
from app import app
from flask import request

token = os.getenv('TOKEN')
bot = TeleBot(token)
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


@app.route('/' + token, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "POST", 200


@app.route('/')
def web_hook():
    bot.remove_webhook()
    bot.set_webhook(url='https://final-project-6cbi.onrender.com/' + token)
    return "CONNECTED", 200


@app.route('/health')
def health():
    return "ok"
