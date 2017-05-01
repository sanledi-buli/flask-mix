from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)

    def __init__(self):
        self.created = datetime.now()
        self.updated = self.created
