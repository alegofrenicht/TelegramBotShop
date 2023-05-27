from app.bot import bot, emoji
from app.text_templates import help_text


@bot.message_handler(commands=['help'])
def help_func(message):
    bot.send_message(message.chat.id, f'{emoji}{help_text}')
