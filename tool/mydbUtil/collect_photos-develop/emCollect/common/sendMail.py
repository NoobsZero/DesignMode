# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class mailSend:
    mailServer = 'mail.em-data.com.cn:465'
    logLevel = 1

    def __init__(self, user, password, timeout=5):
        self.sender = user
        self.password = password
        self.smtpObj = smtplib.SMTP_SSL()
        self.setSmtpObj(timeout, self.logLevel)
        self.receivers = []
        self.status = False
        pass

    def setSmtpObj(self, timeout, logLevel):
        self.smtpObj.set_debuglevel(logLevel)
        self.smtpObj.timeout = timeout
        self.smtpObj.command_encoding = "utf-8"

    def login(self):
        self.smtpObj.connect(self.mailServer)
        self.smtpObj.login(self.sender, self.password)
        print("[{},{}]".format(self.sender,self.password) )
        self.status = True
        return self

    def setReceivers(self, li=[]):
        if len(li) < 1:
            raise Exception('发送列表不能为空呀 ')
        self.receivers = li[:]

    def sendMail(self, content, subject="", contentType="html"):
        if len(content) == 0:
            raise Exception('发送内容不能为空')

        message = MIMEText(content, contentType, self.smtpObj.command_encoding)
        message['From'] = Header(self.sender, self.smtpObj.command_encoding)
        message['To'] = Header(",".join(self.receivers), self.smtpObj.command_encoding)
        message['Subject'] = Header(subject, self.smtpObj.command_encoding)
        self.smtpObj.sendmail(self.sender, receivers, message.as_string())
        print("邮件发送成功")

    def __del__(self):
        if self.status:
            self.smtpObj.close()


def mailHtmlContent(mapContent):
    items = ""
    for key, value in mapContent.items():
        items += """
        <tr>
        <td>{key}</td>
        <td>{value}</td>
        </tr>
        """.format(key=key, value=value)
    return """<table border="1">{}</table>""".format(items)


def getContent(cityName, version, url):
    mc = {
        "项目": "车检",
        "客户": cityName,
        "版本": version,
        "位置": url,
        "显卡": "1070",
        "其他": "",
        "软件更新内容": "",
        "算法": "请使用最新算法版本进行测试",
    }
    return mailHtmlContent(mc)


if __name__ == '__main__':
    user = 'yuyang1@em-data.com.cn'
    password = "*****"
    cityNames = ["青岛"]
    subject = "城市提测"
    receivers = ['yulichao@em-data.com.cn']
    # receivers = ['lipengfei@em-data.com.cn', 'xuepengbo@em-data.com.cn', 'huahaijun@em-data.com.cn',
    #              'yonghao@em-data.com.cn', 'sunchao@em-data.com.cn']
    url = "http://192.168.20.115:7002/buildpackage/chejian-refactor/Release_5.1.46.tar.gz"
    htmlUrl = '<a href="{}">下载</a>'.format(url)
    content = getContent(",".join(cityNames), version="Release_5.1.46",
                         url=htmlUrl)
    print(content)

    try:
        ms = mailSend(user, password).login()
        ms.setReceivers(receivers)
        ms.sendMail(subject=subject, content=content)
    except Exception as ex:
        print("发送失败")
        print(ex)
