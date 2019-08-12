#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import testcase.advertisements.privacyPolicy as privacyPolicy
import testcase.advertisements.splashAd as splashAd
import testcase.advertisements.advertisement as advertisement
import testcase.advertisements.layoutIvBg as layoutIvBg
import tool.isElement as isElements
from time import sleep

def adBase(self):
    print("启动APP后到首页的广告及所有弹窗判断")
    # 隐私政策
    privacyPolicy.privacy_policy_agree(self)
    sleep(5)
    # 闪屏广告
    splashAd.test_noSkip(self)
    sleep(3)
    # 引导图
    layoutIvBg.test_layout_iv_bg(self)
    sleep(5)
    #更新提醒
    advertisement.test_ask_tv_cancel(self)
    sleep(5)

    # 账号安全提示
    flag = isElements.find_Element(self, 'id', 'tv_sure')
    if flag:
        print("账号安全提示-登录限制弹窗显示")
        self.driver.find_element_by_id('tv_sure').click()
        sleep(5)
        self.driver.find_elements_by_id('tv_tab_title')[3].click()
    sleep(5)
    # 首页弹窗广告
    advertisement.test_is_ad(self)
    sleep(5)