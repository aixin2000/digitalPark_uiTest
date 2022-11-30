# -*- coding: utf-8 -*-
import configparser
from config.conf import CONF_PATH


class ParseConFile(object):

    def __init__(self):
        self.file = CONF_PATH
        self.conf = configparser.ConfigParser()
        self.conf.read(self.file, encoding='gb2312')

    def get_all_sections(self):
        """获取所有的section，返回一个列表"""
        return self.conf.sections()

    def get_all_options(self, section):
        """获取指定section下所有的option, 返回列表"""
        return self.conf.options(section)

    def get_locators_or_account(self, section, option):
        """获取指定section, 指定option对应的数据, 返回元祖和字符串"""
        try:
            locator = self.conf.get(section, option)
            if ('->' in locator):
                locator = tuple(locator.split('->'))
            return locator
        except configparser.NoOptionError as e:
            print('error:', e)
        return 'error: No option "{}" in section: "{}"'.format(option, section)

    def get_option_value(self, section):
        """获取指定section下所有的option和对应的数据，返回字典"""
        value = dict(self.conf.items(section))
        return value

    def read_config(self):
        # 获取所有section
        sections = self.conf.sections()
        # ['url', 'email']

        # 获取特定section
        items = self.conf.items('testServer')  # 返回结果为元组
        # [('baidu','http://www.baidu.com'),('port', '80')] 	# 数字也默认读取为字符串

        # 可以通过dict方法转换为字典
        test_url = dict(items)
        return test_url


if __name__ == '__main__':
    b = ParseConFile().get_option_value('LoginPageElements')
    print(b)