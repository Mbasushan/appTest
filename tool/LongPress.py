#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from appium.webdriver.common.touch_action import TouchAction


def long_press(self, el=None, x=None, y=None, duration=1000):
        #长按操作,可以传定位的元素对象，也可以传坐标
        #el 是定位元素的对象
        #x,y是传坐标
        #duration是按住的持续时间，默认1000，单位是毫秒
        TouchAction(self.driver).long_press(el).perform()