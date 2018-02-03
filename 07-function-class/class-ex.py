#!/usr/bin/env python3
# -*- encoding : utf-8 -*-
# Class

class Account():
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount


acc = Account(1000)
print(acc.balance)

acc.deposit(100)
print(acc.balance)

acc.withdraw(500)
print(acc.balance)