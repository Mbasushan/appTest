#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
import testcase.vipAduio.entrance as entrance
import testcase.vipAduio.aduio as aduios
import testcase.vipAduio.play as plays
import testcase.advertisements.advertisement as Ads
import tool.isElement as isElements
import testcase.base.isVip as Isvip
import tool.connectServer as connectServer
import testcase.advertisements.adBase as adBase
import testcase.advertisements.layoutIvBg as layoutIvBg

class Vip(unittest.TestCase):

    def setUp(self):
        self.driver=connectServer.connect_server()
        sleep(5)


    def test_vip_homePage(self):
        """app首页【大咖讲百科】入口"""
        adBase.adBase(self)
        entrance.test_vip_homePage(self)

    def test_vip_menuBar(self):
        """app首页菜单栏【百科】"""
        adBase.adBase(self)
        entrance.test_vip_menuBar(self)

    def test_wiki_search(self):
        """百科首页-搜索百科条目框"""
        adBase.adBase(self)
        entrance.test_vip_menuBar(self)
        sleep(3)
        aduios.test_wiki_search(self)

    def test_open_vip(self):
        """进入大咖开通vip页面"""
        adBase.adBase(self)
        entrance.test_vip_menuBar(self)
        sleep(3)
        aduios.test_open_vip(self)

    def base(self):
        #判断是否有隐私政策弹窗，有则同意
        adBase.adBase(self)
        isVip = Isvip.isVip(self)
        if isVip == "已失效" or isVip == "未开通":
            isvip = False
        else:
            isvip = True
        print("isvip；", isvip)
        entrance.test_vip_menuBar(self)
        return isvip

    def test_scene_list(self):
        """大咖场景列表-播放页"""
        isVip=Vip.base(self)
        sleep(3)
        # 进入大咖场景详情页
        aduios.test_scene_details(self, 1)
        #进入播放页
        aduios.test_scene_list_to_play(self,isVip)

    def test_wiki_scene_list(self):
        """百科首页大咖场景列表-播放页"""
        isVip = Vip.base(self)
        sleep(3)
        # 进入大咖场景列表
        aduios.test_scene_list(self)
        # 进入大咖场景详情页
        aduios.test_scene_details(self, 2)
        #进入播放页
        aduios.test_scene_list_to_play(self,isVip)

    def test_play_manuscripts(self):
        """大咖播放页-操作页、文稿页面互相切换"""
        # 从百科首页【听讲解】进入播放页
        Vip.test_wiki_home_toPlay(self)
        sleep(5)
        self.driver.find_element_by_id('iv_wiki_play_detail_play').click()
        #操作页、文稿页面互相切换
        plays.play_manuscripts(self)

    def test_wiki_home_toPlay(self):
        """从百科首页的【听讲解】进入播放页"""
        isVip = Vip.base(self)
        sleep(3)
        aduios.toPlay(self,isVip)

    def test_wiki_teacher_play(self):
        """大咖主页进入播放页"""
        isVip = Vip.base(self)
        Vip.test_wiki_home_toPlay(self)
        self.driver.find_element_by_id('iv_wiki_play_detail_play').click()
        sleep(5)
        plays.fragment_circle_img(self)
        sleep(5)
        aduios.wiki_teacher_list(self,isVip)

    def test_play_prev_next(self):
        """大咖播放页-上下一首切换"""
        #进入播放页
        isVip = Vip.base(self)
        aduios.toPlay(self, isVip)
        sleep(5)
        self.driver.find_element_by_id('iv_wiki_play_detail_play').click()
        sleep(5)
        #上下一首切换
        plays.play_prev_next(self)


    def test_play_download(self):
        """大咖播放页-离线下载-马上开通"""
        #进入播放页
        isvip = Vip.base(self)
        isPlay = aduios.toPlay(self, isvip)
        sleep(5)
        self.driver.find_element_by_id('iv_wiki_play_detail_play').click()
        sleep(5)
        # 离线下载
        plays.play_download(self, isvip,0)

    def test_play_download_cancel(self):
        """大咖播放页-离线下载-马上开通"""
        #进入播放页
        isvip = Vip.base(self)
        isPlay = aduios.toPlay(self, isvip)
        sleep(5)
        self.driver.find_element_by_id('iv_wiki_play_detail_play').click()
        sleep(5)
        # 离线下载
        plays.play_download(self, isvip, 1)

    def test_play_list(self):
        """大咖播放页-播放列表-切换音频"""
        #进入播放页
        isvip = Vip.base(self)
        isPlay = aduios.toPlay(self, isvip)
        sleep(5)
        self.driver.find_element_by_id('iv_wiki_play_detail_play').click()
        sleep(5)
        plays.play_list(self,isvip)

    def test_play_list_off(self):
        """大咖播放页-播放列表-关闭播放列表弹窗"""
        # 进入播放页
        isvip = Vip.base(self)
        isPlay = aduios.toPlay(self, isvip)
        sleep(5)
        self.driver.find_element_by_id('iv_wiki_play_detail_play').click()
        sleep(5)
        plays.play_list_off(self)

    def test_play_setTime(self):
        """大咖播放页-切换定时选择"""
        # 进入播放页
        isvip = Vip.base(self)
        isPlay = aduios.toPlay(self, isvip)
        sleep(5)
        self.driver.find_element_by_id('iv_wiki_play_detail_play').click()
        sleep(5)
        plays.play_set_time(self)


    def tearDown(self):
        self.driver.quit()