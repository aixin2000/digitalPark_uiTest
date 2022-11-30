# -*- coding: utf-8 -*-
# author:aixin
# datetime:2021/2/19 11:29
# software: PyCharm
import allure
import pytest
from selenium import webdriver
from element_object.login_data import Login_Date
from tools.read_yaml import read_get_yaml


@allure.epic('登录测试case')
@allure.feature('登录功能')
class Test_Login:
    @allure.story('直客登录接口')
    @allure.severity('blocker')
    @allure.step('循环对比')
    @allure.issue("https://www.tapd.cn/tapd_fe/44308309/bug/list?dialog_preview_id=bug_1144308309001010691",
                  name='点击跳转缺陷地址')
    @allure.testcase("https://www.tapd.cn/44308309/sparrow/tcase/tcase_list?category_id=1144308309001000054&data["
                     "Filter][name]=&dialog_preview_id=tcase_1144308309001000828", name='点击我跳转TAPD')
    @allure.description("这里是对直客登录用例的一些详细说明")
    @pytest.mark.parametrize('test_data', read_get_yaml('.\\login_data.yaml'))
    def test_case01(self, open_url, test_data):
        """
        直客登录
        :param kwargs:
        :return:
        """
        allure.dynamic.title(test_data['name'])
        a = open_url
        a.login(test_data['user'], test_data['pwd'])
        assert a.get_message() == test_data['expected']


if __name__ == "__main__":
    pytest.main(['-v', './test_pylogin.py'])
