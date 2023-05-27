import telegram.constants
from app.bot import bot, emoji, types
from app import app, text_templates, models

categories = []


@bot.message_handler(commands=['buy'])
def buy(message):
    global categories
    bot.send_message(message.chat.id, text_templates.sell_text, parse_mode=telegram.constants.ParseMode.HTML)
    with app.app_context():
        devices = models.Device.query.filter_by(placement_type='sell').all()
        [categories.append(device.device_type) for device in devices if device.device_type not in categories]
        if not devices:
            bot.send_message(message.chat.id, f"{emoji}There are no devices yet")
        else:
            categories_markup = types.InlineKeyboardMarkup()
            for category in categories:
                button = types.InlineKeyboardButton(f"{category.capitalize()}", callback_data=f'category for sell:{category.lower()}')
                categories_markup.add(button)
            bot.send_message(message.chat.id, f'{emoji}What sort of device are you looking for?', reply_markup=categories_markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('category for sell:'))
def category_func(call):
    category = call.data.split(':')[1]
    tg_user = call.from_user.username
    with app.app_context():
        db_user = models.TelegramUser.query.filter_by(username=tg_user).first()
        devices = models.Device.query.filter_by(placement_type='sell', device_type=category.capitalize())
        for device in devices:
            if device in db_user.placed_devices:
                user_device_markup = types.InlineKeyboardMarkup()
                button = types.InlineKeyboardButton("It's your device, chill", callback_data='nothing')
                user_device_markup.add(button)
                bot.send_message(call.message.chat.id,
                                 f"{emoji}{text_templates.my_devices_text.format(device.device_type, device.name, device.description, device.price, device.placement_type)}",
                                 parse_mode=telegram.constants.ParseMode.HTML, reply_markup=user_device_markup)
            else:
                other_device_markup = types.InlineKeyboardMarkup()
                rent_button = types.InlineKeyboardButton("Go to owner", callback_data=f'deal:{device.id}')
                other_device_markup.add(rent_button)
                bot.send_message(call.message.chat.id,
                                 f"{emoji}{text_templates.my_devices_text.format(device.device_type, device.name, device.description, device.price, device.placement_type)}",
                                 parse_mode=telegram.constants.ParseMode.HTML, reply_markup=other_device_markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('deal:'))
def deal(call):
    device_id = call.data.split(':')[1]
    device = models.Device.query.filter_by(id=device_id).first()
    owner = models.TelegramUser.query.filter_by(id=device.owner).first()
    bot.send_message(owner.chat_id, f'{emoji}{text_templates.deal_text.format(owner.username, device.name)}')
