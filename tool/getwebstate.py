#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 可以针对当前网络状态封装

def getwebstate(self):
    info = {0: "NO_CONNECTION",

            1: "AIRPLANE_MODE",

            2: "WIFI_ONLY",

            4: "DATA_ONLY",

            6: "ALL_NETWORK_ON"}

    state = self.driver.network_connection

    return info.get(state)
