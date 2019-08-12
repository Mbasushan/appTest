#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
import tool.isElement as isElements

def isLogin(self):
    print("判断用户是否登录")
    # 切换到我的
    self.driver.find_element_by_name('我的').click()
    isLogin=isElements.find_Element(self,'id','tv_my_fragment_login_no_login')
    if isLogin:
        print("用户未登录")
        return False
    else:
        return True

