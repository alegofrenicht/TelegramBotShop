from app import app
from app.bot import bot

webhook_url = 'https://alegofrenicht.github.io/TelegramBotShop/'
bot.set_webhook(url=webhook_url)

if __name__ == "__main__":
    app.run()
