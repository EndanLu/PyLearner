#!/usr/bin/python3
from typing import List
import sys

print('Reopen the world')
print('Just step-in again')

if True:
    print('False')
else:
    print('True')


total: list[str] = ['item 1', 'item 2', 'item 3']   # Add type hint for total.
print(total)

#sys.stdout.write(total)

print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
