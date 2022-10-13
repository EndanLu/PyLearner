#!/usr/bin/python3
from typing import List
import sys

a, b, c, d = 20, 5.5, True, 4+3j;

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

if type(c) == bool:
    print('Statement is True')
else:
    print('Statement is False')


ListAll: list[str] = ['item 1', 'item 2', 'item 3']   # Add type hint for total.
ListTiny = ['item tiny 1', 'item tiny 2']
ListAll += ListTiny
print(ListAll)

print('Daniel \nLu')
print(r'Daniel \nLu')   # r means the original string.

print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)

