from app import app, bot
import os


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv('PORT', 5000))


