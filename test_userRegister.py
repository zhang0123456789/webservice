#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/8 0008 下午 17:52
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : test_userRegister.py

from suds.client import Client

api_url2="http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"

client2=Client(api_url2)

print(client2)


'''如何传递参数值：'''
t={"channel_id":1,"ip":"120.24.235.105","mobile":18827915076 ,
   "pwd":"123456","user_id" :"蜜蜜蜜蜜","verify_code":605487}#用字典的方式传值

result2=client2.service.userRegister(t)
print(result2)