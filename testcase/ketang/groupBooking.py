#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
import tool.isElement as isElement
import tool.swipe as swipe
import testcase.advertisements.advertisement as ad
import testcase.base.isVip as vip
import testcase.ketang.isBuyKe as buyKe
import tool.back as back
import testcase.base.isLogin as IsLogin
import testcase.ketang.isBuyKe as isBuyKe
import testcase.base.login as login

#拼团-新建团:课程包
def groupBooking_packPage(self):
    flag = isElement.find_Element(self, "id", 'com.mbalib.android.wiki:id/recycler_package')
    if not flag:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
    # 点击系统班的第一个课程包
    list = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_package")[0].find_elements_by_class_name("android.widget.LinearLayout")
    list[0].click()
    sleep(5)
    #先判断课程是否已报名
    ll_bottom_pay=isElement.find_Element(self,'id','ll_bottom_pay')
    if ll_bottom_pay:
        print("该课程包未报名，判断该课程包是否为拼团")
        tv_ke_group_book=isElement.find_Element(self,'id','tv_ke_group_book')
        if tv_ke_group_book:
            print("该课程包是拼团")
            self.driver.find_element_by_id('tv_ke_group_book').click()
            sleep(3)
            self.driver.find_element_by_name('支付宝支付').click()
            sleep(6)
        else:
            print("该课程包没有拼团")
    else:
        print("该课程包已报名")

#拼团-新建团:课程包
def groupBooking_course(self):
    flag = isElement.find_Element(self, "id", 'com.mbalib.android.wiki:id/recycler_list')
    if not flag:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
    # 点击系统班的第一个课程包
    list = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_list")[0].find_elements_by_class_name("android.widget.LinearLayout")
    list[0].click()
    sleep(5)
    #先判断课程是否已报名
    ll_bottom_pay=isElement.find_Element(self,'id','ll_bottom_pay')
    if ll_bottom_pay:
        print("该课程未报名，判断该课程是否为拼团")
        tv_ke_group_book=isElement.find_Element(self,'id','tv_ke_group_book')
        if tv_ke_group_book:
            print("该课程是拼团")
            self.driver.find_element_by_id('tv_ke_group_book').click()
            sleep(3)
            self.driver.find_element_by_name('支付宝支付').click()
            sleep(6)
        else:
            print("该课程没有拼团")
    else:
        print("该课程已报名")

#拼团-参团

#拼团详情页-立即拼团

#拼团详情页-邀请好友

#拼团详情页-分享按钮



#拼团详情页-并发
