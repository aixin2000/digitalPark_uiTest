# -*- coding: utf-8 -*-
import pytest
import os
from config.conf import *


if __name__ == '__main__':
    pytest.main([f'--alluredir={RESULT_DIR}'])
    os.system(f'allure generate {RESULT_DIR} -o '
              f'{REPORT_DIR} --clean')
    # test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\InterfaceTest\\report\\index.html'
    # email = send_mail()
    # email.send_mail(test_path)  # 发送测试报告