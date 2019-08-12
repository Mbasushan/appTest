#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver
from appium import webdriver
import testcase.advertisements.advertisement as AdTest
import testcase.advertisements.splashAd as splashAd
import tool.isElement as isElement
import tool.swipe as swipe
import testcase.base.login as login
import tool.back as back

#是否为大咖vip
def isVip(self):
    print("是否为大咖vip")
    #切换到【我的】
    self.driver.find_element_by_name('我的').click()
    # 判断是否登录
    isLogin = isElement.find_Element(self, 'id', 'tv_my_fragment_login_no_login')
    if isLogin:
        # 登录账号
        self.driver.find_element_by_id('tv_my_fragment_login_no_login').click()
        sleep(5)
        login.login_userName(self)
        flag=self.driver.find_element_by_xpath('//android.view.View[@content-desc="绑定 绑定"]').is_enabled()
        if flag:
            back.ivBack(self)
    else:
        print("有登录")
    # 判断是否为vip
    text = self.driver.find_element_by_id('tv_my_fragment_vip_wiki_date').text
    print("大咖vip", text)
    if text == '已失效':
        return '已失效'
    elif text == "未开通":
        return '未开通'
    else:
        return 'vip'


#课堂vip
def isKeVip(self):
    self.driver.find_element_by_name('我的').click()
    #判断是否登录
    isLogin = isElement.find_Element(self, 'id', 'tv_my_fragment_login_no_login')
    if isLogin:
        # 登录账号
        login.login_userName(self)
        flag = self.driver.find_element_by_xpath('//android.view.View[@content-desc="绑定 绑定"]').is_enabled()
        if flag:
            back.ivBack(self)
    else:
        print("有登录")
    #判断是否为vip
    text=self.driver.find_element_by_id('tv_my_fragment_vip_ke_date').text
    print("课堂vip",text)
    if text=='已失效':
        return '已失效'
    elif text=="未开通":
        return '未开通'
    else:
        return 'vip'
