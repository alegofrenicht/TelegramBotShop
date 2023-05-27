from app.bot import bot, emoji, types
from app import app, models, text_templates, db
import telegram.constants


@bot.message_handler(commands=['my_devices'])
def my_devices(message):
    tg_user = message.from_user.username
    with app.app_context():
        db_user = models.TelegramUser.query.filter_by(username=tg_user).first()
        if not db_user.placed_devices:
            bot.send_message(message.chat.id, f"{emoji}You don't have any devices placed")
        else:
            for device in db_user.placed_devices:
                markup = types.InlineKeyboardMarkup()
                delete_btn = types.InlineKeyboardButton('Delete', callback_data=f'delete:{device.id}')
                markup.add(delete_btn)
                bot.send_message(message.chat.id, f"{emoji}{text_templates.my_devices_text.format(device.device_type, device.name, device.description, device.price, device.placement_type)}",
                                 parse_mode=telegram.constants.ParseMode.HTML, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('delete:'))
def delete(call):
    device_id = call.data.split(':')[1]
    with app.app_context():
        tg_user = call.from_user.username
        db_user = models.TelegramUser.query.filter_by(username=tg_user).first()
        device_to_del = models.Device.query.filter_by(id=device_id).first()
        db_user.placed_devices.remove(device_to_del)
        db.session.delete(device_to_del)
        db.session.add(db_user)
        db.session.commit()
        bot.send_message(call.message.chat.id, f'{emoji}{device_to_del.device_type}{device_to_del.name} was successfully deleted from list')
