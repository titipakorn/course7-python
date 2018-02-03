#!/usr/bin/python3
# -*- coding: utf-8 -*-
# http://docs.python-requests.org/en/master/

import requests

headers = {
    'User-Agent': 'stephack.com : v1'
}

url = 'https://httpbin.org/get'
content = requests.get(url, headers=headers)

print(content.text)
