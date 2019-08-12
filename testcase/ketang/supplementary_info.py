#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#信息补充弹窗
import tool.find_toast as findToast
import tool.isElement as isElement
from time import sleep

#不填写信息,点击保存
def  not_filled(self):
    self.driver.find_element_by_id('tvConfirm').click()
    flag=findToast.find_toast(self,'请输入姓名')
    if flag:
        print("未填写补充信息，提示【请输入姓名】")
        return False
    else:
        print("未有提示")
        return True

#不填写信息,点击取消
def  not_filled_cancel(self):
    self.driver.find_element_by_id('tvCancel').click()

#填写所有补充信息
def filled(self):
    #判断姓名是否存在
    name=isElement.find_Element(self,'id','etEditName')
    if name:
        print("存在姓名，输入数据")
        self.driver.find_element_by_id('etEditName').send_keys('Susan')
        # 关闭键盘
        self.driver.hide_keyboard()
    else:
        print("不存在姓名，不用输入数据")

    #判断公司是否存在
    company=isElement.find_Element(self,'id','etEditCompany')
    if company:
        print("存在公司，输入数据")
        self.driver.find_element_by_id('etEditCompany').send_keys('MBA')
        # 关闭键盘
        self.driver.hide_keyboard()
    else:
        print("不存在公司，不用输入数据")

    #判断职务是否存在
    etEditJob=isElement.find_Element(self,'id','etEditJob')
    if etEditJob:
        print("存在职务，输入数据")
        self.driver.find_element_by_id('etEditJob').send_keys('test')
        # 关闭键盘
        self.driver.hide_keyboard()
    else:
        print("不存在职务，不输入数据")
    #判断地区是否存在
    tvAddress=isElement.find_Element(self,'id','tvAddress')
    if tvAddress:
        self.driver.find_element_by_id('tvAddress').click()
        print("存在地区，输入数据")
        #选择省
        self.driver.find_element_by_id('options1').click()#点击省选择
        sleep(10)
        #滑动
        self.driver.swipe(20,800,100,900)
        sleep(10)
        #选择市
        self.driver.find_element_by_id('options2').click()
        sleep(10)
        #滑动
        self.driver.swipe(190,800,300,900)
        sleep(10)

        #选择区
        self.driver.find_element_by_id('options3').click()
        sleep(10)
        # 滑动
        self.driver.swipe(400,800,500,900)
        sleep(5)
        self.driver.find_element_by_id('btnSubmit').click()
    else:
        print("不存在地区，不输入数据")

    sleep(5)
    #提交信息补充数据
    self.driver.find_element_by_id('tvConfirm').click()

#不填写姓名，其他都填
def no_name_filled(self):
    # 判断姓名是否存在
    name = isElement.find_Element(self, 'id', 'etEditName')
    if name:
        print("存在姓名，不输入数据")

    # 判断公司是否存在
    company = isElement.find_Element(self, 'id', 'etEditCompany')
    if company:
        print("存在公司，输入数据")
        self.driver.find_element_by_id('etEditCompany').send_keys('MBA')
        # 关闭键盘
        self.driver.hide_keyboard()
    else:
        print("不存在公司，不用输入数据")

    # 判断职务是否存在
    etEditJob = isElement.find_Element(self, 'id', 'etEditJob')
    if etEditJob:
        print("存在职务，输入数据")
        self.driver.find_element_by_id('etEditJob').send_keys('test')
        # 关闭键盘
        self.driver.hide_keyboard()
    else:
        print("不存在职务，不输入数据")
    # 判断地区是否存在
    tvAddress = isElement.find_Element(self, 'id', 'tvAddress')
    if tvAddress:
        self.driver.find_element_by_id('tvAddress').click()
        print("存在地区，输入数据")
        # 选择省
        # self.driver.find_element_by_id('options1').click()
        # 滑动
        # self.driver.swipe(20,722,180,960,200)
        # sleep(5)
        # 选择市
        # self.driver.find_element_by_id('options2').click()
        # 滑动
        # self.driver.swipe(190,722,360,960,200)

        # 选择区
        # self.driver.find_element_by_id('options3').click()
        # 滑动
        # self.driver.swipe(400, 722, 540,960,200)
        # sleep(3)
        self.driver.find_element_by_id('btnSubmit').click()
    else:
        print("不存在地区，不输入数据")

    sleep(5)
    # 提交信息补充数据
    self.driver.find_element_by_id('tvConfirm').click()
    #判断toast信息

