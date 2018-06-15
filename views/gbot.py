# -*- coding:utf-8 -*-

import time
import telegram
from flask import Flask, request, Blueprint
from configs import settings
from models import BotException
import re

import logging

botviews = Blueprint('bot', __name__, url_prefix='/bot')

bot = telegram.Bot(token=settings.telegram_token)
time.sleep(5)
bot.setWebhook(settings.telegram_webhook)


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




def handdle_message(msg):
    try:
        print msg
        print "==========================="
        print
        print "==========================="

        print bot.get_chat("-1001290687161")
        if msg.text:
            # 发送消息
            text = msg.text.lower().strip()
            if text.startswith("/"):
                # 以“/”开头的消息，是要与机器人交互的消息
                if text.find("@") > -1:
                    text = text.split("@")[0]
                if text.startswith("/faq"):
                    if len(text) == 4:
                        bot.sendMessage(
                            chat_id=msg.chat.id,
                            reply_to_message_id=int(msg.message_id),
                            text=get_faq_introduce(),
                            parse_mode='HTML',
                            reply_markup=telegram.ReplyKeyboardMarkup(keyboard=get_keyboard(text), selective=True))
                    else:
                        tmp = text.split(" ", 1)
                        second_command = tmp[1].encode('utf-8')
                        if second_command not in settings.command['/faq'].keys():
                            raise BotException.CommandException()
                        else:
                            bot.sendMessage(
                                chat_id=msg.chat.id,
                                reply_to_message_id=int(msg.message_id),
                                text=settings.command['/faq'][second_command],
                                parse_mode='HTML',
                                reply_markup=telegram.ReplyKeyboardRemove(selective=True))
                elif text == "/activity":
                    bot.sendMessage(
                        chat_id=msg.chat.id,
                        reply_to_message_id=int(msg.message_id),
                        text=get_activity(),
                        parse_mode='HTML',
                        reply_markup=telegram.ReplyKeyboardMarkup(keyboard=get_keyboard(text), selective=True)
                    )
                elif text in settings.command.keys():
                    bot.sendMessage(
                        chat_id=msg.chat.id,
                        reply_to_message_id=int(msg.message_id),
                        text=settings.command[text],
                        parse_mode='HTML',
                        reply_markup=telegram.ReplyKeyboardRemove(selective=True))
                else:
                    raise BotException.CommandException()
            else:
                # 不是以“/”开头的消息，为正常消息
                allurl = re.finditer(r'((https|http):\/\/)?((\w)*\.){1,2}(com|cn|net|io|pro|top|wang|pub|xin|xyz)', text)
                if allurl:
                    for match in allurl:
                        match_obj = re.match(r'^((https|http):\/\/)?(\w)*\.?yunex.io', "".join(match.group()))
                        # 遍历所匹配到的url
                        if match_obj is not None:
                            # 如果匹配到的是我们官网的域名，continue
                            continue
                        else:
                            # 如果匹配到其他的域名，删除该消息
                            bot.delete_message(msg.chat.id, msg.message_id)
                            bot.restrict_chat_member(str(msg.chat.id), msg.from_user.id, int(time.time())+7200)
                            return
                else:
                    # 未匹配到url，不做任何操作
                    pass
        elif msg.new_chat_members:
            # 添加组内成员
            members = ""
            print msg.new_chat_members
            for curr_member in msg.new_chat_members:
                members += "{} {}、".format(curr_member.first_name, curr_member.last_name)
            welcome = settings.welcome.format(members.strip('、'))
            bot.sendMessage(chat_id=msg.chat.id,
                            reply_to_message_id=int(msg.message_id),
                            text=welcome,
                            parse_mode='HTML')
    except BotException.CommandException, ce:
        bot.sendMessage(chat_id=msg.chat.id, reply_to_message_id=int(msg.message_id), text=ce.message,
                        parse_mode='HTML')
    except Exception:
        pass


@botviews.route("/cmd", methods=["POST", "GET"])
def telegram_bot():
    if request.method == "POST":
        message = request.get_json(force=True)
        update = telegram.Update.de_json(message, bot)
        handdle_message(update.message)
        return "ok"
    return ''


if __name__ == '__main__':
    pass


