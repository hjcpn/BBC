#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
project_dir=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
database_url=os.path.join(project_dir,'bbs.db')
SECRET_KEY = 'development key',
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(database_url)
CELERY_BROKER_URL = 'redis://localhost:6379',
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
SQLALCHEMY_TRACK_MODIFICATIONS = True
