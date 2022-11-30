# -*- coding: utf-8 -*-
# author:aixin
# datetime:2021/2/19 11:21
# software: PyCharm
from log.loggerController import log
from base.base_page import BasePage
from tools.parseConFile import ParseConFile
from element_object.login_data import Login_Date


class Login_Page(BasePage):
    # 元素
    # 配置文件读取元素
    do_conf = ParseConFile()
    # # 网址url
    url = do_conf.read_config()
    test = url['test']
    My_Enterprise_Button = Login_Date['My_Enterprise_Button']
    UserName = Login_Date['UserName']
    PassWord = Login_Date['PassWord']
    LoginBtn = Login_Date['LoginBtn']
    Actual = Login_Date['Actual']

    # 操作流程
    def login(self, username, pwd):
        """登录流程"""
        self.open_url()
        log.info(f'打开{self.test}')
        self.implicitly_wait()
        log.info('隐式等待10秒钟')
        self.click_My_Enterprise_Button()
        log.info(f'点击{self.click_My_Enterprise_Button}按钮')
        self.input_username(username)
        log.info(f'输入账号{username}')
        self.input_password(pwd)
        log.info(f'输入密码{pwd}')
        self.click_loginBtn()
        log.info(f'点击登录按钮{self.LoginBtn}')
        self.click_My_Enterprise_Button()
        log.info(f'点击{self.click_My_Enterprise_Button}按钮')
        self.wait_element_to_be_located(self.Actual)

    def get_message(self):
        """获取断言文本"""
        return self.get_ele_text(self.Actual)

    def open_url(self):
        """打开测试环境网址"""
        return self.open(url=self.test)

    def click_My_Enterprise_Button(self):
        """点击我的企业按钮"""
        return self.click(self.My_Enterprise_Button)

    def input_username(self, username):
        """输入用户名"""
        return self.input_(self.UserName, username)

    def input_password(self, psd):
        """输入密码"""
        return self.input_(self.PassWord, psd)

    def click_loginBtn(self):
        """信息填写完整，点击登录按钮"""
        return self.click(self.LoginBtn)


if __name__ == '__main__':
    a = Login_Page(BasePage)
    # print(a.url)
    # print(a.open_url())
    # print(a.click_password_login_btn())
    print(a.test)
    # print(a.open_url())
    # print(a.url)
