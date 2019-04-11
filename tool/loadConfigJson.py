#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json

#解析json文件
def load_config_json(path):
    print('load config json ' + path)
    with open(path,'r') as f:
        a = f.read()
    try:
        return json.loads(a)
    except Exception as e:
        return None
