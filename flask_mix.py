from flask import Flask

application = Flask(__name__)
application.config.from_object(__name__)

# for csrf
application.secret_key = 'q\xab}\xfb\xcc\xd7B\xb3\x8a\xbe\xe4\xed\xb0\xb0\xcd2\x87=1\xc8\xd6b.r'

# import configuration files
from config import config_db
application.config['SQLALCHEMY_DATABASE_URI'] =\
'postgresql://'+config_db['db_username']+':'+config_db['db_password']+'@'+config_db['db_host']+':'+config_db['db_port']+'/'+config_db['db_name']
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app.models import db
db.init_app(application)

from flask_migrate import Migrate
migrate = Migrate(application,db)

if __name__ == '__main__':
    application.run(port= 7000)
