#!/usr/bin/env python3
# -*- encoding : utf-8 -*-

from utility.req import *
from urllib.parse import urlencode

def notify(msg, token):
    u = 'https://notify-api.line.me/api/notify'
    d = urlencode({'message':msg}).encode('utf-8')
    h = {
        'Authorization':'Bearer ' + token
    }
    return post(u, d, h)
