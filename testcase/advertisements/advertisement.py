#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
import tool.isElement as isElement
import tool.back as back

#判断是否有更新版本弹窗---有点击稍后安装
def test_ask_tv_cancel(self):
    print('稍后安装用例')
    askTvTitle = isElement.find_Element(self, 'id', 'ask_tv_title')
    if askTvTitle:
        print("存在有更新版本弹窗")
        # 点击【稍后安装】
        self.driver.find_element_by_id('ask_tv_cancel').click()
    else:
        print("不存在有更新版本弹窗")
        sleep(5)

#立即安装
def test_ask_tv_confirm(self):
    print('立即安装用例')
    askTvTitle = isElement.find_Element(self, 'id', 'ask_tv_title')
    if askTvTitle:
        print("存在有更新版本弹窗")
        # 点击【立即安装】
        self.driver.find_element_by_id('ask_tv_confirm').click()
    else:
        print("不存在有更新版本弹窗")
        sleep(5)

# 判断是否有首页广告
def test_is_ad(self):
    driver = self.driver
    llparent = isElement.find_Element(self, 'id', 'image')
    sleep(5)
    print('判断是否有首页广告', llparent)
    if llparent:  # 判断是否有首页广告
        print('有首页广告')
        driver.find_element_by_id('image').click()
        sleep(5)
        isWeixin = isElement.find_Element(self, 'id', 'tv_popu_course_bind_wx_bind')
        if isWeixin:
            self.driver.find_element_by_id('tv_popu_course_bind_wx_cancel').click()
        #返回
        back.ivBack(self)
    else:
        print("无首页广告")
    sleep(5)

#app轮播图
def test_home_slideshow(self):
    print('banner图')
    # 判断是否有闪屏广告
    sleep(5)
    #点击banner
    self.driver.find_element_by_id('bannerContainer').click()
    # 返回
    back.ivBack(self)

#app首页横幅广告
def test_home_banner(self):
    print('首页横幅广告')
    #判断是否有首页横幅广告
    hengfu=isElement.find_Element(self,'id','iv_home_wiki')
    if hengfu:
        print('存在横幅广告')
        self.driver.find_element_by_id('iv_home_wiki').click()
        back.ivBack(self)
    else:
        print('不存在横幅广告')



#app课堂首页广告
def test_ketang_ad(self):
    print("课堂首页广告")
    #判断是否有弹窗广告
    llparent=isElement.find_Element(self,'id','llparent')
    if llparent:
        print("课堂首页有广告")
        self.driver.find_element_by_id('llparent').click()
        sleep(5)
        back.ivBack(self)
    else:
        print("课堂首页无广告")
    sleep(5)
