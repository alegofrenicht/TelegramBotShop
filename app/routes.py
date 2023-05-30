from app import app
from app.bot import bot
from flask import request
import os

token = os.getenv('TOKEN')


@app.route('/' + token, methods=['POST'])
def get_message():
    bot.process_new_updates([bot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "POST", 200


@app.route('/')
def web_hook():
    bot.remove_webhook()
    bot.set_webhook(url='https://final-project-2qwc.onrender.com/' + token)
    return "CONNECTED", 200


@app.route('/health')
def health():
    return "ok"
