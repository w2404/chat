import json
import os

import requests
import re
import config
OPENAI_API_KEY = config.key #os.environ.get("OPENAI_API_KEY")
OPENAI_BASE_URL = "https://api.openai.com/v1/chat/completions"


def translator(srt):
    prompt = "You are an expert subtitle translator in all languages. Translate all language subtitle to Chinese subtitle, and keep the original language sentence and the new Chinese subtitle. You need to respond in a fixed format."

    few_shot_text_request = (
        "1\n"
        "00:00:00,000 --> 00:00:07,800\n"
        "Ladies and gentlemen, let's welcome Mr. L.M.A.S, the co-founder and CEO at Tesla, and Jack Ma,\n"
        # "\n"
        # "2\n"
        # "00:00:07,800 --> 00:00:11,680\n"
        # "the co-chair of the UN high-level panel on digital cooperation.\n"
    )

    few_shot_text_response = (
        "1\n"
        "00:00:00,000 --> 00:00:07,800\n"
        "Ladies and gentlemen, let's welcome Mr. L.M.A.S, the co-founder and CEO at Tesla, and Jack Ma,\n"
        "女士们先生们，让我们欢迎特斯拉公司的联合创始人兼首席执行官L.M.A.S先生和数字合作联合国高级别小组的联合主席马云先生。\n"
        # "\n"
        # "2\n"
        # "00:00:07,800 --> 00:00:11,680\n"
        # "the co-chair of the UN high-level panel on digital cooperation.\n"
        # "数字合作联合国高级别小组的联合主席。\n"
    )

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    data = {
        "model": "gpt-3.5-turbo",
        # "temperature": 0,
        # "top_p": 1,
        # "frequency_penalty": 1,
        # "presence_penalty": 1,
        "stream": False,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": few_shot_text_request},
            {"role": "assistant", "content": few_shot_text_response},
            {"role": "user", "content": srt},
        ],
    }

    proxies = {'http': config.proxy, 'https': config.proxy}
    response = requests.post(OPENAI_BASE_URL, headers=headers, json=data,proxies=proxies)

    answer = response.json() #["choices"][0]["message"]["content"].strip()
    return answer
    print(answer)

def splitsrc1(p):

    lines=open(p,).readlines()
    if lines[0][0]=='\ufeff':
        lines[0]=lines[0][1:]

    turn=''
    for line in lines:
        r=re.findall('^\d+$',line)
        if len(r)>0:
            yield turn
            turn=''
        turn+=line
    yield turn

def splitsrc2(turns):
    s=''
    i=0
    for turn in turns:
        s+=turn
        i+=1
        if i%100==0:
            yield s
            s=''
    yield s

def localcache(p,fun,*args):
    if os.path.exists(p):
        return open(p).read()
    s=fun(*args)
    with open(p,'w') as f:
        f.write(s)
    return s



def transfile(p):
    turns=list(splitsrc1(sys.argv[1]))
    turns2=list(splitsrc2(turns))
    ss=''
    for i,turn in enumerate(turns2):
        p_local=f'out/{p.replace("/","-")}-{i:02d}'
        if not os.path.exists(p_local):
            with open(p_local,'w') as f:
                f.write(turn)

        p_local=f'out/{p.replace("/","-")}-{i:02d}-trans'
        if not os.path.exists(p_local):
            s=translator(turn)
            with open(p_local,'w') as f:
                json.dump(s,f)
                #f.write(s)
        ss+=open(p_local).read()

    p_local=f'out/trans-{p.replace("/","-")}'
    if not os.path.exists(p_local):
        with open(p_local,'w') as f:
            f.write(turn)


if __name__ == "__main__":
    import sys
    for p in sys.argv[1:]:
        transfile(p)
    #test_srt=open(sys.argv[1]).readlines()
    #test_srt='\n'.join(test_srt[:100])
    #s=translator(test_srt)
    #import json
    #with open(sys.argv[1]+'.txt','w' ) as f:
    #    json.dump(s,f)
    #    #f.write(s)
