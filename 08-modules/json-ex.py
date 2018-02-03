#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

def json_decode(content):
    try:
        return json.loads(content)
    except Exception:
        print("[!][json_decode] {}".format(content))
        return content

def json_encode(content):
    try:
        return json.dumps(content, sort_keys=True, indent=4)
    except Exception:
        print("[!][json_encode] {}".format(content))
        return None

data = {"c": 0, "b": 1, "a": 2, "d": [4,1,2,3]}

encode = json_encode(data)
print(encode)

decode = json_decode(encode)
print(decode)

print(decode['d'][0])