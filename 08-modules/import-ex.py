#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

content = {"c": 0, "b": 1, "a": 2, "d": [1,2,3]}

encode = json.dumps(content, sort_keys=True, indent=4)
print(encode)