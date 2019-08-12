#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
import tool.isElement as isElement
import tool.swipe as swipe
import testcase.advertisements.advertisement as ad
import testcase.base.isVip as vip
import testcase.ketang.isBuyKe as buyKe
import tool.back as back
import testcase.base.isLogin as IsLogin
import testcase.ketang.isBuyKe as isBuyKe
import testcase.base.login as login
import testcase.pay.payType as payType
import testcase.base.Mbi as mbi
import testcase.ketang.supplementary_info as sInfo

#报名
def test_buyKe(self):
    """进入课程详情页，判断用户是否报名,未报名则报名"""
    # 判断是否登录
    isLogin = IsLogin.isLogin(self)
    if not isLogin:
        self.driver.find_element_by_id('tv_my_fragment_login_no_login').click()
        sleep(5)
        login.login_userName(self)
        #判断是否绑定手机
        bind=self.driver.find_element_by_xpath("//android.view.View[@content-desc='绑定 绑定']").is_enabled()
        print("bind:",bind)
        if bind:
            back.ivBack(self)
    # 当前账号的M币金额
    money = mbi.Mbi(self)
    #返回到【我的】页面
    back.ivBack(self)
    sleep(5)
    #切换到课堂
    self.driver.find_elements_by_id('tv_tab_title')[3].click()
    #判断是否有课堂广告
    ad.test_ketang_ad(self)
    sleep(5)
    screen = swipe.get_size(self)
    self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
    list = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_package")[0].find_elements_by_class_name("android.widget.LinearLayout")
    list[0].click()
    sleep(5)
    #判断是否进入的是微信绑定页，如果是点击【取消】
    flag=isElement.find_Element(self,'id','tv_popu_course_bind_wx_bind')
    if flag:
        self.driver.find_element_by_id('tv_popu_course_bind_wx_cancel').click()
    sleep(5)
    print("进入课程详情页，是否有报名按钮")
    keTitle=self.driver.find_element_by_id('tv_ke_title').text
    print("keTitle:",keTitle)
    tvBuy = isElement.find_Element(self, 'id', 'tv_buy')
    if tvBuy:
        print("存在报名按钮")
        self.driver.find_element_by_id("tv_buy").click()
        sleep(5)
        #使用M币支付报名
        flag=payType.m_pay_cancle(self,money)
        if not flag:
            return
        else:
            back.ivBack(self)
            #判断是否有补充弹窗，有则提交数据
            contet=isElement.find_Element(self,'id','layoutContent')
            if contet:
                print("信息补充弹窗开启")
                #填写信息点击【保存】
                sInfo.filled(self)
            sleep(5)
            back.ivBack(self)
            isBuyKe.is_buy_ke(self, keTitle)
    else:
        print("不存在报名按钮")
        back.ivBack(self)
        isBuyKe.is_buy_ke(self, keTitle)


