from flask import Flask

application = Flask(__name__)
application.config.from_object(__name__)

# for csrf
application.secret_key = 'q\xab}\xfb\xcc\xd7B\xb3\x8a\xbe\xe4\xed\xb0\xb0\xcd2\x87=1\xc8\xd6b.r'

if __name__ == '__main__':
    application.run(port= 7000)
