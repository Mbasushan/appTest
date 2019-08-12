#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
import tool.isElement as isElement

#微信支付-报名-不使用优惠券
def weixin_pay(self):
    print("微信支付-报名-不使用优惠券")
    self.driver.find_element_by_id('tv_weixin').click()
    self.driver.find_element_by_id('btn_pay').click()
    sleep(5)


#支付宝支付
def alPay(self):
    print("支付宝支付-报名-不使用优惠券")
    self.driver.find_element_by_id('tv_alpay').click()
    self.driver.find_element_by_id('btn_pay').click()
    sleep(5)


#M币支付-余额不足去充值
def m_pay(self,money):
    print("M币支付-报名-不使用优惠券")
    tv_money=self.driver.find_element_by_id('tv_money').text[1:]
    tv_money=tv_money[1:]
    money = money[1:]
    money = money[1:]
    flag = float(tv_money) > float(money)
    if flag:
        print("M币余额不足,点击则触发是否去充值")
        self.driver.find_element_by_id('tv_mcoin').click()
        sleep(3)
        self.driver.find_element_by_id('ask_tv_confirm').click()
        title=self.driver.find_element_by_id('toolbar_tv_title').text
        if title=='我的M币':
            print("跳转到M币充值页")
        else:
            print("未跳转到M币充值页")
            self.driver.quit()
    else:
        self.driver.find_element_by_id('tv_mcoin').click()
    self.driver.find_element_by_id('btn_pay').click()
    sleep(5)
    pay_bottom=isElement.find_Element(self,'id','ll_bottom_pay')
    if pay_bottom:
        print("支付不成功")
    else:
        print("支付成功")

#M币支付-余额不足取消充值
def m_pay_cancle(self,money):
    print("M币支付-报名-不使用优惠券")
    tv_money=self.driver.find_element_by_id('tv_money').text[1:]
    tv_money=tv_money[1:]
    money=money[1:]
    money=money[1:]
    flag=float(tv_money)>float(money)
    if flag:
        print("M币余额不足,点击则触发是否去充值")
        self.driver.find_element_by_id('tv_mcoin').click()
        sleep(3)
        self.driver.find_element_by_id('ask_tv_cancel').click()
        print("M币余额不足，取消充值")
        return False
    else:
        self.driver.find_element_by_id('tv_mcoin').click()
        self.driver.find_element_by_id('btn_pay').click()
        sleep(5)
        pay_bottom=isElement.find_Element(self,'id','ll_bottom_pay')
        if pay_bottom:
            print("支付不成功")
            return False
        else:
            print("支付成功")
            return True

#班费支付
def pay_ban_fei(self):
    #班费支付
    print("选择班费支付")
    self.driver.find_element_by_id('ll_course_pay_ban_fei').click()
    sleep(3)


#使用优惠券支付
def voucher_pay(self):
    print("使用优惠券支付")
    self.driver.find_element_by_id('apply_ll_coupon').click()
    sleep(3)
