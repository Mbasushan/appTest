#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
import tool.isElement as isElement
import tool.back as back
import testcase.advertisements.advertisement as Ads
import testcase.advertisements.splashAd as splashAd

#有句名言广告位
def test_afamous_ad(self):
    print("有句名言广告")
    # 判断是否有闪屏广告
    splashAd.test_ad(self)
    # 判断是否有首页广告
    Ads.test_is_ad(self)
    print("进入有句名言")
    self.driver.find_element_by_name('有句名言').click()
    sleep(5)
    # 判断是否有广告位
    # 先判断每日一词是否是有图
    clImage = isElement.find_Element(self, 'id', 'ivAdImage')
    if clImage:
        print("有句名言有广告")
        self.driver.find_element_by_id('ivAdImage').click()
        sleep(5)
        back.ivBack(self)
    else:
        print("有句名言无广告")

# 每日一词广告
def test_dailyword_ad(self):
    print("每日一词广告")
    # 判断是否有闪屏广告
    splashAd.test_ad(self)
    # 判断是否有首页广告
    Ads.test_is_ad(self)
    print("进入每日一词")
    self.driver.find_element_by_name('每日一词').click()
    sleep(5)
    # 判断是否有广告位
    # 先判断每日一词是否是有图
    clImage = isElement.find_Element(self, 'id', 'ivAdImage')
    print("每日一词有广告", clImage)
    if clImage:
        print("每日一词有广告")
        self.driver.find_element_by_id('ivAdImage').click()
        sleep(5)
        back.ivBack(self)
    else:
        print("每日一词无广告")
