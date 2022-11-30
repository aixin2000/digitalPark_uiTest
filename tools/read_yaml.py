# -*- coding: utf-8 -*-
import json
import yaml
from config.conf import *
from tools.random_phone import randomPhone


def read_get_yaml(readyaml):
    """
    读取yaml文件
    :return:
    """
    with open(f'{DATA_Path}' + readyaml, 'r', encoding='gbk')as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        # print(data[0]['username'])
        # print(data[0]['request']['data'])
        print(data)
        return data


# 写入
def write_yaml():
    with open(f'{DATA_Path}' + './register_data.yaml', encoding="utf-8", mode="a")as f:
        value = yaml.dump(randomPhone(), stream=f, allow_unicode=True)
        # print(value)


if __name__ == '__main__':
    read_get_yaml()
