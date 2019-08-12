#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 导入三个库文件
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def find_toast(self,message):
    #获取toast  message为需要抓到的toast文本   
    print("message:",message)
    toast_element = (By.XPATH, "//*[contains(@text, " + "'" + message + "'" + ")]")
    element= WebDriverWait(self.driver,0.5).until(expected_conditions.presence_of_element_located((By.XPATH, toast_element)))
    if element.text== message:
        return True
    else:
        return False
