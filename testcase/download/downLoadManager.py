#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
#下载管理

def downLoad_manager(self):
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    sleep(3)
    # 选择【下载】
    self.driver.find_element_by_name('下载').click()
    sleep(3)
    print("进入下载管理页面")
    self.driver.find_element_by_id('toolbar_setting1').click()