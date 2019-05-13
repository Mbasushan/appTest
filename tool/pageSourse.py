from time import sleep
import tool.swipe as swipe


# 判断是否滑动到底部：
def test_pageSourse(self):
    # 第一次滑动前，获取最后一个元素
    infolists1 = self.driver.find_elements_by_id('tv_title')
    originalinfo = infolists1[(len(infolists1) - 1)].text
    print(originalinfo)
    sleep(5)
    isSwipe = True
    # 滑动
    while isSwipe:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 1000)
        infolists2 = self.driver.find_elements_by_id('tv_title')
        currentinfo= infolists2[(len(infolists1) - 1)].text
        if currentinfo!=originalinfo:
            originalinfo= currentinfo
            self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 1000)
        else:
            isSwipe = False
            print(currentinfo)
            print("This is the buttom")
