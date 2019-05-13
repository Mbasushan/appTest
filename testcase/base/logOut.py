#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import tool.isElement as isElements
import tool.swipe as swipe
from time import sleep
#退出登录
def log_out(self):
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    isElement=isElements.find_Element(self,'name','设置')
    if isElement:
        self.driver.find_element_by_name('设置').click()
    else:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)

    sleep(5)
    self.driver.find_element_by_name('账号安全').click()
    sleep(5)
    self.driver.find_element_by_id('account_tv_exit').click()
    self.driver.find_element_by_id('ask_tv_confirm').click()
    print("退出账号")