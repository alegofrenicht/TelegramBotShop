from app import app
from app.bot import bot
import os


if __name__ == "__main__":
    app.run(host="10.222.25.20", port=int(os.environ.get('PORT', 5000)))


