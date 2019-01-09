#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: test_sendMCode.py
#@time: 2019/01/10 
#@email:1402686685@qq.com
from suds.client import Client
api_url1="http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
client1=Client(api_url1)
print(client1)


'''如何传递参数值：'''
t={"client_ip":"120.24.235.105","mobile": 18827915076,"tmpl_id":1}#用字典的方式传值

result1=client1.service.sendMCode(t)
print(result1)