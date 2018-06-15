#-*-coding:utf-8 -*-


command_format_requirements = "1.所有命令不区分大小写\n2.所有命令一览：\n"
command_introduction = "\n<code>/dividends\t今日鼓励金\n/activity\t官方活动\n/yun\tYUN玩法规则介绍\n/officialstaffs\t官方人员\n/faq\t常见问题\n/help\t命令帮助\n</code>"
faq_params = ("平台上线时间", "鼓励金规则", "充币", "提币", "法币交易")
official_activity_params = ("火力全開", "邀請好友")


command = {
    'error': "您输入的命令有误\n{}{}".format(command_format_requirements,command_introduction),
    "/faq": {
        "平台上线时间" : "我们非常荣幸的宣布：YunEx交易平台将于2018年6月5日14:00（UTC/GMT+ 8）正式上线运营。感谢您这些日子的支持与帮助，我们将竭尽全力为您提供一个安全、稳定、有趣的区块链资产交易平台。\n\nUSDT、BTC、ETH、SNET充值通道将于2018年6月5号 14：00（UTC+8）开放。\n\n6月6号将上线BTC/USDT、ETH/USDT、SNET/USDT、ETH/BTC、SNET/BTC交易对。\n\nYunEx正式上线公告链接：\nhttps://support.yunex.io/hc/zh-tw/articles/360003862492-YunEx%E4%BA%A4%E6%98%93%E5%B9%B3%E5%8F%B0%E6%AD%A3%E5%BC%8F%E4%B8%8A%E7%B7%9A%E5%85%AC%E5%91%8A\n开放充值通道公告链接：\nhttps://support.yunex.io/hc/zh-tw/articles/360004500071-YunEx%E4%B8%8A%E7%B7%9ABTC-ETH-SNET",
        "鼓励金规则" : "1.YunEx平台根据用户YUN持有量占比，将平台每天的手续费收入的100%作为鼓励金以USDT/BTC的形式分配给YUN持有者。\n计算公式如下：\n鼓励金奖励=平台交易手续费收入*【YUN持有数量/存放在平台的YUN总数】\n2.平台每天会对用户交易进行统计，统计周期为当日0:00:00-23:59:59；平台按照统计数据，于次日将赠送YUN按相应比例发放到用户的个人账户。（如果遇到区块拥堵、交易量增大或者节假日等情况，鼓励金发放时间都会适当延后）\n3.YUN快照时间为每日23:59:59。\n4.以上所有时间均为东八区时间。",
        "充币" : "【登录】后进入【个人中心】的【资产明细】，选择您想要充值的币种，点击【充币】，点击【复制】获取您的充币地址，再到您的钱包里粘贴到地址栏。",
        "提币" : "【登录】后进入【个人中心】的【资产明细】，选择您想要提币的币种，点击【提币】，把您的钱包地址粘贴到提币地址栏，点击提币。（温馨提示：为了安全起见，实名认证之后才可使用提币功能）",
        "法币交易" : "我们YunEx目前不支持法币充值哦。如果亲想要用人民币等法币充值的话，您可以访问支持法币交易的网站，网站支持中文，具体请您查看以下链接：https://www.coincola.com/",
        "火力全開" : "火力全開 交易就送！\n為慶祝YunEx正式上線，凡在YunEx官網參與幣幣交易的用戶均有機會獲得YUN獎勵。\n时间：2018.06.06 14:00 - 2018.06.21 14:00（UTC/GMT+ 8）\n活动公告链接：https://support.yunex.io/hc/zh-tw/articles/360004277431-%E7%81%AB%E5%8A%9B%E5%85%A8%E9%96%8B-%E4%BA%A4%E6%98%93%E5%B0%B1%E9%80%81-",
        "邀請好友" : "邀請好友 壕送30萬YUN！\n活動期間內，壹旦您邀請的壹級好友和二級好友產生真實交易，即可獲得平臺的YUN贈送，平臺每天會對用戶交易進行統計，統計周期為當日0:00:00-23:59:59。\n时间: 2018.06.06 14:00 - 2018.07.06 14:00（UTC/GMT+ 8）\n活动公告链接：https://support.yunex.io/hc/zh-tw/articles/360004449892-%E9%82%80%E8%AB%8B%E5%A5%BD%E5%8F%8B-%E5%A3%95%E9%80%8130%E8%90%ACYUN-",
    },
    '/dividends' : "1、6月7号每100YUN可获得鼓励金： 17.974065 USDT，0. 000919 BTC，合计约25 USDT。\n2、累计每100YUN已获得鼓励金：51.317625 USDT，0.002561 BTC，合计约70.7 USDT",
    "/help" : "{}{}".format(command_format_requirements,command_introduction),
    "/officialstaffs":"谨防诈骗,YunEx只有以下官方人员 ：\nYunEx 北极星\nYunEx 启明星\nYunEX 木星\nYunEx 水星\nYunEx 天王星",
    "/activity" : "",
    "/yun" : "在YunEx平台持有YUN可获得平台每日100%收益鼓励金,细则参考链接:https://support.yunex.io/hc/zh-tw/articles/360003548292-YUN%E7%99%BC%E8%A1%8C%E5%85%AC%E5%91%8A",
}

command_second_params = {
    "/faq": faq_params,
    "/activity": official_activity_params,
}

welcome = "嗨！~嗨！~欢迎<b>{}</b>加入YunEx大家庭\n平台手续费100%用于平台币YUN持有者鼓励金，平台上线至今一个YUN已累计鼓励金8.25元。赶快一起加入吧！\n\n有什么问题可以发送命令给我们云小朵哦\n/faq\t常见问题\n/help\t命令帮助\n/officialstaffs\t官方人员\n/dividends\t今日鼓励金\n/yun\tYUN玩法规则介绍\n/activity\t官方活动"
