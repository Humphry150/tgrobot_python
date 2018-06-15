# -*- coding: utf-8 -*-

import logging
from configs import settings

bind = '%s:%s' % (settings.host, settings.port)
workers = 10
worker_connections = 1000
worker_class = 'gevent'
backlog = 2048
timeout = 1000
debug = False
log_level = logging.ERROR
daemon = False
pidfile = '/tmp/gunicorn_tg_robot_%s.pid' % bind
