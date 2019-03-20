#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver
from appium import webdriver
import tool.isElement as isElement
import tool.back as back
import testcase.advertisements.advertisement as Ads

class SplashAd(unittest.TestCase):

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

    # 闪屏广告点击跳转
    def test_splash_tv_skip(self):
        # 判断是否有闪屏广告
        print('判断是否有闪屏广告')
        driver = self.driver
        splash = isElement.find_Element(self, 'id', 'splash_iv_image')
        if splash:
            print('有闪屏广告点击【跳过】')
            driver.find_element_by_id('splash_tv_skip').click()
            Ads.Ad.test_is_ad(self)
        else:
            print('test_splash_tv_skip无闪屏广告')

    # 不点击跳过闪屏广告，倒计时结束
    def test_noSkip(self):
        print('不点击跳过闪屏广告，倒计时结束')
        # 判断是否有闪屏广告
        driver = self.driver
        splash = isElement.find_Element(self, 'id', 'splash_iv_image')
        # 不点击闪屏广告或者跳过按钮，倒计时结束跳转到首页
        if splash:
            print('有闪屏广告不做操作等倒计时')
            sleep(10)
            # 判断是否有首页广告
            Ads.Ad.test_is_ad(self)
        else:
            print('test_noSkip无闪屏广告')

    # 点击闪屏广告
    def test_ad(self):
        # 判断是否有更新弹窗
        splash = isElement.find_Element(self, 'id', 'splash_iv_image')
        if splash:
            print('点击闪屏广告')
            self.driver.find_element_by_id('splash_iv_image').click()
            sleep(5)
            # 返回
            back.ivBack(self)
            # 执行操作：判断是否有闪屏广告
            Ads.Ad.test_is_ad(self)
        else:
            print('test_ad无闪屏广告')

    def tearDown(self):
        self.driver.quit()