#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
import tool.isElement as isElement
import tool.swipe as swipe
import testcase.advertisements.advertisement as ad
import testcase.ketang.isMiniPlay as isMiniPlays
import testcase.ketang.my_ketang as ketang

#课程包进入课程进入播放
def ke_packPage(self):
    # 切换到课堂
    self.driver.find_element_by_name('课堂').click()
    sleep(5)
    ad.test_ketang_ad(self)
    sleep(3)
    isMini=isMiniPlays.isMiniPlay(self)
    if isMini:
        self.driver.find_element_by_id('iv_close').click()
    flag=isElement.find_Element(self,"id",'com.mbalib.android.wiki:id/recycler_package')
    if  not flag:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
    #点击系统班的第一个课程包
    list = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_package")[0].find_elements_by_class_name("android.widget.LinearLayout")
    list[0].click()
    sleep(5)
    #判断课程包是否报名
    tvBuy = isElement.find_Element(self, 'id', 'tv_buy')
    if tvBuy:
        #未报名
        print("该课程包未报名")
        return
    else:
        tabTitle=isElement.find_Element(self,'id','tv_tab_title')
        while not tabTitle:
            screen = swipe.get_size(self)
            self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 3000)
            tabTitle = isElement.find_Element(self, 'id', 'tv_tab_title')
    self.driver.find_elements_by_id("com.mbalib.android.wiki:id/tv_tab_title")[1].click()
    sleep(3)
    self.driver.find_elements_by_id("com.mbalib.android.wiki:id/llParent")[0].click()
    #进入课程的介绍页
    sleep(5)
    self.driver.find_element_by_id("tv_study").click()
    sleep(5)
    #进入播放页
    thumb=isElement.find_Element(self,'id','com.mbalib.android.wiki:id/layout_play_view')
    sleep(5)
    if thumb:
        print("成功进入播放页")
        self.driver.find_element_by_id('play_view').click()
        self.driver.find_element_by_id('iv_back').click()
        playState=isElement.find_Element(self,'id','iv_close')
        if playState:
            print("课程未自动播放")
        else:
            print("课程有自动播放")
    else:
        print("未进入播放页")

#从课程进入播放
def ke_course(self):
    # 切换到课堂
    self.driver.find_element_by_name('课堂').click()
    sleep(5)
    ad.test_ketang_ad(self)
    sleep(3)
    isMini = isMiniPlays.isMiniPlay(self)
    if isMini:
        self.driver.find_element_by_id('iv_close').click()
    flag = isElement.find_Element(self, "id", 'com.mbalib.android.wiki:id/recycler_list')
    while not flag:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
        flag = isElement.find_Element(self, "id", 'com.mbalib.android.wiki:id/recycler_list')
        # 点击全部课程的第一个课程
    list = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_list")[0].find_elements_by_class_name("android.widget.LinearLayout")
    list[0].click()
    sleep(5)
    # 判断课程是否报名
    tvBuy = isElement.find_Element(self, 'id', 'tv_buy')
    if tvBuy:
        # 未报名
        print("该课程未报名")
        return
    else:
        tabTitle = isElement.find_Element(self, 'id', 'tv_tab_title')
        while not tabTitle:
            screen = swipe.get_size(self)
            self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 3000)
            tabTitle = isElement.find_Element(self, 'id', 'tv_tab_title')
    self.driver.find_elements_by_id("com.mbalib.android.wiki:id/tv_tab_title")[1].click()
    sleep(3)
    self.driver.find_element_by_id("tv_study").click()
    sleep(5)
    # 进入播放页
    thumb = isElement.find_Element(self, 'id', 'com.mbalib.android.wiki:id/layout_play_view')
    sleep(5)
    if thumb:
        print("成功进入播放页")
        self.driver.find_element_by_id('play_view').click()
        self.driver.find_element_by_id('iv_back').click()
        playState = isElement.find_Element(self, 'id', 'iv_close')
        if playState:
            print("课程未自动播放")
        else:
            print("课程有自动播放")
    else:
        print("未进入播放页")

