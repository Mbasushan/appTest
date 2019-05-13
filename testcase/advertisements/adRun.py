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
        jsonPath = 'D:/app/testcase/json/setting.json'
        self.driver=connectServer.connect_server(jsonPath)
        sleep(5)

    # 判断是否有引导图
    def test_aa_layout_iv_bg(self):
        LayoutIvBg.test_aa_layout_iv_bg(self)

    # 判断是否有更新版本弹窗---有点击稍后安装
    def test_ask_tv_cancel(self):
        ad.test_ask_tv_cancel(self)

    # 立即安装
    def test_ask_tv_confirm(self):
        ad.test_ask_tv_confirm(self)

    # 判断是否有好评弹窗
    def test_tvcnacle(self):
        praises.test_tvcnacle(self)

    # 点击【暖心好评】
    def test_praise(self):
        praises.test_praise(self)

    # 点击【差评吐槽】
    def test_complaints(self):
        praises.test_complaints(self)

    # 判断是否有首页广告
    def test_is_ad(self):
        ad.test_is_ad(self)

    # app轮播图
    def test_home_slideshow(self):
        ad.test_home_slideshow(self)

    # app首页广告
    def test_home_banner(self):
        ad.test_home_banner(self)

    # 大咖开通页背景广告位
    def test_wiki_audio_vip(self):
        ad.test_wiki_audio_vip(self)

    # app课堂首页广告
    def test_ketang_ad(self):
        ad.test_ketang_ad(self)

    # 有句名言广告位
    def test_afamous_ad(self):
        afamousAd.test_afamous_ad(self)

    # 每日一词广告
    def test_dailyword_ad(self):
        afamousAd.test_dailyword_ad(self)

    # 搜索里的广告
    def test_search_ad(self):
        searchAd.test_search_ad(self)

    # 闪屏广告点击跳转
    def test_splash_tv_skip(self):
        splashAd.test_splash_tv_skip(self)

    # 不点击跳过闪屏广告，倒计时结束
    def test_noSkip(self):
        splashAd.test_noSkip(self)

    # 点击闪屏广告
    def test_ad(self):
        splashAd.test_ad(self)


    def tearDown(self):
        self.driver.quit()
