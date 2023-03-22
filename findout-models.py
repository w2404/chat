"""
这里列出可以使用的模型

查找结果是这个帐号最新可用的模型还是 gpt-3.5-turbo
"""
import requests
import datetime
import json
import config
headers={"Authorization":"Bearer "+config.key}
proxies={'http':config.proxy,'https':config.proxy}
u='https://api.openai.com/v1/models'
r=requests.get(u,headers=headers,proxies=proxies)
o=r.json()
#with open('2.json','w') as f:json.dump(o,f)
l=o['data']

#for o in l:print(o)

#日期排列，找到最新的模型
l1=[(o['created'],datetime.datetime.fromtimestamp(o['created']),o['owned_by'],o['object'],o['id']) for o in l]
l1=sorted(l1)
for o in l1:print(o[1],o[2],o[3],o[4])


         