#未报名，有试听章节，不是点击【试听】按钮
def ke_course_audition_noBuy(self):
    """未报名点击章节试听"""
    # 切换到课堂
    self.driver.find_element_by_name('课堂').click()
    sleep(5)
    ad.test_ketang_ad(self)
    sleep(3)
    isMini = isMiniPlays.isMiniPlay(self)
    if isMini:
        self.driver.find_element_by_id('iv_close').click()
    flag = isElement.find_Element(self, "id", 'com.mbalib.android.wiki:id/recycler_list')
    while not flag:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
        flag = isElement.find_Element(self, "id", 'com.mbalib.android.wiki:id/recycler_list')
    # 点击全部课程的第一个课程
    list = self.driver.find_element_by_id("com.mbalib.android.wiki:id/recycler_list").find_elements_by_id("llParent")
    list[0].click()
    sleep(5)
    # 判断课程是否报名
    tvBuy = isElement.find_Element(self, 'id', 'tv_buy')
    if tvBuy:
        # 未报名
        print("该课程未报名")
        tabTitle = isElement.find_Element(self, 'id', 'tv_tab_title')
        while not tabTitle:
            screen = swipe.get_size(self)
            self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 3000)
            tabTitle = isElement.find_Element(self, 'id', 'tv_tab_title')
        self.driver.find_elements_by_id("com.mbalib.android.wiki:id/tv_tab_title")[1].click()
        sleep(3)
        #判断该课程是否有试听章节
        listen=isElement.find_Element(self,'id','tv_try_listen')
        while not listen:
            screen = swipe.get_size(self)
            self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
            listen = isElement.find_Element(self, 'id', 'tv_try_listen')
        self.driver.find_elements_by_id('com.mbalib.android.wiki:id/recycler')[0].find_elements_by_id('note_iv_title')[0].click()
        sleep(5)
        # 进入播放页
        thumb = isElement.find_Element(self, 'id', 'com.mbalib.android.wiki:id/layout_play_view')
        sleep(5)
        if thumb:
            print("成功进入播放页")
            self.driver.find_element_by_id('play_view').click()
            self.driver.find_element_by_id('iv_back').click()
            playState = isElement.find_Element(self, 'id', 'iv_close')
            if playState:
                print("课程未自动播放")
            else:
                print("课程有自动播放")
    else:
        #已报名
        print("该课程已报名")

#未报名，点击【试听】按钮
def ke_course_auditionBut_noBuy(self):
    """未报名点击【试听】按钮"""
    # 切换到课堂
    self.driver.find_element_by_name('课堂').click()
    sleep(5)
    ad.test_ketang_ad(self)
    sleep(3)
    isMini = isMiniPlays.isMiniPlay(self)
    if isMini:
        self.driver.find_element_by_id('iv_close').click()
    flag = isElement.find_Element(self, "id", 'com.mbalib.android.wiki:id/recycler_list')
    while not flag:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
        flag = isElement.find_Element(self, "id", 'com.mbalib.android.wiki:id/recycler_list')
    # 点击全部课程的第一个课程
    list = self.driver.find_element_by_id("com.mbalib.android.wiki:id/recycler_list").find_elements_by_id("llParent")
    list[0].click()
    sleep(5)
    # 判断课程是否报名
    tvBuy = isElement.find_Element(self, 'id', 'tv_buy')
    if tvBuy:
        # 未报名
        print("该课程未报名")
        listen=isElement.find_Element(self,'id','tvTryListen')
        if listen:
            print("该课程【试听】按钮显示")
            self.driver.find_element_by_id('tvTryListen').click()
            sleep(5)
            # 进入播放页
            thumb = isElement.find_Element(self, 'id', 'com.mbalib.android.wiki:id/layout_play_view')
            sleep(5)
            if thumb:
                print("成功进入播放页")
                self.driver.find_element_by_id('play_view').click()
                self.driver.find_element_by_id('iv_back').click()
                playState = isElement.find_Element(self, 'id', 'iv_close')
                if playState:
                    print("课程未自动播放")
                else:
                    print("课程有自动播放")
        else:
            print("该课程【试听】按钮隐藏")
    else:
        print("该课程未报名")

