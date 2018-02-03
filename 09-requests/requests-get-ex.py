#!/usr/bin/python3
# -*- coding: utf-8 -*-
# http://docs.python-requests.org/en/master/

import requests

url = 'https://httpbin.org/get'
content = requests.get(url)

print(content)

print(content.text)

print(content.headers)

print(content.headers['Content-Type'])