#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import make_celery
from BBS.app import create_app
app=create_app()
celery=make_celery(app)