#vip折扣价报名
def vip_buy_packPage(self):
    # 判断用户是否为vip
    vipText = vip.isKeVip(self)
    ll_taps = self.driver.find_elements_by_id('ll_tap')
    ll_taps[3].click()
    # 判断是否有课堂广告
    ad.test_ketang_ad(self)
    ivFold = isElement.find_Element(self, 'id', 'ivFold')
    # flag=isElement.find_Element(self,"id",'com.mbalib.android.wiki:id/recycler_package')
    if not ivFold:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
    # 点击系统班的第一个课程包
    list = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_package")[
        0].find_elements_by_class_name("android.widget.LinearLayout")
    self.driver.find_element_by_id('ivFold').click()
    flowLayout = list[0].find_elements_by_id('textview')
    siz = len(flowLayout)
    index = 0
    flowText = flowLayout[index].text
    while flowText == 'VIP折扣价':
        index = +1
        if index < siz:
            flowText = flowLayout[index].text
        else:
            print("未有VIP折扣价")
            return

    list[0].click()
    sleep(5)
    #该课程的价格
    tv_prive=self.driver.find_element_by_id('tv_prive').text
    #判断该课程是否已报名
    isbuy=isElement.find_Element(self,'id','ll_bottom_pay')
    if isbuy:
        print("该课程包还未报名")
        if vipText=="vip":
            isFree = isElement.find_Element(self, 'id', 'll_ke_vip_listen')
            if isFree:
                print("该课程包是vip免费听")
                return
            else:
                print("该课程包是vip折扣")
                # 点击报名
                self.driver.find_element_by_id('tv_buy').click()
                sleep(5)
                # 实际支付金额为tv_prive
                tv_money = self.driver.find_element_by_id('tv_money').text[1:]
                money = tv_money[1:]
                tv_prive=float(tv_prive)*0.8
                tv_prive = ("%.2f" % tv_prive)
                print(tv_prive)
                if money == tv_prive:
                    print("vip折扣")
                    # 选择M币支付
                    payType.m_pay_cancle(self, money)
                else:
                    print("金额不符合")
                    return
        else:
            print("该用户不是vip用户")
            # 点击报名
            self.driver.find_element_by_id('tv_buy').click()
            sleep(5)
            #实际支付金额为tv_prive
            tv_money=self.driver.find_element_by_id('tv_money').text[1:]
            money=tv_money[1:]
            if money == tv_prive:
                print("未打折扣")
                #选择M币支付
                payType.m_pay_cancle(self,money)
            else:
                print("金额不符合")
                return
    else:
        print("该课程包已报名")


#vip免费听-课程包
def vip_free_packPage(self):
    #判断用户是否为vip
    vipText=vip.isKeVip(self)
    ll_taps=self.driver.find_elements_by_id('ll_tap')
    ll_taps[3].click()
    ivFold = isElement.find_Element(self, 'id', 'ivFold')
    #flag=isElement.find_Element(self,"id",'com.mbalib.android.wiki:id/recycler_package')
    if not ivFold:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
    #点击系统班的第一个课程包
    list = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_package")[0].find_elements_by_class_name("android.widget.LinearLayout")
    self.driver.find_element_by_id('ivFold').click()
    flowLayout=list[0].find_elements_by_id('textview')
    siz=len(flowLayout)
    index=0
    flowText = flowLayout[index].text
    while flowText =='VIP免费听':
        index=+1
        if index <siz:
            flowText=flowLayout[index].text
        else:
            print("未有vip免费听")
            return

    list[0].click()
    sleep(5)
    vipListen=isElement.find_Element(self,'id','ll_ke_vip_listen')
    if vipListen:
        print("该课程未报名")
        #判断用户是否为vip
        if vipText=='vip':
            payBottom=self.driver.find_elements_by_id('ll_bottom_pay')
            if len(payBottom)==1:
                print("用户是vip用户")
                self.driver.find_element_by_id('ll_ke_vip_listen').click()
                sleep(5)
                flag = isElement.find_Element(self, 'id', 'll_ke_vip_listen')
                if not flag:
                    print("vip免费听激活课程成功")
                else:
                    print("vip免费听激活课程失败")
                    return
                #我的课程中显示出该课程，有【vip免费听】标签
                title=self.driver.find_element_by_id('tv_ke_title').text
                back.ivBack(self)
                isbuyKe=buyKe.is_buy_ke(self,title)
                if isbuyKe:
                    print("vip免费听有加入我的课程列表")
                    list1 = self.driver.find_elements_by_id('com.mbalib.android.wiki:id/layout_recycler')[0].find_elements_by_class_name('android.widget.RelativeLayout')
                    tv_titles = self.driver.find_elements_by_id('com.mbalib.android.wiki:id/layout_recycler')[0].find_elements_by_id('com.mbalib.android.wiki:id/tv_title')
                    size = len(list1)
                    print("list长度:", size)
                    for index in range(len(tv_titles)):
                        if title == tv_titles[index].text:
                            print("title:",tv_titles[index].text)
                            #判断是否有vip免费听按钮
                            vipLogo=isElement.find_Element(self,'id','iv_item_my_course_vip')
                            if vipLogo:
                                print("有显示【vip免费听】标签")
                            else:
                                print("未显示【vip免费听】标签")
                else:
                    print("vip免费听未加入我的课程列表")
            else:
                print("用户不是vip用户")
                self.driver.find_element_by_id('ll_ke_vip_listen').click()
                sleep(5)
                tvTitle=self.driver.find_element_by_id('tvTitle').click()
                if tvTitle=='课堂VIP ':
                    print("点击vip免费听，跳转到课堂vip开通页")
                    return
        else:
            print("用户不是vip用户")

    else:
        print("该课程已报名")

