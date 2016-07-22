#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_migrate import MigrateCommand



def create_manager(app):
    manager=Manager(app)
    manager.add_command('db',MigrateCommand)

    return manager
