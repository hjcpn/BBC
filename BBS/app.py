from flask import Flask
from BBS.setting import config
from BBS.__about__ import appname
from BBS.api import api
from BBS.model.tables import db
from flask_migrate import Migrate


class Application(Flask):
    def __init__(self, *arg, **kwargs):
        super(Application, self).__init__(appname, *arg, **kwargs)
        self.config.from_object(config)

    def add_api(self):
        api.init_app(self)

    def add_sqlalchemy(self):
        db.init_app(self)
        migrate = Migrate()
        migrate.init_app(self, db)


def create_app():
    app = Application()
    app.add_api()
    app.add_sqlalchemy()
    return app
