#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import unittest
from time import sleep
import tool.connectServer as connectServer
import testcase.download.downloaded as downloaded
import testcase.download.downloadKe as downloadKe
import testcase.advertisements.advertisement as ad

class DownLoadRun(unittest.TestCase):

    def setUp(self):
        self.driver=connectServer.connect_server()
        sleep(5)

    #下载课程
    def test_a_download_ke(self):
        """从【我的课程】进入课程介绍页下载课程"""
        ad.splashAd.test_noSkip(self)
        ad.test_is_ad(self)
        downloadKe.download_ke(self)

    #未登录进入【已下载】
    def test_noLogin_download(self):
        """未登录进入【已下载】"""
        ad.splashAd.test_noSkip(self)
        ad.test_is_ad(self)
        downloaded.noLogin_download(self)

    #已登录进入【已下载】
    def test_login_download(self):
        """播放已下载音频-有网络"""
        ad.splashAd.test_noSkip(self)
        ad.test_is_ad(self)
        downloaded.login_download(self)

    # 判断当前在播放的视音频是否在【已下载】列表中
    def test_play_is_downloaded(self):
        """判断当前在播放的视音频是否在【已下载】列表中"""
        ad.splashAd.test_noSkip(self)
        ad.test_is_ad(self)
        downloaded.play_is_downloaded(self)

    # 未报名，点击下载，触发提示弹窗,点击【马上报名】
    def test_no_apply(self):
        """未报名，点击下载，触发提示弹窗,点击【马上报名】"""
        ad.splashAd.test_noSkip(self)
        ad.test_is_ad(self)
        downloadKe.no_apply(self)

    #未报名，点击下载，触发提示弹窗,点击【取消】
    def test_no_apply_cancle(self):
        """未报名，点击下载，触发提示弹窗,点击【取消】"""
        ad.splashAd.test_noSkip(self)
        ad.test_is_ad(self)
        downloadKe.no_apply_cancle(self)

    #删除已下载
    def test_delete_downloaded(self):
        """长按删除已下载数据"""
        ad.splashAd.test_noSkip(self)
        ad.test_is_ad(self)
        downloaded.delete_downloaded(self)

    def test_no_network_play(self):
        """无网络播放离线下载"""
        ad.splashAd.test_noSkip(self)
        ad.test_is_ad(self)
        downloaded.no_network_play(self)

    def tearDown(self):
        self.driver.quit()