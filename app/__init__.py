from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['DEBUG'] = True
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresql:QTTkWWI6j6uLLWRJmnfrRtKEv8PezBR6@dpg-chp6hiqk728ivvuoeipg-a.oregon-postgres.render.com/bot_database_m3ar'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, bot, routes

if __name__ == "__main__":
    bot.bot.infinity_polling()
