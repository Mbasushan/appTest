#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep

from selenium import webdriver
from appium import webdriver
import testcase.advertisements.advertisement as Ads
import tool.swipe as swipe
import testcase.base.isLogin as IsLogin
import tool.isElement as isElement
import testcase.base.login as login
import tool.back as back
import testcase.ketang.isBuyKe as isBuyKe
import tool.connectServer as connectServer

class ApplayKe(unittest.TestCase):

    def setUp(self):
        jsonPath = 'D:/app/testcase/json/setting.json'
        self.driver=connectServer.connect_server(jsonPath)
        sleep(5)

    #进入课程详情页
    def test_noLogin_applyKe(self):
        #判断是否登录
        isLogin=IsLogin.isLogin(self)
        print("未登录点击【报名】")
        Ads.test_ketang_ad(self)
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
        list=self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_package")[0].find_elements_by_class_name("android.widget.LinearLayout")
        list[0].click()
        sleep(5)
        #判断是否进入的是课程详情页
        title=self.driver.find_element_by_id("toolbar_tv_title").text
        if title=="课程详情":
            print("进入课程详情页，是否有报名按钮")
            tvBuy=isElement.find_Element(self,'id','tv_buy')
            if tvBuy:
                print("存在报名按钮")
                self.driver.find_element_by_id("tv_buy").click()
                sleep(5)
                if isLogin:
                    print("用户已登录")
                    #获取当前课程的标题
                    title=self.driver.find_element_by_id('tv_ke_title').text
                    # 选择M币支付
                    self.driver.tap([(425, 818)])
                    #点击【立即支付】
                    self.driver.tap([(452, 934)])
                    back.ivBack(self)
                    isBuyKe.is_buy_ke(self,title)
                    #self.driver.find_element_by_id("pop_btn_pay").click()
                else:
                    print("用户未登录")
                    login_sub = self.driver.find_element_by_xpath("(//android.view.View[@content-desc=\"登录\"])[2]").is_displayed()
                    if login_sub:
                        print("点击报名，跳转到登录页成功")
                        #通过手机号登录
                        #login.login_phone(self)
                        #通过用户名登录
                        login.login_userName(self)
                        title1=self.driver.find_element_by_id("toolbar_tv_title").text
                        if title1 == "课程详情":
                            print("登录成功，返回到课程详情页")
                        else:
                            print("登录成功，返回不是到课程详情页")
                    else:
                        print("未跳转到登录页")
            else:
                print("不存在报名按钮")
                #判断是否登录
                if isLogin:
                    print("用户已登录，判断该课程是否已经购买")
                else:
                    print("不存在报名按钮，又未登录")
        else:
            print("进入的不是课程详情页")



    def tearDown(self):
        self.driver.quit()