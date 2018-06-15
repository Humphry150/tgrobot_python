# coding:8tf-8

from telegram import User


class UserHandler(User):
    def __init__(self):
        super(UserHandler, self).__init__()

    def is_user_in_white_list(self):
        pass