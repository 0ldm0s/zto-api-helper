# -*- coding: utf-8 -*-
import requests
import simplejson as json
from hashlib import md5
from base64 import b64encode
from typing import Dict, Any, Optional, Tuple


class ZtoApiHelper(object):
    VERSION: str = '0.1'
    api_host: str
    app_key: str
    app_secret: str

    def __init__(self, app_key: str, app_secret: str, is_sandbox: bool = True):
        self.api_host = 'japi-test.zto.com' if is_sandbox else 'japi.zto.com'
        self.app_key = app_key
        self.app_secret = app_secret

    def gen_digest(self, data: Dict[str, Any]) -> Optional[str]:
        try:
            json_str: str = json.dumps(data)
        except json.JSONDecodeError:
            return None
        plan_text = f'{json_str}{self.app_secret}'
        result = md5(plan_text.encode('UTF-8'))
        crypto: bytes = b64encode(result.digest())
        return crypto.decode('utf-8')

    def get_remote_data(self, api_uri: str, data: Dict[str, Any], company_id: Optional[str] = None) \
            -> Tuple[Optional[Dict[str, Any]], str]:
        digest: Optional[str] = self.gen_digest(data)
        if digest is None:
            return None, '生成签名错误'
        headers = {
            'User-Agent': f'pymio-zto-sdk/{self.VERSION}',
            'Content-Type': 'application/json',
            'x-dataDigest': digest
        }
        if company_id is not None:
            headers['x-companyId'] = company_id
        else:
            headers['x-appKey'] = self.app_key
        try:
            r = requests.post(f'https://{self.api_host}/{api_uri}', data=json.dumps(data),
                              headers=headers)
            return r.json(), 'OK'
        except Exception as e:
            return None, str(e)
