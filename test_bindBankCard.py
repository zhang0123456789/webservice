#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: test_bindBankCard.py 
#@time: 2019/01/10 
#@email:1402686685@qq.com
from suds.client import Client

api_url4="http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"

client4=Client(api_url4)

print(client4)


'''如何传递参数值：'''
t={"uid":100004681,"pay_pwd":249076,"mobile":18827913076,"cre_id":362201199504210418,
   "user_name":"彭思源","cardid":6212261502001124118,"bank_type":1001,"bank_name":"中国工商银行" }#用字典的方式来传值

result4=client4.service.bindBankCard(t)
print(result4)