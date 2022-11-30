# -*- coding: utf-8 -*-
import pytest
from base_object.login_page import Login_Page
from element_object.login_data import Login_Date


@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page = Login_Page(driver)
    # home_page = HomePage(driver)
    # contact_page = ContactPage(driver)
    # send_mail_page = SendMailPage(driver)
    yield driver, login_page


@pytest.fixture(scope='function')
def open_url(ini_pages):
    driver = ini_pages[0]
    login_page = ini_pages[1]
    # login_page.open_url()
    yield login_page
    driver.delete_all_cookies()


if __name__ == '__main__':
    open_url()
