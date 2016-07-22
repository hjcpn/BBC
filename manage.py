#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BBS.commands import create_manager
from BBS.app import create_app

app = create_app()
manager = create_manager(app)

if __name__ == '__main__':
    manager.run()
