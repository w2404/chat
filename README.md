这是一个通过代理服务器连接chatgpt API的多轮对话脚本。

我在这里修改这个脚本，就不用每次修改后发微信了。

# 安装

1. 需要安装python。安装的时候要勾选path和pip选项。

2. 打开命令行，输入pip install requests。确保requests下载成功，安装完成。

3. 点击右上角的code -> download zip，下载这个repo。并且解压。或者只下载[multi-turn.py](multi-turn.py)也可以，至少现在这里只有这一个脚本。

4. 在解压后，新建一个config.py文件，放在multi-turn.py同一个目录中。在其中填写代理服务器和API key。这个API key我会用微信发给你。

# 运行

打开命令行，用python ./multi-turn.py <保存聊天记录的文件> 的方式执行。

也可以双击或是右键multi-turn.py运行。

脚本会循环执行，一问一答，直到你按ctrl+d或者ctrl+c退出。

# 聊天记录

默认聊天记录会保存在history目录下，没有txt json之类的后缀名。

你可以用记事本或者notepad++打开这些文件，它们的保存格式是utf8。记事本或许不支持utf8，打开可能会有乱码。

如果用脚本读取一个有内容的聊天记录，就可以继续上次的对话。

但是对话总长度不允许超出4000 token。token是openai定义的一个单位，大约等同于英语的单词。

# 代理服务器

我的经验是代理服务器用hyster，连接会更稳定。不过如果连接不稳定，导致脚本断开连接退出，你也可以用脚本读取之前的历史聊天记录，继续之前的对话。

# 感想

在我写这个repo的时候，碰到了一些任何零碎问题。

像是怎么给repo设置github账户密码，怎么延长git密码的保存时间，怎么在md文件中写一个链接。

都是很基础的问题，但是平时不常用，就记不住，用的时候都会去问google，但是问google的话，你就需要好好斟酌用什么关键词去搜索，不然就要翻查好几页搜索结果，还要看文档。

但是问gpt的话，它会直接回答你。

# 问题

有任何问题或是要求可以到Issues中提出来。这比在微信中聊起来方便。你需要注册一个github账号，用outlook邮箱，163邮箱什么的就可以。
