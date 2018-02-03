#!/usr/bin/env python3
# -*- encoding : utf-8 -*-

def function():
    print("function!")

def function_with_args(param1, param2):
    print("param1, {} , param2 {}".format(param1, param2))

def function_with_return(a, b):
    return a + b

function()

function_with_args("first", "last")

x = function_with_return(1,2)
print(x)