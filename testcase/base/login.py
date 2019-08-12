#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#手机号登录
from time import sleep

def login_phone(self):
    print("手机号登录")
    # 输入手机号码
    self.driver.find_element_by_xpath("//android.webkit.WebView[@content-desc=\"帐户登录 - MBA智库帐户\"]/android.widget.EditText").click()
    self.driver.find_element_by_xpath("//android.webkit.WebView[@content-desc=\"帐户登录 - MBA智库帐户\"]/android.widget.EditText").send_keys('15960445986')
    # 输入密码
    self.driver.find_element_by_xpath("//android.webkit.WebView[@content-desc=\"帐户登录 - MBA智库帐户\"]/android.view.View[4]/android.widget.EditText").click()
    self.driver.find_element_by_xpath("//android.webkit.WebView[@content-desc=\"帐户登录 - MBA智库帐户\"]/android.view.View[4]/android.widget.EditText").send_keys('123456')
    self.driver.hide_keyboard()
    self.driver.find_element_by_xpath("(//android.view.View[@content-desc=\"登录 登录\"])[2]").click()
    sleep(5)

def login_userName(self):
     print("用户名登录")
     #切换成用户名登录
     self.driver.find_element_by_accessibility_id("手机号登录").click()
     sleep(3)
     self.driver.find_element_by_accessibility_id("用户名登录").click()
     #输入用户名
     self.driver.find_element_by_xpath("//android.webkit.WebView[@content-desc=\"帐户登录 - MBA智库帐户\"]/android.widget.EditText").click()
     self.driver.find_element_by_xpath("//android.webkit.WebView[@content-desc=\"帐户登录 - MBA智库帐户\"]/android.widget.EditText").send_keys('Sxs1')
     #输入密码
     self.driver.find_element_by_xpath("//android.webkit.WebView[@content-desc=\"帐户登录 - MBA智库帐户\"]/android.view.View[4]/android.widget.EditText").click()
     self.driver.find_element_by_xpath("//android.webkit.WebView[@content-desc=\"帐户登录 - MBA智库帐户\"]/android.view.View[4]/android.widget.EditText").send_keys('123456')
     self.driver.hide_keyboard()
     self.driver.find_element_by_xpath("(//android.view.View[@content-desc=\"登录 登录\"])[2]").click()
     sleep(5)

#退出登录
def log_out(self):
    # 切换到我的
    self.driver.find_element_by_id('iv_my_fragment_setting').click()
    sleep(5)
    self.driver.find_element_by_id('setting_item_safe').click()
    sleep(5)
    self.driver.find_element_by_id('account_tv_exit').click()
    self.driver.find_element_by_id('ask_tv_confirm').click()
    print("退出账号")
