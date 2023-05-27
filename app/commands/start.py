from app import app, models, db, text_templates
from app.bot import bot, emoji


@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.username
    chat_id = message.chat.id
    with app.app_context():
        username = models.TelegramUser.query.filter_by(username=user).first()
        if username:
            pass
        else:
            db.session.add(models.TelegramUser(username=user, chat_id=chat_id))
            db.session.commit()
    bot.send_message(message.chat.id, f'{emoji}Hello, {user.upper()}! Welcome to my land, how can I help you?')
    bot.send_message(message.chat.id, f'{emoji}{text_templates.help_text}')
