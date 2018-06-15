# coding:8tf-8


import telegram
import re
from userhandler import UserHandler
from chathandler import ChatHandler
from telegram.bot import Bot as bot
from configs import settings
from models import BotException
from functions.command import *


class MessageHandler(telegram.Message):

    welcome = settings.welcome

    def is_message_must_be_check(self, msg):
        """
        判断聊天组是否需要被管理
        :param msg:
        :return:
        """
        if not ChatHandler().is_chat_to_manage():
            # 非组或者非超级组的会话，不需要检查消息
            return False

        if UserHandler().is_user_in_white_list():
            # 在白名单中的用户，不需要检查消息
            return False

        return True

    def check_message(self):
        """
        检查message
        :return:
        """
        self.check_url()
        self.check_document()
        self.check_photo()
        self.check_audio()
        self.check_video()
        self.check_new_member()

    def check_url(self):
        """
        检查是否有url，如果有，是否满足规则
        :param msg:
        :return:
        """
        allurl = re.finditer(r'((https|http):\/\/)?((\w)*\.){1,2}(com|cn|net|io|pro|top|wang|pub|xin|xyz)', self.text)
        if allurl:
            for match in allurl:
                match_obj = re.match(r'^((https|http):\/\/)?(\w)*\.?yunex.io', "".join(match.group()))
                # 遍历所匹配到的url
                if match_obj is not None:
                    # 如果匹配到的是我们官网的域名，continue
                    continue
                else:
                    # 如果匹配到其他的域名，删除该消息
                    bot.delete_message(self.chat.id, self.message_id)
                    bot.restrict_chat_member(str(self.chat.id), self.from_user.id, int(time.time()) + 7200)
                    return
        else:
            # 未匹配到url，不做任何操作
            pass

    def check_document(self):
        """
        检查是否有document，如果有，是否满足规则
        :param msg:
        :return:
        """
        pass

    def check_photo(self):
        """
        检查是否有photo，如果有，是否满足规则
        :param msg:
        :return:
        """
        pass

    def check_audio(self):
        """
        检查是否有audio，如果有，是否满足规则
        :param msg:
        :return:
        """
        pass

    def check_video(self):
        """
        检查是否有video，如果有，是否满足规则
        :param msg:
        :return:
        """
        pass

    def check_new_member(self):
        """
        检查是否新人入群
        :param msg:
        :return:
        """
        try:
            if self.new_chat_members:
                for curr_member in self.new_chat_members:
                    self.welcome += "{} {}、".format(curr_member.first_name, curr_member.last_name)
                welcome = settings.welcome.format(self.welcome.strip('、'))
                bot.sendMessage(chat_id=self.chat.id,
                                reply_to_message_id=int(self.message_id),
                                text=welcome,
                                parse_mode='HTML')
        except Exception:
            pass

    def check_message(self):
        self.check_new_member()
        self.check_url()

    def handle_message(self):
        """
        消息处理
        :return:
        """
        if self.is_message_must_be_check():
            self.check_message()
        self.handle_command()

    def handle_command(self):
        """
        处理发送过来的命令（“/”开头）
        :return:
        """
        try:
            text = self.text
            if text.find("@") > -1:
                text = text.split("@")[0]
            if text.startswith("/faq"):
                if len(text) == 4:
                    bot.sendMessage(
                        chat_id=self.chat.id,
                        reply_to_message_id=int(self.message_id),
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
                            chat_id=self.chat.id,
                            reply_to_message_id=int(self.message_id),
                            text=settings.command['/faq'][second_command],
                            parse_mode='HTML',
                            reply_markup=telegram.ReplyKeyboardRemove(selective=True))
            elif text == "/activity":
                bot.sendMessage(
                    chat_id=self.chat.id,
                    reply_to_message_id=int(self.message_id),
                    text=get_activity(),
                    parse_mode='HTML',
                    reply_markup=telegram.ReplyKeyboardMarkup(keyboard=get_keyboard(text), selective=True)
                )
            elif text in settings.command.keys():
                bot.sendMessage(
                    chat_id=self.chat.id,
                    reply_to_message_id=int(self.message_id),
                    text=settings.command[text],
                    parse_mode='HTML',
                    reply_markup=telegram.ReplyKeyboardRemove(selective=True))
            else:
                raise BotException.CommandException()
        except BotException.CommandException, ce:
            bot.sendMessage(chat_id=self.chat.id, reply_to_message_id=int(self.message_id), text=ce.message,
                        parse_mode='HTML')
        except Exception:
            pass



