#!/usr/bin/python3

import sys

def testBasic():
    a, b, c, d = 20, 5.5, True, 4+3j;

    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))

    if type(c) == bool:
        print('Statement is True')
    else:
        print('Statement is False')

    print('Daniel \nLu')
    print(r'Daniel \nLu')  # r means the original string.

def testListAndTuple():

    ListAll: list[str] = ['item 1', 'item 2', 'item 3']   # Add type hint for total.
    ListTiny = ['item tiny 1', 'item tiny 2']
    ListAll += ListTiny
    print(ListAll)

    ListAll[2] = ''     # Change list item.
    print(ListAll)


