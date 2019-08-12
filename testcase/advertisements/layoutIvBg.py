#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver
from appium import webdriver
import tool.isElement as isElement
import tool.swipe as swipe

# 判断是否有引导图
def test_layout_iv_bg(self):
    print("引导图")
    ivBg = isElement.find_Element(self, 'id', 'layout_iv_bg')
    if ivBg:
        print("引导图存在")
        # 左滑
        screen = self.get_size()
        num = 1
        while (num <= 4):
            self.driver.swipe(screen[0] * 0.75, screen[1] * 0.5, screen[0] * 0.05, screen[1] * 0.5, 6000)
            print('第', num, '张引导图')
            num =num+1
        self.driver.find_element_by_id('layout_iv_bg').click()
        sleep(5)
    else:
        print("无引导图")
