#!/usr/bin/env python3
# -*- encoding : utf-8 -*-

import json
from requests import post as __post__
from requests import get as __get__

DEFAULT_TIME_OUT = 4
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

'''
request GET/POST
'''
def get(u):
    return _get(build_requests(u))

def post(u, d={}, h={}):
    return _post(build_requests(u, d, h))

def build_requests(u, d={}, h={}):
    payload = {}
    h.update(DEFAULT_HEADERS)
    if d:
        payload['data'] = d

    payload['url'] = u
    payload['headers'] = h
    payload['timeout'] = DEFAULT_TIME_OUT
    return payload

def _get(payload):
    try:
        req = __get__(**payload)
        return json_decode(req.text)
    except Exception:
        print("[!][_get] {}".format(payload))
        return None

def _post(payload):
    try:
        req = __post__(**payload)
        return json_decode(req.text)
    except Exception:
        print("[!][_post] {}".format(payload))
        return None

def json_decode(content):
    try:
        return json.loads(content, parse_float=format_float)
    except Exception:
        print("[!][json_decode] {}".format(content))
        return content

def json_encode(input):
    try:
        return json.dumps(input, separators=(',', ':'))
    except Exception:
        print("[!][json_encode] {}".format(input))
        return None
