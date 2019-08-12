#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
import tool.isElement as isElement
#我的课程
def my_ketang(self):
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    sleep(3)
    # 选择【课程】
    self.driver.find_element_by_name('课程').click()
    sleep(3)
    list = self.driver.find_elements_by_id('com.mbalib.android.wiki:id/layout_recycler')[0].find_elements_by_class_name('android.widget.RelativeLayout')
    if len(list)!=0:
        #点击进入课程介绍页
        list[0].click()
        sleep(5)
    else:
        #该用户未报名
        print("用户未报名过")

#进入播放页
def playView(self):
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    sleep(3)
    # 选择【课程】
    self.driver.find_element_by_name('课程').click()
    sleep(3)
    list = self.driver.find_elements_by_id('com.mbalib.android.wiki:id/layout_recycler')[0].find_elements_by_class_name('android.widget.RelativeLayout')
    if len(list) != 0:
        # 点击进入课程介绍页
        list[0].click()
        sleep(5)
        self.driver.find_element_by_id("tv_study").click()
        sleep(5)
        # 进入播放页
        thumb = isElement.find_Element(self, 'id', 'com.mbalib.android.wiki:id/layout_play_view')
        sleep(5)
        if thumb:
            return True
        else:
            return False
    else:
        print("未报名过")
        return False