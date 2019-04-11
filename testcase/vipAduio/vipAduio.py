#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver
from appium import webdriver
import testcase.advertisements.advertisement as Ads
import testcase.advertisements.splashAd as splashAd
import tool.isElement as isElement
import tool.back as back
import testcase.base.isVip as Isvip
import tool.swipe as swipe

class Vip(unittest.TestCase):

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

    #从首页的【今日推荐】的【大咖讲百科】进入大咖首页
    def test_vipAduio01(self):
        # 判断是否有闪屏广告
        splashAd.test_ad(self)
        # 判断是否有首页广告
        Ads.test_is_ad(self)
        sleep(5)
        print("从首页的【今日推荐】的【大咖讲百科】进入大咖首页")
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
        self.driver.find_elements_by_id('ivSection')[0].click()
        sleep(5)

    #从首页的【今日推荐】的【专区】进入大咖首页
    def test_vipAduioMore(self):
        # 判断是否有闪屏广告
        splashAd.test_ad(self)
        # 判断是否有首页广告
        Ads.test_is_ad(self)
        sleep(5)
        print("从首页的【今日推荐】的【专区】进入大咖首页")
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
        self.driver.find_elements_by_id('tvMore')[0].click()
        sleep(5)

    #点击首页的【今日推荐】的音频进入大咖播放页
    def test_vipAduioPlay(self):
        # 判断是否有闪屏广告
        splashAd.test_ad(self)
        # 判断是否有首页广告
        Ads.test_is_ad(self)
        sleep(5)
        print("点击首页的【今日推荐】的音频进入大咖播放页")
        #用户是否为VIP用户
        isVip= Isvip.isVip(self)
        back.ivBack(self)
        sleep(5)
        # 点击的是否为试听音频
        aduio = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/wikiAudioRecycler")[0].find_elements_by_class_name("android.widget.RelativeLayout")
        print("audio",aduio)
        try:
            aduioIsVip = aduio[0].find_element_by_id('imageVip').is_displayed()
        except:
            aduioIsVip=False
        if isVip:
            print("点击音频进入大咖播放页")
            aduio[0].find_element_by_id('tv_title').click()
            sleep(5)
        else:
            #用户不是VIP用户则需判断音频是否为试听音频
            if aduioIsVip:
                print("该音频是非试听音频")
                aduio[0].find_element_by_id('tv_title').click()
                sleep(5)
                #触发分享弹窗或者开通VIP弹窗
                tvOpen=isElement.find_Element(self, 'id', 'tvOpen')
                #点击【开通vip】
                if tvOpen:
                    print("有触发弹窗")
                    self.driver.find_element_by_id('tvOpen').click()
                    sleep(5)
                    #进入开通vip页面，判断是否进入的是开通vip页面
                    tvPay=isElement.find_Element(self,'id','tvPay')
                    if tvPay:
                        print("进入开通vip页面")
                    else:
                        print("未进入开通vip页面")
                else:
                    print("无触发弹窗")
            else:
                print("该音频是试听音频")
                aduio[0].find_element_by_id('tv_title').click()
                sleep(5)

    #app首页【大咖讲百科】入口
    def test_vip_homePage(self):
        print("app首页【大咖讲百科】入口")
        # 判断是否有闪屏广告
        splashAd.test_ad(self)
        # 判断是否有首页广告
        Ads.test_is_ad(self)
        print("点击进入大咖讲百科")
        self.driver.find_element_by_id('home_tv_wiki').click()
        sleep(5)


    def tearDown(self):
        self.driver.quit()
