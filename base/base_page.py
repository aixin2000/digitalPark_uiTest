# -*- coding: utf-8 -*-
import time
from selenium.webdriver.support.wait import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    TimeoutException,
    NoAlertPresentException,
)
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 打开浏览器
    def open(self, url):
        self.driver.get(url)

    # 定位元素
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 最大化浏览器
    def max_window(self):
        self.driver.maximize_window()

    # 隐式等待
    def implicitly_wait(self, time=10):
        self.driver.implicitly_wait(time)

    # 显示等待
    def wait_element_to_be_located(self, locator):
        """显示等待某个元素出现，且可见"""
        print('info:waiting "{}" to be located'.format(locator))
        try:
            return WD(self.driver, 5).until(ec.presence_of_element_located(locator))
        except TimeoutException as t:
            print('error: found "{}" timeout！'.format(locator), t)

    # 点击元素
    def click(self, loc):
        self.locator(loc).click()

    # 输入文字
    def input_(self, loc, text):
        self.locator(loc).send_keys(text)

    # 关闭浏览器
    def quit(self):
        self.driver.quit()

    # 获取alert弹窗文本
    def alert_text(self):
        return self.driver.switch_to.alert.text

    # 在alert弹窗点击确认
    def alert_accept(self):
        """
        alert点确认
        """
        self.driver.switch_to.alert.accept()

    # 在alert弹窗点击取消
    def alert_dismiss(self):
        """
        alert点取消
        """
        self.driver.switch_to.alert.dismiss()

    # 返回元素某属性的值
    def get_attribute(self, loc, attribute):
        """
        返回元素某属性的值
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param attribute: 属性名称
        :return: 属性值
        """
        value = self.locator(loc).get_attribute(attribute)
        return value

    # 返回元素的文本
    def get_ele_text(self, loc):
        """
        返回元素的文本
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :return: 元素的文本
        """
        return self.locator(loc).text

    def js(self, script):
        """
        执行JavaScript
        :param script:js语句
        """
        self.driver.execute_script(script)

    def scroll_element(self, locator):
        """
        拖动滚动条至目标元素
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        """
        script = "return arguments[0].scrollIntoView();"
        element = self.locator(locator)
        self.driver.execute_script(script, element)

    def scroll_top(self):
        """
        滚动至顶部
        """
        self.js("window.scrollTo(document.body.scrollHeight,0)")

    def scroll_bottom(self):
        """
        滚动至底部
        """
        self.js("window.scrollTo(0,document.body.scrollHeight)")

    def back(self):
        """
        页面后退
        """
        self.driver.back()

    def forward(self):
        """
        页面向前
        """
        self.driver.forward()

    def enter(self, locator):
        """
        在元素上按回车键
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        self.locator(locator).send_keys(Keys.ENTER)

    def double_click(self, locator):
        """
        双击元素
        :param locator: 定位方法'
        """
        element = self.locator(locator)
        ActionChains(self.driver).double_click(element).perform()

    def move_to_element(self, locator):
        """
        鼠标指向元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        element = self.locator(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def drag_and_drop(self, locator, target_locator):
        """
        拖动一个元素到另一个元素位置
        :param locator: 要拖动元素的定位
        :param target_locator: 目标位置元素的定位
        """
        element = self.locator(locator)
        target_element = self.locator(target_locator)
        ActionChains(self.driver).drag_and_drop(element, target_element).perform()

    def frame_in(self, locator):
        """
        进入frame
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        """
        e = self.locator(locator)
        self.driver.switch_to.frame(e)

    def frame_out(self):
        """
        退出frame返回默认文档
        """
        self.driver.switch_to.default_content()

    def open_new_window_by_locator(self, locator):
        """
        点击元素打开新窗口，并将句柄切换到新窗口
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        """
        self.locator(locator).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close(self):
        """
        关闭当前页
        """
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def sleep(self, sec):
        """
        固定等待
        :param sec:
        :return:
        """
        time.sleep(sec)
