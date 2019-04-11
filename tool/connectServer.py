#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
from appium import webdriver
import tool.loadConfigJson as loadConfigJson

#读取与appium建立连接所需的配置文件，解析json，并传入，与appium服务器建立连接，并返回driver对象。
def connect_server(config_path):
    desired_caps = loadConfigJson.load_config_json(config_path)
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver
