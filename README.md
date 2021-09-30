# 项目说明

首先，本项目不会有英文版。毕竟不会有外国人会使用中通快递的。其次，这是非官方项目，仅作为抛砖引玉之用。最后，这是从我自己的项目所使用的PyMIO框架中抽离的简易项目，因此没有考虑动态配置的问题。如需要动态配置，可以考虑使用PyMIO项目。

## 更新日志

| 版本号 | 说明                           |
| ------ | ------------------------------ |
| 0.1    | 简易版本，仅抽离了核心业务函数 |

# 版权说明

```
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.

```

 # How To Use

## 安装依赖

```shell
pip install -r requirements.txt
```

## 直接使用

源码中的zto_api_helper文件夹可以直接剪贴复制到具体的项目中直接使用，只需要确定已安装完对应的依赖即可。

## PIP方式

可能会有，也可能通不过，通过了再算。

# 代码时间

首先确保已经添加了对应的api接口权限。其次，如果在测试输出签名时发生了跟官方接口给出的结果不一致时，不要惊慌，请先检查空格。官方的demo全部吃掉了空格，因此如果直接使用的是`json.dumps`的话，会因为加入了空格而导致签名不一致的情况，只要在官方的api工具内，补齐对应的空格，即可得到一致的计算结果（或者你愿意的话，也可以直接替换掉json.dumps后json文本的空格）。

## Show Me The Code

```python
# -*- coding: utf-8 -*-
from zto_api_helper import ZtoApiHelper

app_key: str = 'd577e7b5024ad20446e10'
app_secret: str = '0e8e9457d493666ee2f5adb783e69abb'

# 初始化助手类
helper = ZtoApiHelper(app_key, app_secret, is_sandbox=True)
# 具体的查询参数
data = {
    'type': 0,
    'orderCode': '210107000003719103',
    'billCode': ''
}
# remote_data为远程服务器返回的信息，如果发生异常，则返回None，此时msg变量为具体的错误信息
remote_data, msg = helper.get_remote_data('zto.open.getOrderInfo', data)
if remote_data is None:
    print(msg)
    exit(0)
print(remote_data)

```

