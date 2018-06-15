# -*- coding:utf-8 -*-

import os
from flask import Flask
from configs import settings
from views.gbot import botviews


static_folder_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
app = Flask(__name__, static_folder=static_folder_root)
app.register_blueprint(botviews)


if __name__ == '__main__':
    app.run(debug=settings.debug, port=settings.port, host=settings.host)
