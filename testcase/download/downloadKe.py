#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
import testcase.ketang.my_ketang as myKe
import tool.isElement as isElement
import testcase.advertisements.advertisement as Ads
import tool.swipe as swipe

#从【我的课程】进入课程介绍页下载课程
def download_ke(self):
    print("从【我的课程】进入课程介绍页下载课程")
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    sleep(3)
    # 选择【课程】
    self.driver.find_element_by_name('课程').click()
    sleep(3)
    list =self.driver.find_elements_by_id('com.mbalib.android.wiki:id/layout_recycler')[0].find_elements_by_id('com.mbalib.android.wiki:id/tv_title')
    print("我的课程数据：",list)
    if len(list) != 0:
        # 点击进入课程介绍页
        list[0].click()
        sleep(5)
        #介绍页点击【XX学习】
        self.driver.find_element_by_id('tv_study').click()
        sleep(5)
        print("判断是否下载")
        isDownLoda = isElement.find_Element(self, 'id', 'ivDownloadConplete')
        if isDownLoda:
            print("已下载")
        else:
            print("还未下载,点击下载")
            self.driver.find_element_by_id('imageDownload').click()
            sleep(5)
    else:
        # 该用户未报名
        print("用户未报名过")

#未报名，点击下载，触发提示弹窗,点击【马上报名】
def no_apply(self):
    self.driver.find_element_by_name('课堂').click()
    print("课程未报名，有试听章节，进入试听点击【下载】")
    Ads.test_ketang_ad(self)
    screen = swipe.get_size(self)
    self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 10000)
    list = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_list")
    if not list:
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 10000)
        list = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_list")
    list[0].find_elements_by_class_name("android.widget.LinearLayout")[0].click()
    sleep(5)
    isBuy=isElement.find_Element(self,'id','tv_buy')
    if isBuy:
        print("该课程未报名")
        #判断该课程是否有试听章节
        course=isElement.find_Element(self,'id','tv_tab_title')
        if not course:
            self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 10000)
        self.driver.find_element_by_name('课程').click()
        sleep(3)
        isListen=isElement.find_Element(self,"id","tv_try_listen")
        if isListen:
            print("该课程有试听章节")
            self.driver.find_elements_by_id('com.mbalib.android.wiki:id/llparent')[0].find_elements_by_id("com.mbalib.android.wiki:id/recycler")[0].click()
            sleep(5)
            self.driver.find_element_by_id("imageDownload").click()
            sleep(3)
            #触发【报名后可下载课程】弹窗
            popuWind=isElement.find_Element(self,'name','报名后可下载课程')
            if popuWind:
                print("触发【报名后可下载课程】弹窗")
                #点击【马上报名】
                self.driver.find_element_by_id("tvSignUp").click()
                sleep(5)
                title=self.driver.find_element_by_id('toolbar_tv_title').text
                if title=='课程详情':
                    print("点击【马上报名】返回到课程详情页，该测试用例成功")
                else:
                    print("点击【马上报名】跳转不是返回到了课程详情页")
            else:
                print("未触发【报名后可下载课程】弹窗")

        else:
            print("该课程无试听章节")
    else:
        print("该课程已报名")

#未报名，点击下载，触发提示弹窗,点击【取消】
def no_apply_cancle(self):
    self.driver.find_element_by_name('课堂').click()
    print("课程未报名，有试听章节，进入试听点击【下载】")
    Ads.test_ketang_ad(self)
    screen = swipe.get_size(self)
    self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 10000)
    list = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_list")
    if not list:
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 10000)
        list = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_list")
    list[0].find_elements_by_class_name("android.widget.LinearLayout")[0].click()
    sleep(5)
    isBuy=isElement.find_Element(self,'id','tv_buy')
    if isBuy:
        print("该课程未报名")
        #判断该课程是否有试听章节
        course = isElement.find_Element(self, 'id', 'tv_tab_title')
        if not course:
            self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 10000)
        self.driver.find_element_by_name('课程').click()
        sleep(3)
        isListen=isElement.find_Element(self,"id","tv_try_listen")
        if isListen:
            print("该课程有试听章节")
            self.driver.find_elements_by_id('com.mbalib.android.wiki:id/llparent')[0].find_element_by_id("com.mbalib.android.wiki:id/recycler").click()
            sleep(5)
            self.driver.find_element_by_id("imageDownload").click()
            sleep(3)
            #触发【报名后可下载课程】弹窗
            popuWind=isElement.find_Element(self,'name','报名后可下载课程')
            if popuWind:
                print("触发【报名后可下载课程】弹窗,点击【取消】")
                #点击【取消】
                self.driver.find_element_by_id("tvCancel").click()
                sleep(5)
            else:
                print("未触发【报名后可下载课程】弹窗")
        else:
            print("该课程无试听章节")
    else:
        print("该课程已报名")

