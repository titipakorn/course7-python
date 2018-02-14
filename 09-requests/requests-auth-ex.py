#!/usr/bin/python3
# -*- coding: utf-8 -*-
# http://docs.python-requests.org/en/master/

import requests

url = 'https://httpbin.org/basic-auth/user/passwd'
content = requests.get(url, auth=('user', 'passwd'))
print(r.text)

''' output

{
authenticated: true,
user: "user"
}

'''