#未报名，课程未有试听章节，点击课程
def ke_course_NoListenButton(self):
    """未报名，点击未有试听章节"""
    sleep(5)
    ad.test_ketang_ad(self)
    sleep(3)
    isMini = isMiniPlays.isMiniPlay(self)
    if isMini:
        self.driver.find_element_by_id('iv_close').click()
    flag = isElement.find_Element(self, "id", 'com.mbalib.android.wiki:id/recycler_list')
    while not flag:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
        flag = isElement.find_Element(self, "id", 'com.mbalib.android.wiki:id/recycler_list')
    # 点击全部课程的第一个课程
    list = self.driver.find_element_by_id("com.mbalib.android.wiki:id/recycler_list").find_elements_by_id("llParent")
    list[0].click()
    sleep(5)
    # 判断课程是否报名
    tvBuy = isElement.find_Element(self, 'id', 'tv_buy')
    if tvBuy:
        # 未报名
        print("该课程未报名")
        tabTitle = isElement.find_Element(self, 'id', 'tv_tab_title')
        while not tabTitle:
            screen = swipe.get_size(self)
            self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 3000)
            tabTitle = isElement.find_Element(self, 'id', 'tv_tab_title')
        self.driver.find_elements_by_id("com.mbalib.android.wiki:id/tv_tab_title")[1].click()
        sleep(3)
        # 判断该课程是否有试听章节
        listen = isElement.find_Element(self, 'id', 'tv_try_listen')
        if not listen:
            self.driver.find_elements_by_id('com.mbalib.android.wiki:id/recycler')[0].find_elements_by_id('note_iv_title')[0].click()
            sleep(5)
            print("触发支付弹层")
        else:
            print("有试听章节")
    else:
        # 已报名
        print("该课程已报名")

#从【我的课程】进入课程详情页进行播放
def ke_course_play_myCourse(self):
    thumb=ketang.playView(self)
    sleep(5)
    if thumb:
        print("成功进入播放页")
        self.driver.find_element_by_id('play_view').click()
        self.driver.find_element_by_id('iv_back').click()
        playState = isElement.find_Element(self, 'id', 'iv_close')
        if playState:
            print("课程未自动播放")
        else:
            print("课程有自动播放")
    else:
        print("未进入播放页")

#从【全局播放器】进入播放页
def miniPlay_keCourse(self):
    flag=isMiniPlays.isMiniPlay(self)
    if flag:
        self.driver.find_element_by_id('ll_mini_parent').click()
        sleep(5)
        playView=isElement.find_Element(self,'id','layout_play_view')
        if playView:
            print("进入播放页")
        else:
            print("未进入播放页")
    else:
        print("未有全局播放器")
        return


#关闭全局播放器
def close_miniPlay(self):
    flag=isMiniPlays.isMiniPlay(self)
    if flag:
        # 判断全局播放器是暂停还是播放状态
        close = isElement.find_Element(self, 'id', 'iv_close')
        if close:
            print("关闭全局播放器")
            self.driver.find_element_by_id('iv_close').click()
        else:
            print("播放器未暂停，先暂停再关闭")
            self.driver.find_element_by_id('iv_play_state').click()
            self.driver.find_element_by_id('iv_close').click()
    else:
        print("未有全局播放器")
        return

#暂停/播放全局播放器
def miniPlay_play(self):
    flag=isMiniPlays.isMiniPlay(self)
    if flag:
        #判断全局播放器是暂停还是播放状态
        close=isElement.find_Element(self,'id','iv_close')
        if close:
            print("全局播放器为暂停，点击播放")
            self.driver.find_element_by_id('iv_play_state').click()
            close = isElement.find_Element(self, 'id', 'iv_close')
            if close:
                print("未播放")
                return
            else:
                print("播放成功")
                return
        else:
            print("全局播放器为播放，点击暂停")
            self.driver.find_element_by_id('iv_play_state').click()
            close = isElement.find_Element(self, 'id', 'iv_close')
            if close:
                print("未播放")
                return
            else:
                print("播放成功")
                return
    else:
        print("未有全局播放器")
        return



#退出播放页，显示【全局播放器】

#播放页暂停播放，退出播放页，不显示【全局播放器】
