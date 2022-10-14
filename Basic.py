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

def testList():
    ListAll: list[str] = ['item 1', 'item 2', 'item 3']   # Add type hint for total.
    ListTiny = ['item tiny 1', 'item tiny 2'];  # Change list item
    ListAll += ListTiny
    print(ListAll)

    ListAll[2] = ''     # Change list item.
    print(ListAll)

def testTuple():
    TupleAll = ('windows', 123, 2.23, 'linux', 3+4j)
    print(TupleAll)

    #TupleAll[1] = 40;   # To change tuple item is illegal.

def testSet():
    SetAll = {'Google', 'TMall', 'Apple', 'Tencent', 'Facebook', 'Baidu'}
    mark = 'Tencent';
    if mark in SetAll:
        print(mark + ' is in set')
    else:
        print(mark + ' is NOT in set')


