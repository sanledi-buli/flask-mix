from flask import Flask

application = Flask(__name__)
application.config.from_object(__name__)

# import configuration files
from config import config_db, config_app
application.config['SQLALCHEMY_DATABASE_URI'] =\
'postgresql://'+config_db['db_username']+':'+config_db['db_password']+'@'+config_db['db_host']+':'+config_db['db_port']+'/'+config_db['db_name']
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# for csrf
application.secret_key = config_app['secret_key']

from app.models import db, bcrypt
db.init_app(application)
bcrypt.init_app(application)

from app.constanta import const
const.app_secret_key = config_app['secret_key']

from flask_migrate import Migrate
migrate = Migrate(application,db)

from app import auth_blueprint
application.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == '__main__':
    application.run(port= 7000, debug=True)
