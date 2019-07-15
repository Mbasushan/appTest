#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import testcase.advertisements.splashAd as splashAd
import testcase.advertisements.advertisement as ads
import tool.isElement as isElements

def isLogin(self):
    print("判断用户是否登录")
    # 判断是否有闪屏广告
    splashAd.test_ad(self)
    # 判断是否有首页广告
    ads.test_is_ad(self)
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    isLogin=isElements.find_Element(self,'id','tv_my_fragment_login_no_login')
    if isLogin:
        print("用户未登录")
        return False
    else:
        return True