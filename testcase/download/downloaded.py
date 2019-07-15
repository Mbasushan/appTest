#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchElementException

import testcase.advertisements.advertisement as ad
import tool.isElement as isElement
import tool.getwebstate as state
import tool.ConnectionType as ConnectionType
import testcase.base.isLogin as isLogins
import testcase.base.login as Logins
from appium.webdriver.common.touch_action import TouchAction
import testcase.download.downloadKe as downloadKe
import tool.back as back

#判断是否有数据
def isData(self):
    print("判断【已下载】列表是否有数据")
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    sleep(3)
    # 选择【下载】
    self.driver.find_element_by_name('下载').click()
    sleep(3)
    flag=isElement.find_Element(self, 'id', 'tvTitle')
    if flag:
        return True
    else:
        return False

# 未登录情况下，【已下载】无数据
def noLogin_download(self):
    #判断是否登录
    isLogin=isLogins.isLogin(self)
    if isLogin:
        print("已登录，退出登录")
        Logins.log_out(self)
    else:
        print("未登录")
    # 选择【下载】
    self.driver.find_element_by_name('下载').click()
    sleep(3)
    flag = True
    try:
        self.driver.find_element_by_xpath("(//android.webkit.WebView[@content-desc=\"帐户登录 - MBA智库帐户\"])")
    except NoSuchElementException as e:
        print("false")
        flag= False
    if flag:
        print("未登录跳转到登录页")
    else:
        print("有登录不会跳转到登录页")





#用户有已下载数据，点击进入播放器
def login_download(self):
    # 判断是否登录
    isLogin = isLogins.isLogin(self)
    # 返回
    back.ivBack(self)
    if isLogin:
        print("已登录")
    else:
        print("未登录,登录账号")
        self.driver.find_element_by_id("tv_my_fragment_login_no_login").click()
        sleep(5)
        Logins.login_userName(self)
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    sleep(3)
    # 选择【下载】
    self.driver.find_element_by_name('下载').click()
    sleep(3)
    list = self.driver.find_elements_by_id('com.mbalib.android.wiki:id/recycler')[0].find_elements_by_class_name('android.widget.LinearLayout')
    if len(list)==0:
       print("已下载列表无数据")
    else:
        list[0].click()
        sleep(5)


#判断当前在播放的视音频是否在【已下载】列表中
def play_is_downloaded(self):
    print("判断当前在播放的视音频是否在【已下载】列表中")
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    sleep(3)
    # 选择【下载】
    self.driver.find_element_by_name('下载').click()
    sleep(3)
    mini=isElement.find_Element(self,'id','ll_mini_parent')
    if mini:
        print("当前正在播放")
        #判断当前播放的是否已下载
        list = self.driver.find_elements_by_id('com.mbalib.android.wiki:id/recycler')[0].find_elements_by_id('tvTitle')
        tv_title =self.driver.find_element_by_id('tv_title').text
        #判断当前页面有几条已下载数据
        size=len(list)
        print("当前播放章节标题：",tv_title)
        for index in range(size):
            text=list[index].text
            print("循环列表，当前章节标题",text)
            if tv_title ==text :
                print("当前播放的音频已下载 ")
            else:
                print("当前播放的音频未下载")
    else:
        print("当前未在播放")

#关闭网络，点击【已下载】列表的课程，跳转到播放页，可播放
def no_network_play(self):
    print("关闭网络，点击【已下载】列表的课程")
    #关闭网络
    self.driver.set_network_connection(ConnectionType.ConnectionType.NO_CONNECTION)
    print(state.getwebstate(self))
    sleep(5)
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    sleep(3)
    # 选择【下载】
    self.driver.find_element_by_name('下载').click()
    sleep(3)
    list = self.driver.find_elements_by_id('com.mbalib.android.wiki:id/recycler')[0].find_elements_by_class_name('android.widget.LinearLayout')
    print("list：",len(list))
    if len(list) == 0:
        print("已下载列表无数据")
    else:
        list[0].click()
        sleep(5)
    # 开启网络
    self.driver.set_network_connection(ConnectionType.ConnectionType.ALL_NETWORK_ON)


#【已下载】列表，长按是否删除
def delete_downloaded(self):
    print("【已下载】列表，长按是否删除")
    #先判断是否有数据
    if isData(self):
        #长按触发删除确认弹窗
        e1 =self.driver.find_elements_by_id('com.mbalib.android.wiki:id/recycler')[0].find_elements_by_class_name("android.widget.LinearLayout")[0]
        TouchAction(self.driver).long_press(e1).perform()
        sleep(5)
        tv_title = self.driver.find_element_by_id('ask_tv_content').text
        self.driver.find_element_by_id('ask_tv_confirm').click()
        # 判断是否删除成功
        list = self.driver.find_elements_by_id('com.mbalib.android.wiki:id/recycler')[0].find_elements_by_id('tvTitle')
        # 判断当前页面有几条已下载数据
        size = len(list)
        print("当前播删除章节标题：", tv_title)
        for index in range(size):
            text = list[index].text
            print("循环列表，当前章节标题", text)
            if tv_title == text:
                print("未删除成功")
            else:
                print("已删除成功")
    else:
        print("未有下载数据")