#!/usr/bin/env python
# -*- coding: utf-8 -*-

SECRET_KEY = 'development key',
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///bbs.db'
CELERY_BROKER_URL = 'redis://localhost:6379',
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
SQLALCHEMY_TRACK_MODIFICATIONS = True
