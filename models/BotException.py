#-*-coding:utf-8 -*-

from configs import settings

class BotException(Exception):
    """电报机器人异常类"""
    def __init__(self):
        pass


class CommandException(BotException):
    """电报机器人命令异常类"""
    def __init__(self):
        # super(BotException).__init__()
        self.message = settings.command['error']


