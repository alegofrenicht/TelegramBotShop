from app import app
from app.bot import bot

webhook_url = 'https://final-project-l7lz.onrender.com/webhook'
bot.set_webhook(url=webhook_url)

if __name__ == "__main__":
    app.run()
