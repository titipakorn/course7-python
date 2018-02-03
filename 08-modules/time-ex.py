#!/usr/bin/env python3
# -*- encoding : utf-8 -*-

import time

def nonce():
    return int(time.time() * 1000)

def delay(t):
    if t > 1:
        time.sleep(t)

while True:
    print("time:{} : {}".format(nonce(), time.time()))
    delay(3)