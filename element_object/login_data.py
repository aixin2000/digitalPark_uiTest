# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

Login_Date = {
    'My_Enterprise_Button': (By.XPATH, '//*[@id="app"]/div[1]/div[1]/section/div/div/section[2]/section/img'),
    'UserName': (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[3]/div[1]/input'),
    'PassWord': (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[3]/div[2]/input'),
    'LoginBtn': (By.CLASS_NAME, 'login-btn'),
    'Actual': (By.CLASS_NAME, 'company-span')
}

if __name__ == '__main__':
    print(Login_Date['denglu'])
    print(Login_Date['actual'])
