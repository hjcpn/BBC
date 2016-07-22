#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BBS.model import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(10), nullable=False)

    def __init__(self, nickname):
        self.nickname = nickname

    def __repr__(self):
        return '<user:{}>'.format(self.nickname)



