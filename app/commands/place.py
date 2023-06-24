from app import app, db, models
from app.bot import bot, emoji, commands, types
from app.text_templates import place_text, rent_sell


device_type = ''
device_name = ''
device_description = ''
device_price = ''
placement_type = ''


def interrupt_request(message):
    markup = types.InlineKeyboardMarkup()
    yes_button = types.InlineKeyboardButton('Yes', callback_data='yes')
    no_button = types.InlineKeyboardButton('No', callback_data='no')
    markup.add(yes_button, no_button)
    bot.send_message(message.chat.id, f'{emoji}Are you sure you want to stop?', reply_markup=markup)


@bot.message_handler(commands=['place'])
def place(message):
    markup = types.InlineKeyboardMarkup()
    rent_button = types.InlineKeyboardButton("👢 Rent", callback_data="rent")
    sell_button = types.InlineKeyboardButton("💰 Sell", callback_data="sell")
    markup.add(rent_button, sell_button)
    bot.send_message(message.chat.id, f'{emoji}{place_text}', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rent')
def rent(call):
    global placement_type
    placement_type = 'rent'
    question = bot.send_message(call.message.chat.id, f"{emoji}{rent_sell['class_quest']}")
    bot.register_next_step_handler(question, device_class_func)


@bot.callback_query_handler(func=lambda call: call.data == 'sell')
def sell(call):
    global placement_type
    placement_type = 'sell'
    question = bot.send_message(call.message.chat.id, f"{emoji}{rent_sell['class_quest']}")
    bot.register_next_step_handler(question, device_class_func)


def device_class_func(message):
    global device_type
    device_type = message.text.strip().capitalize()
    if message.text in commands:
        interrupt_request(message)
        return
    question = bot.send_message(message.chat.id, f"{emoji}{rent_sell['name_quest']}")
    bot.register_next_step_handler(question, device_name_func)


def device_name_func(message):
    global device_name
    device_name = message.text.strip().upper()
    if message.text in commands:
        interrupt_request(message)
        return
    question = bot.send_message(message.chat.id, f"{emoji}{rent_sell['descript_quest']}")
    bot.register_next_step_handler(question, device_description_func)


@bot.callback_query_handler(func=lambda call: call.data == 'yes')
def yes_reply(call):
    bot.send_message(call.message.chat.id, f"{emoji}You've just stopped the process of placing your device in our"
                                           f" marketplace, partner.\nIs there anything I can assist you with, pardner?")


@bot.callback_query_handler(func=lambda call: call.data == 'no')
def no_reply(call):
    question = bot.send_message(call.message.chat.id, f"{emoji}{rent_sell['name_quest']}")
    bot.register_next_step_handler(question, device_name_func)


def device_description_func(message):
    global device_description
    device_description = message.text.strip().capitalize()
    if message.text in commands:
        interrupt_request(message)
        return
    question = bot.send_message(message.chat.id, f"{emoji}{rent_sell['price_quest'].format(placement_type)}")
    bot.register_next_step_handler(question, device_price_func)


def device_price_func(message):
    global device_price
    device_price = message.text.strip()
    if message.text in commands:
        interrupt_request(message)
        return
    if not device_price.isdigit():
        bot.send_message(message.chat.id, "Are you making fun of me? Come on, partner!")
        question = bot.send_message(message.chat.id, f"{emoji}{rent_sell['price_quest'].format(placement_type)}")
        bot.register_next_step_handler(question, device_price_func)
        return
    user = message.from_user.username
    with app.app_context():
        username = models.TelegramUser.query.filter_by(username=user).first()
        device_db = models.Device.query.filter_by(name=device_name).first()
        if device_db:
            bot.send_message(message.chat.id, f"{emoji}Such device already exists.")
        else:
            db.session.add(models.Device(device_type=device_type,
                                         name=device_name,
                                         description=device_description,
                                         price=int(device_price),
                                         placement_type=placement_type,
                                         owner=username.id
                                         )
                           )
            db.session.commit()
            bot.send_message(
                message.chat.id, f"{emoji}You successfully placed your device for {placement_type}"
            )
        if placement_type == 'rent':
            bot.send_message(
                message.chat.id, f"{emoji}You can find it following /{placement_type}"
            )
        else:
            bot.send_message(
                message.chat.id, f"{emoji}You can find it following /buy"
            )
