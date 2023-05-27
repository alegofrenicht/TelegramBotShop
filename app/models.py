from app import db


class TelegramUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    chat_id = db.Column(db.Integer, nullable=True)
    placed_devices = db.relationship('Device', backref='user', lazy='select')


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_type = db.Column(db.String(100), index=True)
    name = db.Column(db.String(300), index=True)
    description = db.Column(db.String(600), index=True)
    price = db.Column(db.Integer, nullable=True)
    placement_type = db.Column(db.String(10), index=True)
    owner = db.Column(db.Integer, db.ForeignKey('telegram_user.id'))
