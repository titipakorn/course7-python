#!/usr/bin/python3
# -*- coding: utf-8 -*-
# http://docs.python-requests.org/en/master/

import requests

post = {
    'key1': 'value1',
    'key2': 'val2'
}

url = 'https://httpbin.org/post'
content = requests.post(url, data=post)

print(content.text)
