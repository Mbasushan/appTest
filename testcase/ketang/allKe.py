#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import tool.isElement as isElement
import testcase.advertisements.advertisement as Ads
import tool.swipe as swipe

#课堂首页，滑动到看到【全部课程】
def allKe(self):
    Ads.test_ketang_ad(self)
    screen = swipe.get_size(self)

    list = isElement.find_Element(self,'id',"recycler_list")
    if list:
        print("看到了全部课程")
        return True
    else:
        size=0

    while size==0:
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 7000)
        list = isElement.find_Element(self, 'id', "recycler_list")
        if list:
            print("看到了全部课程")
            try:
                llParent = self.driver.find_elements_by_id('recycler_list')[0].find_element_by_id("tv_num").is_displayed()
                if llParent:
                    return True
                else:
                    self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
            except:
                print("2")
        else:
            size = 0
    print("看到了全部课程")
    return True