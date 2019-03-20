#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver
from appium import webdriver
import testcase.vipAduio as vipAduio
import testcase.isVip as isVip

class VipPlay(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['automationName'] = 'Appium'
        desired_caps['autoLaunch'] = 'true'# Appium是否要自动启动或安装app，默认true
        desired_caps['platformName'] = 'Android'
        # desired_caps['version']='8.0.0'
        desired_caps['version'] = '6.0'
        #desired_caps['deviceName'] = 'DIG-TL10'  # 这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['deviceName']='STF-AL00'#这是测试机的型号，可以查看手机的关于本机选项获得
        # desired_caps['app'] = PATH('D:\pythonScript\app-debug.apk')#被测试的App在电脑上的位置
        desired_caps['appPackage'] = 'com.mbalib.android.wiki'
        desired_caps['appActivity'] = 'com.mbalib.android.modules.main.app.controller.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(5)

    #大咖讲百科
    def test_vipPlay(self):
        vipAduio.Vip.test_vip_homePage(self)

    #播放页
    def test_play(self):
        print("大咖音频播放页")
        #判断是否是vip
        #isvip=isVip.isVip(self)
        #if isVip:

        #else:
           #self.driver.find_element_by_id('llNote').is_displayed()

    def tearDown(self):
        self.driver.quit()