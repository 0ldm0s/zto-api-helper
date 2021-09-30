# -*- coding: utf-8 -*-
from zto_api_helper import ZtoApiHelper

app_key: str = 'd577e7b5024ad20446e10'
app_secret: str = '0e8e9457d493666ee2f5adb783e69abb'

helper = ZtoApiHelper(app_key, app_secret, is_sandbox=True)
data = {
    'type': 0,
    'orderCode': '210107000003719103',
    'billCode': ''
}
remote_data, msg = helper.get_remote_data('zto.open.getOrderInfo', data)
if remote_data is None:
    print(msg)
    exit(0)
print(remote_data)
