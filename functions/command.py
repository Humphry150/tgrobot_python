# coding:utf-8

from configs import settings
import telegram


def get_keyboard(command):
    return_list = []
    if command is not None:
        for val in settings.command_second_params[command]:
            if command == '/activity':
                return_list.append([telegram.KeyboardButton(text="{} {}".format('/faq', val))])
            else:
                return_list.append([telegram.KeyboardButton(text="{} {}".format(command, val))])
    return return_list


def get_faq_introduce():
    return_str = "'/faq' 使用方式：\n\n<code>"
    for val in settings.faq_params:
        return_str += "/faq {}\n".format(val)
    return_str += "</code>"
    return return_str


def get_activity():
    return_str = "\n<code>"
    for val in settings.official_activity_params:
        return_str += "/faq {}\n".format(val)
    return_str += "</code>"
    return return_str