# -*- coding: utf-8 -*-
import os
import allure
import pytest
from selenium import webdriver
from config.conf import DRIVER_Path

_driver = None


# 测试失败时添加截图和测试用例描述(用例的注释信息)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """钩子函数：获取每个用例的状态"""
    # 获取钩子方法的调用结果
    my_results = yield
    rep = my_results.get_result()
    # 获取用例call，执行结果是失败的，不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step("添加失败截图"):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


@pytest.fixture(scope='module')
def driver():
    global _driver
    print('------------open browser------------')
    _driver = webdriver.Chrome(DRIVER_Path + './chromedriver.exe')
    _driver.maximize_window()
    yield _driver
    print('------------close browser------------')
    _driver.quit()
