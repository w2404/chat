"""
"""
import requests
import json
import sys
import config

#分隔符
split='------------------------'

def send(messages):
    headers = {"Authorization": "Bearer " + config.key, "Content-Type": "application/json"}
    proxies = {'http': config.proxy, 'https': config.proxy}
    u = 'https://api.openai.com/v1/chat/completions'
    data = {"model": "gpt-3.5-turbo", "messages": messages, "temperature": 0.7}
    r = requests.post(u, json.dumps(data), headers=headers, proxies=proxies)
    o = r.json()
    return o


#决定历史文件存储路径
if len(sys.argv) > 1:
    p_store = sys.argv[1]
else:
    import os
    os.makedirs('./history/', exist_ok=True)
    i = len(os.listdir('./history/'))
    p_store = f'./history/{i}'
print('聊天记录保存在', p_store)
open(p_store, 'a').close()
#读取历史记录
messages = [json.loads(line) for line in open(p_store)]
for m in messages:
    if m['role']=='user':print('------------------------') #加分隔符方便阅读
    print(m['role'], ':', m['content'])

while True:
    s = input(split+'\nuser: ')
    if len(s.strip())<1:continue
    m1 = {"role": "user", "content": s}
    messages.append(m1)
    resp = send(messages)
    with open(p_store, 'a') as f:
        json.dump(m1, f, ensure_ascii=False)
        f.write('\n')
    if 'choices' not in resp:
        print(resp)
    for c in resp['choices']:
        m2 = c['message']
        with open(p_store, 'a') as f:
            json.dump(m2, f, ensure_ascii=False)
            f.write('\n')
        messages.append(m2)
        print(m2['role'], ':', m2['content'])
    print(resp['usage'])