#vip免费听-课程
def vip_free_course(self):
    # 判断用户是否为vip
    vipText = vip.isKeVip(self)
    ll_taps = self.driver.find_elements_by_id('ll_tap')
    ll_taps[3].click()
    # 判断是否有课堂广告
    ad.test_ketang_ad(self)
    flag=isElement.find_Element(self, "id", 'com.mbalib.android.wiki:id/recycler_list')
    while not flag:
        screen = swipe.get_size(self)
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, 6000)
        flag = isElement.find_Element(self, "id", 'com.mbalib.android.wiki:id/recycler_list')
    #点击全部课程的第一个课程
    list = self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_list")[0].find_elements_by_class_name("android.widget.LinearLayout")
    self.driver.find_element_by_id('ivFold').click()
    flowLayout=list[0].find_elements_by_id('textview')
    siz=len(flowLayout)
    index=0
    flowText = flowLayout[index].text
    while flowText !='VIP免费听':
        index=index+1
        if index <siz:
            flowText=flowLayout[index].text
        else:
            print("未有vip免费听")
            return
    self.driver.find_element_by_id('ivFold').click()
    self.driver.find_elements_by_id("com.mbalib.android.wiki:id/recycler_list")[0].find_elements_by_class_name("android.widget.LinearLayout")[0].click()
    sleep(5)
    vipListen=isElement.find_Element(self,'id','ll_ke_vip_listen')
    if vipListen:
        print("该课程未报名")
        #判断用户是否为vip
        if vipText=='vip':
            payBottom=self.driver.find_elements_by_id('ll_bottom_pay')
            if len(payBottom)==1:
                print("用户是vip用户")
                self.driver.find_element_by_id('ll_ke_vip_listen').click()
                sleep(5)
                flag = isElement.find_Element(self, 'id', 'll_ke_vip_listen')
                if not flag:
                    print("vip免费听激活课程成功")
                else:
                    print("vip免费听激活课程失败")
                    return
                #我的课程中显示出该课程，有【vip免费听】标签
                title=self.driver.find_element_by_id('tv_ke_title').text
                back.ivBack(self)
                isbuyKe=buyKe.is_buy_ke(self,title)
                if isbuyKe:
                    print("vip免费听有加入我的课程列表")
                    list1 = self.driver.find_elements_by_id('com.mbalib.android.wiki:id/layout_recycler')[0].find_elements_by_class_name('android.widget.RelativeLayout')
                    tv_titles = self.driver.find_elements_by_id('com.mbalib.android.wiki:id/layout_recycler')[0].find_elements_by_id('com.mbalib.android.wiki:id/tv_title')
                    for index in range(len(tv_titles)):
                        if title == tv_titles[index].text:
                            print("title:",tv_titles[index].text)
                            #判断是否有vip免费听按钮
                            vipLogo=isElement.find_Element(self,'id','iv_item_my_course_vip')
                            if vipLogo:
                                print("有显示【vip免费听】标签")
                            else:
                                print("未显示【vip免费听】标签")
                else:
                    print("vip免费听未加入我的课程列表")
            else:
                print("用户不是vip用户")
                self.driver.find_element_by_id('ll_ke_vip_listen').click()
                sleep(5)
                tvTitle=self.driver.find_element_by_id('tvTitle').click()
                if tvTitle=='课堂VIP ':
                    print("点击vip免费听，跳转到课堂vip开通页")
                    return
        else:
            print("用户不是vip用户")

    else:
        buy=isElement.find_Element(self,'id','tv_buy')
        if buy:
            print("该课程未报名且该课程不是vip免费听课程")
        else:
            print("该课程已报名")
