#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#判断课程是否购买
from time import sleep
import tool.swipe as swipe

def is_buy_ke(self,title):
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    sleep(3)
    # 选择【课程】
    self.driver.find_element_by_name('课程').click()
    sleep(3)
    list=self.driver.find_elements_by_id('com.mbalib.android.wiki:id/layout_recycler')[0].find_elements_by_class_name('android.widget.RelativeLayout')
    tv_titles=self.driver.find_elements_by_id('com.mbalib.android.wiki:id/layout_recycler')[0].find_elements_by_id('com.mbalib.android.wiki:id/tv_title')
    size = len(list)
    print("list长度:",size)
    for index in range(len(tv_titles)):
        if title==tv_titles[index].text:
            print("报名成功")
            return True
        else:
           print("未找到")


