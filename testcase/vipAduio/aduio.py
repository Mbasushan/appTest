#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
import tool.isElement as isElement
import tool.swipe as swipe


# 搜索百科条目框
def test_wiki_search(self):
    self.driver.find_element_by_id('ll_wiki_home_search').click()
    sleep(5)
    # 进入条目搜索页签
    # 判断是否进入的是搜索页面
    flag = isElement.find_Element(self, 'id', 'search_bg')
    if flag:
        print("搜索页面")
        self.driver.find_element_by_id('search_et_content').send_keys(u"ceshi")
        self.driver.find_element_by_id('toolbar_tv_cancel').click()
        sleep(5)
    else:
        print("不是搜索页面")


# 六大分类
def test_wiki_classify(self):
    print("百科首页六大分类")


# 进入开通vip页面
def test_open_vip(self):
    print("开通vip")
    self.driver.find_element_by_id('iv_wiki_home_open_vip').click()
    sleep(5)
    # 判断是否进入开通大咖vip页面
    text = self.driver.find_element_by_id('tvTitle').text
    if text == "大咖讲百科VIP":
        print("进入大咖开通vip页面")
    else:
        print("未进入大咖开通vip页面")


# 进入大咖场景列表页
def test_scene_list(self):
    flag = isElement.find_Element(self, 'id', 'iv_wiki_home_scene_more')
    if flag:
        self.driver.find_element_by_id('iv_wiki_home_scene_more').click()
        sleep(5)


# 进入大咖场景详情页
# type  1   百科首页的场景列表进入
# type  2   大咖场景列表页进入
def test_scene_details(self, type):
    if type == 1:
        flag = isElement.find_Element(self, 'id', 'recycler_wiki_home_scene')
        if flag:
            print("存在大咖场景列表")
        else:
            print("不存在大咖场景")
            return
    list = self.driver.find_elements_by_id('iv_item_wiki_scene')
    list[0].click()
    sleep(5)
    print("进入大咖场景列表")


# 大咖场景详情页进入播放页
def test_scene_list_to_play(self, isVip):
    empty = isElement.find_Element(self, 'id', 'layout_ll_empty')
    if empty:
        print("该场景暂无数据")
    else:
        print("该场景有数据")
        # 点击vip音频可进行播放
        list = self.driver.find_elements_by_id('ll_parent')[1].find_elements_by_class_name(
            'android.widget.RelativeLayout')
        flag = list[0].find_element_by_id('ivImageVip').is_enabled()
        list[0].click()
        sleep(5)
        if flag:
            print("该音频是vip音频")
            if isVip:
                print("用户是vip，进入播放页")
            else:
                print("用户不是vip用户，触发开通弹窗")
                parentPanel = isElement.find_Element(self, 'id', 'parentPanel')
                if parentPanel:
                    print("触发了开通提示弹窗")
                else:
                    print("未触发")
        else:
            print("该音频不是vip音频，不管用户是否为vip都进入播放页")

        # 判断进入的是否为播放页
        play = isElement.find_Element(self, 'id', 'rl_wiki_play_detail_top')
        if play:
            print("进入播放页")
        else:
            print("未进入播放页")


# 大咖教师主页列表进入播放页
def wiki_teacher_list(self, isVip):
    print("大咖教师主页列表进入播放页")
    # 点击vip音频可进行播放
    list = self.driver.find_elements_by_id('ll_parent')[1].find_elements_by_class_name('android.widget.RelativeLayout')
    flag = list[0].find_element_by_id('ivImageVip').is_enabled()
    list[0].click()
    sleep(5)
    if flag:
        print("该音频是vip音频")
        if isVip:
            print("用户是vip，进入播放页")
        else:
            print("用户不是vip用户，触发开通弹窗")
            parentPanel = isElement.find_Element(self, 'id', 'parentPanel')
            if parentPanel:
                print("触发了开通提示弹窗")
            else:
                print("未触发")
    else:
        print("该音频不是vip音频，不管用户是否为vip都进入播放页")
    # 判断进入的是否为播放页
    play = isElement.find_Element(self, 'id', 'rl_wiki_play_detail_top')
    if play:
        print("进入播放页")
    else:
        print("未进入播放页")


# 百科首页进入播放页
def toPlay(self, isVip):
    print("从百科首页进入播放页")
    # 判断是否能看到【听讲解】列表
    flag = isElement.find_Element(self, 'id', 'recycler_wiki_home_listen')
    while not flag:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
        flag = isElement.find_Element(self, 'id', 'recycler_wiki_home_listen')
    sleep(5)
    list = self.driver.find_elements_by_id('recycler_wiki_home_listen')[0].find_elements_by_id('rl_item_wiki_home_all')
    sleep(5)
    try:
        sizes=len(list[0])
        aduioVip = list[0].find_element_by_id('ivImageVip').is_displayed()
    except:
        aduioVip=False
    print("aduioVip:", aduioVip)
    list[0].click()
    sleep(5)
    if aduioVip:
        print("该音频是vip音频")
        if isVip:
            print("用户是vip，进入播放页")
        else:
            print("用户不是vip用户，触发开通弹窗")
            parentPanel = isElement.find_Element(self, 'id', 'parentPanel')
            if parentPanel:
                print("触发了开通提示弹窗")
            else:
                print("未触发")
    else:
        print("该音频不是vip音频，不管用户是否为vip都进入播放页")
    # 判断进入的是否为播放页
    play = isElement.find_Element(self, 'id', 'rl_wiki_play_detail_top')
    if play:
        print("进入播放页")
        return True
    else:
        print("未进入播放页")
        return False
