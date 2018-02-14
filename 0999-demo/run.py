#!/usr/bin/env python3
# -*- encoding : utf-8 -*-

from init import *

bx = BX()

bx.get_ticker()
thb_btc_rate = bx.get_coin('thb_btc')
print(thb_btc_rate)


# while True:
# 	bx.get_ticker()
# 	thb_btc_rate = bx.get_coin('thb_btc')
# 	print(thb_btc_rate)

# 	delay(1)

# bx.get_ticker()
# print(ticker)


# buy = bx.get_buy_rate('thb_eth', 3500)
# print(buy)
# print()


# sell = bx.get_sell_rate('thb_eth', 0.5)
# print(sell)
# print()
