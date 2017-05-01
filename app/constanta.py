class Const:
    def __init__(self):
        pass

    @property
    def app_secret_key(self):
        return self._app_secret_key

    @app_secret_key.setter
    def app_secret_key(self, app_secret_key):
        self._app_secret_key = app_secret_key

const = Const()
