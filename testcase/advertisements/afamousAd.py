#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver
from appium import webdriver
import tool.isElement as isElement
import tool.back as back
import tool.swipe as swipe
import testcase.advertisements.advertisement as Ads
import testcase.advertisements.splashAd as splashAd

class AfamousAd(unittest.TestCase):

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

    #有句名言广告位
    def test_afamous_ad(self):
        print("有句名言广告")
        # 判断是否有闪屏广告
        splashAd.SplashAd.test_ad(self)
        # 判断是否有首页广告
        Ads.Ad.test_is_ad(self)
        print("进入有句名言")
        self.driver.find_element_by_name('有句名言').click()
        sleep(5)
        # 判断是否有广告位
        # 先判断每日一词是否是有图
        clImage = isElement.find_Element(self, 'id', 'ivAdImage')
        if clImage:
            print("有句名言有广告")
            self.driver.find_element_by_id('ivAdImage').click()
            sleep(5)
            back.ivBack(self)
        else:
            print("有句名言无广告")

    # 每日一词广告
    def test_dailyword_ad(self):
        print("每日一词广告")
        # 判断是否有闪屏广告
        splashAd.SplashAd.test_ad(self)
        # 判断是否有首页广告
        Ads.Ad.test_is_ad(self)
        print("进入每日一词")
        self.driver.find_element_by_name('每日一词').click()
        sleep(5)
        # 判断是否有广告位
        # 先判断每日一词是否是有图
        clImage = isElement.find_Element(self, 'id', 'ivAdImage')
        print("每日一词有广告", clImage)
        if clImage:
            print("每日一词有广告")
            self.driver.find_element_by_id('ivAdImage').click()
            sleep(5)
            back.ivBack(self)
        else:
            print("每日一词无广告")

    def tearDown(self):
        self.driver.quit()