#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
import tool.isElement as isElement
import tool.back as back
import testcase.advertisements.advertisement as Ads

# 闪屏广告点击跳转
def test_splash_tv_skip(self):
    # 判断是否有闪屏广告
    print('判断是否有闪屏广告')
    splash = isElement.find_Element(self, 'id', 'splash_iv_image')
    if splash:
        print('有闪屏广告点击【跳过】')
        self.driver.find_element_by_id('splash_tv_skip').click()
        Ads.test_is_ad(self)
    else:
        print('test_splash_tv_skip无闪屏广告')


# 不点击跳过闪屏广告，倒计时结束
def test_noSkip(self):
    print('不点击跳过闪屏广告，倒计时结束')
    # 判断是否有闪屏广告
    splash = isElement.find_Element(self, 'id', 'splash_iv_image')
    # 不点击闪屏广告或者跳过按钮，倒计时结束跳转到首页
    if splash:
        print('有闪屏广告不做操作等倒计时')
        sleep(10)
        # 判断是否有首页广告
        Ads.test_is_ad(self)
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
        Ads.test_is_ad(self)
    else:
        print('test_ad无闪屏广告')

