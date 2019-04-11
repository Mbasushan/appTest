#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver
from appium import webdriver
import tool.isElement as isElement

# 判断是否有好评弹窗
def test_tvcnacle(self):
    print("是否有好评弹窗")
    tvPraise = isElement.find_Element(self, 'id', 'tvPraise')
    sleep(5)
    if tvPraise:
        print("存在好评弹窗，点击【取消】")
        self.driver.find_element_by_id('tvCnacle').click()
    else:
        print("不存在好评弹窗")

#点击【暖心好评】
def test_praise(self):
    print("是否有好评弹窗")
    tvPraise = isElement.find_Element(self, 'id', 'tvPraise')
    sleep(5)
    if tvPraise:
        print("存在好评弹窗，点击【暖心好评】")
        self.driver.find_element_by_id('tvPraise').click()
    else:
        print("不存在好评弹窗")

# 点击【差评吐槽】
def test_complaints(self):
    print("是否有好评弹窗")
    tvPraise = isElement.find_Element(self, 'id', 'tvPraise')
    sleep(5)
    if tvPraise:
        print("存在好评弹窗，点击【差评吐槽】")
        self.driver.find_element_by_id('tvComplaints').click()
        sleep(5)
        # 跳转到【意见反馈】页面
        title = self.driver.find_element_by_id('toolbar_tv_title').text
        if title == '意见反馈':
            print("点击【差评吐槽】跳转到【意见反馈】页面成功")
        else:
            print("点击【差评吐槽】跳转到【意见反馈】页面失败")
    else:
        print("不存在好评弹窗")