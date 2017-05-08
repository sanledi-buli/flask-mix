from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_bcrypt import Bcrypt
import datetime as dt
from constanta import const
import jwt

db = SQLAlchemy()
bcrypt = Bcrypt()

class Validator(object):

    @staticmethod
    def verify_require(request_value):
        if request_value is not None and request_value.strip() != '':
            return True
        return False

    @staticmethod
    def verify_unique(obj, request_value):
        res = db.session.query(func.count(obj).label('count')).filter(obj == request_value)
        if res[0].count == 0:
            return True
        return False

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128))
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)

    def __init__(self,**kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def encode_auth_token(self, user_id):
        try:
            payload = {
                'expiration': str(dt.datetime.now() + dt.timedelta(days=0, seconds=5)),
                'time_created': str(dt.datetime.now()),
                'subject': user_id
            }
            return jwt.encode(
                payload,
                const.app_secret_key,
                algorithm='HS256'
            )
        except Exception as e:
            import pdb; pdb.set_trace()
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, const.app_secret_key)
            return payload['subject']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    @staticmethod
    def create_from_json(json):
        json_respons = {'body': None, 'code': None}
        if json is None or type(json) is not dict:
            json_respons['body'] = const.res_require_template
            json_respons['code'] = 400
            return json_respons

        if not Validator.verify_require(json['name']):
            json_respons['body'] = const.res_require_template + 'name'
            json_respons['code'] = 400
            return json_respons

        if not Validator.verify_require(json['email']):
            json_respons['body'] = const.res_require_template + 'email'
            json_respons['code'] = 400
            return json_respons

        if not Validator.verify_require(json['password']):
            json_respons['body'] = const.res_require_template + 'password'
            json_respons['code'] = 400
            return json_respons

        if not Validator.verify_unique(User.email, json['email']):
            json_respons['body'] = 'Email' + const.res_exists_template
            json_respons['code'] = 400
            return json_respons


        user = User(
            name=json['name'],
            email=json['email'],
            address=json['address'],
            phone_number=json['phone_number'],
            password=json['password'],
            created=dt.datetime.now(),
            updated=dt.datetime.now()
        )
        db.session.add(user)
        try:
            db.session.commit()
            auth_token = user.encode_auth_token(user.id).decode()
        except Exception as ex:
            db.session.rollback()
            raise ex
            return { 'body' : { 'message': 'Internal server error.' }, 'code': 500 }
        return { 'body' : { 'message': 'Successfully registered.', 'access_token': auth_token }, 'code': 201 }

    @staticmethod
    def email_already_exists(email):
        res = db.session.query(func.count(User.id).label('count')).filter(User.email == email)
        if res[0].count != 0:
            return True
        return False
