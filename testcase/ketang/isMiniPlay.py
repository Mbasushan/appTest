#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import tool.isElement as isElements

def isMiniPlay(self):
    #判断是否有全局播放器
    flag=isElements.find_Element(self,'id','ll_mini_parent')
    if flag:
        return True
    else:
        return False

