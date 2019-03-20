#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver
from appium import webdriver
import tool.isElement as isElement

class Praises(unittest.TestCase):

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


    # 判断是否有好评弹窗
    def test_tvcnacle(self):
        print("是否有好评弹窗")
        tvPraise = isElement.find_Element(self, 'id', 'tvPraise')
        sleep(5)
        if tvPraise:
            print("存在好评弹窗，点击【取消】")
            self.driver.find_element_by_id('tvCnacle').click()
        else:
            print("不存在好评弹窗")

    #点击【暖心好评】
    def test_praise(self):
        print("是否有好评弹窗")
        tvPraise = isElement.find_Element(self, 'id', 'tvPraise')
        sleep(5)
        if tvPraise:
            print("存在好评弹窗，点击【暖心好评】")
            self.driver.find_element_by_id('tvPraise').click()
        else:
            print("不存在好评弹窗")

    # 点击【差评吐槽】
    def test_complaints(self):
        print("是否有好评弹窗")
        tvPraise = isElement.find_Element(self, 'id', 'tvPraise')
        sleep(5)
        if tvPraise:
            print("存在好评弹窗，点击【差评吐槽】")
            self.driver.find_element_by_id('tvComplaints').click()
            sleep(5)
            # 跳转到【意见反馈】页面
            title = self.driver.find_element_by_id('toolbar_tv_title').text
            if title == '意见反馈':
                print("点击【差评吐槽】跳转到【意见反馈】页面成功")
            else:
                print("点击【差评吐槽】跳转到【意见反馈】页面失败")
        else:
            print("不存在好评弹窗")

    def tearDown(self):
        self.driver.quit()