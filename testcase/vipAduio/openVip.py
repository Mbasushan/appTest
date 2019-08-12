#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
import tool.isElement as isElement
import tool.swipe as swipe
import tool.back as back

#开通vip入口

#大咖场景详情页

#我的页面-大咖开通页入口
def my_open_vip(self):
    print("[我的]页面大咖开通入口")

#大咖开通页背景广告位
def test_wiki_audio_vip(self):
    print("大咖开通页背景广告位")
    screen = swipe.get_size(self)
    self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
    #进入大咖首页
    print("点击首页的大咖讲百科进入大咖首页")
    self.driver.find_elements_by_id("com.mbalib.android.wiki:id/ivSection")[0].click()
    #点击开通，进入开通页
    self.driver.find_element_by_id('ll_header').click()
    sleep(5)
    vipAd=isElement.find_Element(self,'id','ivVipBanner')
    if vipAd:
        print("存在大咖开通页背景广告位")
        self.driver.find_element_by_id('ivVipBanner').click()
        sleep(5)
        back.ivBack(self)
    else:
        print("不存在大咖开通页背景广告位")