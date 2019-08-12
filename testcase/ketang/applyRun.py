#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
import testcase.advertisements.advertisement as Ads
import testcase.advertisements.adBase as adBase
import tool.connectServer as connectServer
import testcase.ketang.kePlayTime as kePlay
import testcase.ketang.signUp as signUp

class ApplayKe(unittest.TestCase):

    def setUp(self):
        self.driver=connectServer.connect_server()
        sleep(5)

    #报名
    def test_test_buyKe(self):
        """进入课程包详情页，判断用户是否报名,未报名则报名"""
        adBase.adBase(self)
        signUp.test_buyKe(self)



    def test_kePlay_packPage(self):
        """课程包选择课程进入播放页"""
        adBase.adBase(self)
        # 切换到课堂
        self.driver.find_element_by_name('课堂').click()
        Ads.test_ketang_ad(self)
        kePlay.ke_packPage(self)

    def test_ke_course(self):
        """从课程进入播放页"""
        adBase.adBase(self)
        kePlay.ke_course(self)

    def test_ke_course_audition_noBuy(self):
        """未报名点击章节试听"""
        adBase.adBase(self)
        # 切换到课堂
        self.driver.find_element_by_name('课堂').click()
        Ads.test_ketang_ad(self)
        kePlay.ke_course_audition_noBuy(self)

    def test_ke_course_auditionBut_noBuy(self):
        """未报名，点击【试听】按钮"""
        adBase.adBase(self)
        # 切换到课堂
        self.driver.find_element_by_name('课堂').click()
        Ads.test_ketang_ad(self)
        kePlay.ke_course_auditionBut_noBuy(self)

    def test_ke_course_NoListenButton(self):
        """未报名，点击未有试听章节"""
        adBase.adBase(self)
        # 切换到课堂
        self.driver.find_element_by_name('课堂').click()
        Ads.test_ketang_ad(self)
        kePlay.ke_course_NoListenButton(self)

    def test_ke_course_play_myCourse(self):
        """从【我的课程】进入课程详情页进行播放"""
        adBase.adBase(self)
        # 切换到课堂
        self.driver.find_element_by_name('课堂').click()
        Ads.test_ketang_ad(self)
        kePlay.ke_course_play_myCourse(self)

    def test_miniPlay_play(self):
        """暂停/播放全局播放器"""
        adBase.adBase(self)
        kePlay.miniPlay_play(self)

    def test_close_miniPlay(self):
        """关闭全局播放器"""
        adBase.adBase(self)
        kePlay.close_miniPlay(self)

    def test_miniPlay_keCourse(self):
        """从【全局播放器】进入播放页"""
        Ads.test_is_ad(self)
        kePlay.miniPlay_keCourse(self)

    def test_vip_free_packPage(self):
        """从【全局播放器】进入播放页"""
        adBase.adBase(self)
        signUp.vip_free_packPage(self)

    def test_signUp_vipFree(self):
        """课程包vip免费听"""
        adBase.adBase(self)
        self.driver.find_element_by_name('课堂').click()
        Ads.test_ketang_ad(self)
        signUp.vip_free_packPage(self)

    def test_signUp_vipFreeCourse(self):
        """课程vip免费听"""
        adBase.adBase(self)
        self.driver.find_element_by_name('课堂').click()
        Ads.test_ketang_ad(self)
        signUp.vip_free_course(self)

    #def test_rlPlayTime(self):
     #   """从【全局播放器】进入播放页"""
      #  Ads.test_is_ad(self)
       # players.rlPlayTime(self)

    def tearDown(self):
        self.driver.quit()