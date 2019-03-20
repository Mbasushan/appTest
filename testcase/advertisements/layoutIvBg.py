#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver
from appium import webdriver
import tool.isElement as isElement

class LayoutIvBg(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['automationName'] = 'Appium'
        desired_caps['platformName'] = 'Android'
        desired_caps['autoLaunch'] = 'true'  # Appium是否要自动启动或安装app，默认true
        # desired_caps['version']='8.0.0'
        desired_caps['version'] = '6.0'
        desired_caps['deviceName'] = 'DIG-TL10'  # 这是测试机的型号，可以查看手机的关于本机选项获得
        # desired_caps['deviceName']='STF-AL00'#这是测试机的型号，可以查看手机的关于本机选项获得
        # desired_caps['app'] = PATH('D:\pythonScript\app-debug.apk')#被测试的App在电脑上的位置
        desired_caps['appPackage'] = 'com.mbalib.android.wiki'
        desired_caps['appActivity'] = 'com.mbalib.android.modules.main.app.controller.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(5)

    # 判断是否有引导图
    def test_aa_layout_iv_bg(self):
        print("引导图")
        ivBg = isElement.find_Element(self, 'id', 'layout_iv_bg')
        if ivBg:
            print("引导图存在")
            # 左滑
            screen = self.get_size()
            num = 1
            while (num <= 4):
                self.driver.swipe(screen[0] * 0.75, screen[1] * 0.5, screen[0] * 0.05, screen[1] * 0.5, 6000)
                print('第', num, '张引导图')
                num + +1
            self.driver.find_element_by_id('layout_iv_bg').click()
            sleep(5)
        else:
            print("无引导图")

    def tearDown(self):
        self.driver.quit()