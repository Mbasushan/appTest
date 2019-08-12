#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
import tool.isElement as isElement
import tool.swipe as swipe

#获取M币余额
def Mbi(self):
    #self.driver.find_elements_by_id('tv_tab_title')[4].click()
    name=isElement.find_Element(self,'id','tv_my_fragment_M_bi')
    while not name:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
        name = isElement.find_Element(self, 'name', 'M币')
    self.driver.find_element_by_id('tv_my_fragment_M_bi').click()
    sleep(5)
    mcoin=self.driver.find_element_by_id('tv_mcoin').text
    #去掉符号
    money=mcoin.strip('￥')
    return money