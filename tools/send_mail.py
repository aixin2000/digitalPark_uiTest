# -*- coding:utf-8 -*-
# author:aixin
# datetime:2021/2/19 14:29
# software: PyCharm
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
from email.utils import parseaddr, formataddr
import time


class Email:
    # ==============定义发送邮件==========
    def send_mail(self, file_new):
        # -----------1.跟发件相关的参数------
        smtpserver = 'smtp.qq.com'  # 发件服务器
        sender = '1454622738@qq.com'  # 发件人邮箱
        username_AuthCode = 'kehpcvdjpxilffaj'  # 邮箱发件授权码
        receiver = ['1454622738@qq.com']  # 收件人邮箱
        # receiver = ['809950119@qq.com', '1454622738@qq.com', '445180207@qq.com']  # 收件人邮箱

        # ----------2.编辑邮件的内容------
        # 读文件
        f = open(file_new, 'rb')
        mail_body = f.read()
        f.close()
        # 邮件正文是MIMEText
        body = MIMEText(mail_body, 'html', 'utf-8')
        # 邮件对象
        msg = MIMEMultipart()
        msg['Subject'] = Header("自动化测试报告", 'utf-8').encode()  # 主题
        msg['From'] = Header(u'测试机 <%s>' % sender)  # 发件人
        # msg['To'] = Header(u'测试负责人 <%s>' % receiver)  # 收件人
        msg['To'] = ','.join(receiver)
        msg.attach(body)
        # 附件
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="test_report.html"'
        msg.attach(att)

        # 发邮件
        smtp = smtplib.SMTP_SSL(smtpserver, port=465)
        smtp.login(sender, username_AuthCode)
        smtp.sendmail(sender, msg['To'].split(','), msg.as_string())
        smtp.quit()
        print("邮件已发出！注意查收。")

    # ======查找测试目录，找到最新生成的测试报告文件======
    def new_report(self, test_report):
        lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
        lists.sort(key=lambda fn: os.path.getmtime(test_report + '/' + fn))  # 按时间排序
        file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
        print(file_new)
        return file_new
