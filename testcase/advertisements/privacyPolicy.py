#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import tool.isElement as isElement
from time import sleep
#隐私政策弹窗

def privacy_policy_agree(self):
    #判断是否有隐私政策弹窗
    flag=isElement.find_Element(self,'id','tv_app_privacy_right_title')
    if flag:
        #存在隐私政策弹窗
        #点击同意
        self.driver.find_element_by_id('tv_app_privacy_right_agree').click()
        sleep(5)
    else:
        print("不存在隐私政策弹窗")

def privacy_policy_NoAgree(self):
    #判断是否有隐私政策弹窗
    flag=isElement.find_Element(self,'id','tv_app_privacy_right_title')
    if flag:
        #存在隐私政策弹窗
        #点击不同意
        self.driver.find_element_by_id('tv_app_privacy_right_disagree').click()
        sleep(5)
    else:
        print("不存在隐私政策弹窗")