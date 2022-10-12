#!/usr/bin/python3
from typing import List
import sys

a, b, c, d = 20, 5.5, True, 4+3j;

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

if True:
    print('False')
else:
    print('True')


total: list[str] = ['item 1', 'item 2', 'item 3']   # Add type hint for total.
print(total)

print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
#print ('\n python 路径为',sys.path)
