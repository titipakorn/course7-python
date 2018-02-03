#!/usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib
import hmac

def hash(secret_key, msg, algorithm=hashlib.sha256):
    return hmac.new(secret_key.encode(), msg.encode(), algorithm).hexdigest()

'''
hash = HMAC-SHA256(payload, secret_key).to_hex
ex.
hash = HMAC-SHA256('GET|/api/v2/markets|access_key=xxx&foo=bar&tonce=123456789', 'yyy').to_hex
        = 'e324059be4491ed8e528aa7b8735af1e96547fbec96db962d51feb7bf1b64dee'
'''

secret_key = 'yyy'
msg = 'GET|/api/v2/markets|access_key=xxx&foo=bar&tonce=123456789'

payload = hash(secret_key, msg)
print("key:{}".format(secret_key))
print("msg:{}".format(msg))
print("hmac:{}".format(payload))
