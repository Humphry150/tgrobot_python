# coding:8tf-8

from telegram import Chat
from configs import settings


class ChatHandler(Chat):

    def is_chat_to_manage(self):
        """
        判断会话是否需要被机器人管理
        :return:
        """
        if not self.is_chat_group():
            # 如果不是“聊天组”，则返回False
            return False

        for self.id in settings.bot_config['ChatToManage']:
            # 如果当前会话在配置中
            return True

        return False

    def is_chat_group(self):
        """
        判断该会话是不是属于一个群消息
        :return:如果是普通聊天组，或者超级聊天组，则返回True;否则返回False
        """
        if self.type == self.GROUP or self.type == self.SUPERGROUP:
            return True
        else:
            return False