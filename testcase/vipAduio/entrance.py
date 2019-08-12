#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
import tool.isElement as isElement
import tool.back as back
import testcase.base.isVip as Isvip
import tool.swipe as swipe

# app首页【大咖讲百科】入口
def test_vip_homePage(self):
    """app首页【大咖讲百科】入口"""
    self.driver.find_element_by_id('home_tv_wiki').click()
    sleep(5)
    #判断是否进入百科首页
    screen = swipe.get_size(self)
    self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
    #获取标题栏标题
    title=self.driver.find_element_by_id('tv_wiki_home_title').text
    if title=='智库百科':
        print("进入的是百科首页")
    else:
        print("进入的不是百科首页")

#点击菜单栏【百科】
def test_vip_menuBar(self):
    """从菜单栏进入【百科】首页"""
    self.driver.find_elements_by_id('tv_tab_title')[2].click()
    sleep(5)
    # 判断是否进入百科首页
    screen = swipe.get_size(self)
    self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
    # 获取标题栏标题
    title = self.driver.find_element_by_id('tv_wiki_home_title').text
    if title == '智库百科':
        print("进入的是百科首页")
        screen1 = swipe.get_size(self)
        self.driver.swipe(screen1[0] * 0.5, screen1[1] * 0.25, screen1[0] * 0.5, screen1[1] * 0.75, 6000)
    else:
        print("进入的不是百科首页")


#该入口新版本已隐藏
# 从首页的【今日推荐】的【大咖讲百科】进入大咖首页
def test_vipAduio01(self):
    """从首页的【今日推荐】的【大咖讲百科】进入大咖首页"""
    print("从首页的【今日推荐】的【大咖讲百科】进入大咖首页")
    screen = swipe.get_size(self)
    self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
    self.driver.find_elements_by_id('ivSection')[0].click()
    sleep(5)

#该入口新版本已隐藏
# 从首页的【今日推荐】的【专区】进入大咖首页
def test_vipAduioMore(self):
    """从首页的【今日推荐】的【专区】进入大咖首页"""
    print("从首页的【今日推荐】的【专区】进入大咖首页")
    screen = swipe.get_size(self)
    self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
    self.driver.find_elements_by_id('tvMore')[0].click()
    sleep(5)

#该入口新版本已隐藏
# 点击首页的【今日推荐】的音频进入大咖播放页
def test_vipAduioPlay(self):
    """点击首页的【今日推荐】的音频进入大咖播放页"""
    print("点击首页的【今日推荐】的音频进入大咖播放页")
    # 用户是否为VIP用户
    isVip = Isvip.isVip(self)
    back.ivBack(self)
    sleep(5)
    # 点击的是否为试听音频
    aduio = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/wikiAudioRecycler")[0].find_elements_by_class_name("android.widget.RelativeLayout")
    print("audio", aduio)
    try:
        aduioIsVip = aduio[0].find_element_by_id('imageVip').is_displayed()
    except:
        aduioIsVip = False
    if isVip:
        print("点击音频进入大咖播放页")
        aduio[0].find_element_by_id('tv_title').click()
        sleep(5)
    else:
        # 用户不是VIP用户则需判断音频是否为试听音频
        if aduioIsVip:
            print("该音频是非试听音频")
            aduio[0].find_element_by_id('tv_title').click()
            sleep(5)
            # 触发分享弹窗或者开通VIP弹窗
            tvOpen = isElement.find_Element(self, 'id', 'tvOpen')
            # 点击【开通vip】
            if tvOpen:
                print("有触发弹窗")
                self.driver.find_element_by_id('tvOpen').click()
                sleep(5)
                # 进入开通vip页面，判断是否进入的是开通vip页面
                tvPay = isElement.find_Element(self, 'id', 'tvPay')
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


