#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
import testcase.advertisements.adBase as adBase
import tool.connectServer as connectServer
import testcase.base.login as logins
import testcase.base.isLogin as isLogins
import tool.swipe as swipe


class Login(unittest.TestCase):

    def setUp(self):
        self.driver=connectServer.connect_server()
        sleep(5)

    def login_phone(self):
        """手机号登录"""
        adBase.adBase(self)
        # 判断是否登录
        isLogin = isLogins.isLogin(self)
        if isLogin:
            print("已登录")
            logins.log_out(self)
            #下滑页面
            screen = swipe.get_size(self)
            self.driver.swipe(screen[0] * 0.5, screen[1] * 0.25, screen[0] * 0.5, screen[1] * 0.75, 6000)
        else:
            print("未登录,登录账号")
        self.driver.find_element_by_name("点击登录").click()
        sleep(5)
        logins.login_phone(self)

    def login_username(self):
        """用户名登录"""
        adBase.adBase(self)
        # 判断是否登录
        isLogin = isLogins.isLogin(self)
        if isLogin:
            print("已登录")
            logins.log_out(self)
            # 下滑页面
            screen = swipe.get_size(self)
            self.driver.swipe(screen[0] * 0.5, screen[1] * 0.25, screen[0] * 0.5, screen[1] * 0.75, 6000)
        else:
            print("未登录,登录账号")
        self.driver.find_element_by_name("点击登录").click()
        sleep(5)
        logins.login_userName(self)

    def login_out(self):
        """退出登录"""
        logins.log_out(self)

    def tearDown(self):
        self.driver.quit()