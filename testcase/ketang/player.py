#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import tool.isElement as isElement
from time import sleep
import testcase.ketang.my_ketang as ketang

#定时播放-播完本节
def rlPlayTime(self):
    #进入播放页
    thumb=ketang.playView(self)
    sleep(5)
    if thumb:
        print("成功进入播放页")
        #选择定时
        self.driver.find_element_by_id("rlPlayTime").click()
        sleep(3)
        #触发定时选择
        print("选择【播完本节】")
        self.driver.find_element_by_name('播完本节').click()
        text=self.self.driver.find_element_by_id("rlPlayTime").text
        if text=='本节完':
            print("选择播完本节")
        else:
            print("定时失败")
            return
    else:
        print("未进入播放页")

#定时播放-不开启
def rlPlayTime_noTime(self):
    #进入播放页
    thumb=ketang.playView(self)
    sleep(5)
    if thumb:
        print("成功进入播放页")
        #选择定时
        self.driver.find_element_by_id("rlPlayTime").click()
        sleep(3)
        #触发定时选择
        print("选择【不开启】")
        self.driver.find_element_by_name('不开启').click()
        text=self.self.driver.find_element_by_id("rlPlayTime").text
        if text=='定时':
            print("选择不开启")
        else:
            print("定时失败")
            return
    else:
        print("未进入播放页")


#倍速播放

#全屏播放

#拉动进度条

#暂停播放

#下载按钮

#分享按钮

#文稿按钮


