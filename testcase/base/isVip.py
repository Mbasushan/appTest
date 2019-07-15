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

#是否为大咖vip
def isVip(self):
    print("是否为大咖vip")
    #判断是否有首页横幅广告，有的话则往上滑动，显示出大咖讲百科内容
    hengfu = isElement.find_Element(self, 'id', 'iv_home_wiki')
    if hengfu:
        print('向上滑动')
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
    else:
        print('不存在横幅广告')

    print("从首页的【今日推荐】的【大咖讲百科】进入大咖首页")
    self.driver.find_elements_by_id('ivSection')[0].click()
    sleep(6)
    tvDesc=self.driver.find_element_by_id('tvdesc').text
    print("tvdesc的值：",tvDesc)
    if tvDesc=='专享大咖讲解':
        print("该用户不是VIP用户")
        return False
    elif tvDesc=="VIP已到期":
        print("该用户VIP已到期")
        return False
    else:
        return True

#课堂vip
def isKeVip(self):
    self.driver.find_element_by_name('我的').click()
    #判断是否登录
    isLogin = isElement.find_Element(self, 'id', 'tv_my_fragment_login_no_login')
    if isLogin:
        # 登录账号
        login.login_userName(self)
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
