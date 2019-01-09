#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: test_verifiedUserAuth.py 
#@time: 2019/01/10 
#@email:1402686685@qq.com
from suds.client import Client

api_url3="http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"

client3=Client(api_url3)

print(client3)


'''如何传递参数值：'''
t={"uid":100004681,"true_name":"彭思源","cre_id":362201199504210418 }#用字典的方式传值

result3=client3.service.verifyUserAuth(t)
print(result3)