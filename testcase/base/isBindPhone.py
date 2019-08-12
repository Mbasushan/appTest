#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep

#判断是否绑定手机号
def isBindPhone(self):
    self.driver.find_element_by_id('iv_my_fragment_setting').click()
    sleep(3)
    self.driver.find_element_by_name('账号安全').click()
    sleep(3)
    text=self.driver.find_elements_by_id('account_item_mobile')[0].find_element_by_id('item_iv_messageText').text
    if text=='未绑定':
        return False
    else:
        return True

#判断是否绑定了微信
def isBindWeixin(self):
    print("判断用户是否绑定了微信")
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    sleep(5)
    self.driver.find_element_by_id('iv_my_fragment_setting').click()
    sleep(5)
    self.driver.find_element_by_name('账号安全').click()
    text=self.driver.find_elements_by_id('account_item_wechat')[0].find_element_by_id('item_iv_messageText').text
    if text=='未绑定':
        return False
    else:
        return True

#判断是否是【绑定微信】提醒页面