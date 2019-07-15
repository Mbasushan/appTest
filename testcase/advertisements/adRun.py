#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
import testcase.advertisements.advertisement as ad
import tool.connectServer as connectServer
import testcase.advertisements.splashAd as splashAd
import testcase.advertisements.afamousAd as afamousAd
import testcase.advertisements.layoutIvBg as LayoutIvBg
import testcase.advertisements.praises as praises
import testcase.advertisements.searchAd as searchAd


class Ad(unittest.TestCase):

    def setUp(self):
        self.driver=connectServer.connect_server()
        sleep(5)

    # 判断是否有引导图
    def test_aa_layout_iv_bg(self):
        """判断是否有引导图"""
        LayoutIvBg.test_aa_layout_iv_bg(self)

    # 判断是否有更新版本弹窗---有点击稍后安装
    def test_ask_tv_cancel(self):
        """稍后安装"""
        ad.test_ask_tv_cancel(self)

    # 立即安装
    def test_ask_tv_confirm(self):
        """立即安装"""
        ad.test_ask_tv_confirm(self)

    # 点击【暖心好评】
    def test_praise(self):
        """暖心好评"""
        praises.test_praise(self)

    # 点击【差评吐槽】
    def test_complaints(self):
        """差评吐槽"""
        praises.test_complaints(self)

    # 判断是否有首页广告
    def test_is_ad(self):
        """首页广告"""
        ad.test_is_ad(self)

    # app轮播图
    def test_home_slideshow(self):
        """app轮播图"""
        splashAd.test_ad(self)
        # 判断是否有首页广告
        ad.test_is_ad(self)
        ad.test_home_slideshow(self)

    # app首页横幅广告
    def test_home_banner(self):
        """app首页横幅广告"""
        # 判断是否有闪屏广告
        splashAd.test_ad(self)
        # 判断是否有首页广告
        ad.test_is_ad(self)
        ad.test_home_banner(self)

    # 大咖开通页背景广告位
    def test_wiki_audio_vip(self):
        """大咖开通页背景广告位"""
        # 判断是否有闪屏广告
        splashAd.test_ad(self)
        # 判断是否有首页广告
        ad.test_is_ad(self)
        ad.test_wiki_audio_vip(self)

    # app课堂首页广告
    def test_ketang_ad(self):
        """app课堂首页广告"""
        # 判断是否有闪屏广告
        splashAd.test_ad(self)
        # 判断是否有首页广告
        ad.test_is_ad(self)
        # 切换到课堂
        self.driver.find_element_by_name('课堂').click()
        sleep(5)
        ad.test_ketang_ad(self)

    # 有句名言广告位
    def test_afamous_ad(self):
        """有句名言广告位"""
        afamousAd.test_afamous_ad(self)

    # 每日一词广告
    def test_dailyword_ad(self):
        """每日一词广告"""
        afamousAd.test_dailyword_ad(self)

    # 搜索里的广告
    def test_search_ad(self):
        """搜索里的广告"""
        searchAd.test_search_ad(self)

    # 闪屏广告点击跳转
    def test_splash_tv_skip(self):
        """闪屏广告点击跳转"""
        splashAd.test_splash_tv_skip(self)

    # 不点击跳过闪屏广告，倒计时结束
    def test_noSkip(self):
        """不点击跳过闪屏广告，倒计时结束"""
        splashAd.test_noSkip(self)

    # 点击闪屏广告
    #def test_ad(self):
        #splashAd.test_ad(self)


    def tearDown(self):
        self.driver.quit()
