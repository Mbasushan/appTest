#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver
from appium import webdriver
import tool.isElement as isElement
import tool.back as back
import testcase.advertisements.advertisement as Ads
import testcase.advertisements.splashAd as splashAd
import tool.swipe as swipe
class SearchAd(unittest.TestCase):

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

    #搜索里的广告
    def test_search_ad(self):
        print('搜索首页广告')
        # 判断是否有闪屏广告
        splashAd.SplashAd.test_ad(self)
        # 判断是否有首页广告
        Ads.Ad.test_is_ad(self)
        self.driver.find_element_by_id('toolbar_iv_search').click()
        sleep(5)
        #收起键盘
        self.driver.hide_keyboard()
        #点击首个广告：目前是大咖广告
        self.driver.find_elements_by_id("com.mbalib.android.wiki:id/image")[0].click()
        back.ivBack(self)
        #点击每日一词，有句名言，智库早报
        print('进入每日一词')
        self.driver.find_elements_by_id('com.mbalib.android.wiki:id/ivImge')[0].click()
        back.ivBack(self)
        print('进入有句名言')
        self.driver.find_elements_by_id('com.mbalib.android.wiki:id/ivImge')[1].click()
        back.ivBack(self)
        print('进入智库早报')
        self.driver.find_elements_by_id('com.mbalib.android.wiki:id/ivImge')[2].click()
        back.ivBack(self)
        print("进入搜索广告位")
        self.driver.find_elements_by_id("com.mbalib.android.wiki:id/image")[1].click()
        back.ivBack(self)
        #切换到课堂
        print("切换到课堂搜索页")
        self.driver.find_element_by_name('课堂').click()
        #判断是否有广告
        print("判断课堂搜索页是否有广告")
        IvImageAd=isElement.find_Element(self,'id','IvImageAd')
        if IvImageAd:
            print("存在课堂搜索页广告")
            self.driver.find_element_by_id('IvImageAd').click()
            sleep(5)
            back.ivBack(self)
        else:
            print("不存在课堂搜索页广告")

        #切换到资讯搜索页
        print("切换到资讯搜索页")
        self.driver.find_element_by_name('资讯').click()
        IvImageAd = isElement.find_Element(self, 'id', 'IvImageAd')
        if IvImageAd:
            print("存在资讯搜索页广告")
            self.driver.find_element_by_id('IvImageAd').click()
            sleep(5)
            back.ivBack(self)
        else:
            print("不存在资讯搜索页广告")
        sleep(5)

    def tearDown(self):
        self.driver.quit()