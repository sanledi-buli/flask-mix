class Const(object):
    def __init__(self):
        pass

    @property
    def app_secret_key(self):
        return self._app_secret_key

    @app_secret_key.setter
    def app_secret_key(self, app_secret_key):
        self._app_secret_key = app_secret_key

    @property
    def res_require_template(self):
        return 'Missing required parameters '

    @res_require_template.setter
    def res_require_template(self, request_value):
        raise AttributeError('Read-only attribute.')

    @property
    def res_exists_template(self):
        return ' already exists'

    @res_exists_template.setter
    def res_exists_template(self, request_value):
        raise AttributeError('Read-only attribute.')

const = Const()
