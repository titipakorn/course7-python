#!/usr/bin/python3
# -*- coding: utf-8 -*-

from json import dumps

content = {"c": 0, "b": 1, "a": 2, "d": [1,2,3]}

encode = d(content, sort_keys=True, indent=4)
print(encode)