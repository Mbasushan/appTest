#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import testcase.advertisements.splashAd as splashAd
import testcase.advertisements.advertisement as ads

def isLogin(self):
    print("判断用户是否登录")
    # 判断是否有闪屏广告
    splashAd.test_ad(self)
    # 判断是否有首页广告
    ads.test_is_ad(self)
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    isLogin=self.driver.find_element_by_id('tvNickName').text
    if isLogin=='点击登录':
        print("用户未登录")
        return False
    else:
        return True