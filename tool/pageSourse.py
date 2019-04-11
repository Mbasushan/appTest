#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def count_list_item_vertical(self):
    driver=self.driver
    items = driver.find_elements_by_xpath(self.path + "/*[@class='android.widget.FrameLayout']") ##获取初始状态时界面上展示的列表项
    num = len(items) ##获取初始状态时界面上展示的列表项的个数作为初始数目
    h = items[0].size.get('height') ##获得单个列表项的高度

    swiped = True ##滑动标识
    while swiped:
        ###滑动前列表各参数
        beforeswipe = driver.page_source
        beforeRv = find_element.found_element_by_class(self,driver)
        beforeRvHeight = beforeRv.size.get('height')
        beforeRvX = beforeRv.location.get('x')
        beforeRvY = beforeRv.location.get('y')
        beforeItems = driver.find_elements_by_xpath(self.path + "/*[@class='android.widget.FrameLayout']")
        beforeItemsSize = len(beforeItems)
        beforeBottomHeight = beforeItems[beforeItemsSize - 1].size.get('height')

        driver.swipe(beforeRvX, beforeRvY + beforeRvHeight * 0.5, beforeRvX,
                     beforeRvY + beforeRvHeight * 0.5 - h * 0.8, 0)

        ###滑动后列表各参数
        afterswipe = driver.page_source
        afterRv = find_element.found_element_by_class(self,driver)
        afterRvHeight = afterRv.size.get('height')
        afterItems = driver.find_elements_by_xpath(self.path + "/*[@class='android.widget.FrameLayout']")
        afterItemsSize = len(afterItems)
        afterBottomHeight = afterItems[afterItemsSize - 1].size.get('height')


        ##首先判断列表是否滑动到尽头
        if afterswipe == beforeswipe:
            swiped = False
        else:
            ##比较滑动前后，列表的高度变化
            if afterRvHeight > beforeRvHeight:
                num = afterItemsSize ##列表高度增加的情况下，滑动后界面上展示的列表项个数即为列表项个数
                swiped = True
            elif afterRvHeight == beforeRvHeight:
                ##列表高度不变时，比较界面中展示的最后一个列表项的高度变化
                if afterBottomHeight < beforeBottomHeight:
                    num = num +1 ##最后一个列表项高度减少时，列表项个数加1
                swiped = True
            elif afterRvHeight < beforeRvHeight:
                swiped = False
    print(num)