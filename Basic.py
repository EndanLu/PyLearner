#!/usr/bin/python3

import sys


def testBasic():
    a, b, c, d = 20, 5.5, True, 4 + 3j;

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
    listAll: list[str] = ['item 1', 'item 2', 'item 3']  # Add type hint for total.
    listTiny = ['item tiny 1', 'item tiny 2'];  # Change list item
    listAll += listTiny
    print(listAll)

    listAll[2] = ''  # Change list item.
    print(listAll)


def testTuple():
    tupleAll = ('windows', 123, 2.23, 'linux', 3 + 4j)
    print(tupleAll)

    # tupleAll[1] = 40;   # To change tuple item is illegal.


def testSet():
    setAll = {'Google', 'TMall', 'Apple', 'Tencent', 'Facebook', 'Baidu', 'Apple', 'Google'}
    print(setAll)  # Auto-remove duplicate item

    mark = 'Tencent';
    if mark in setAll:
        print(mark + ' is in set')
    else:
        print(mark + ' is NOT in set')

    # set可以进行集合运算
    a = set('abracadabra')
    b = set('alacazam')

    print(a)    # Auto-remove duplicate item
    print(b)    # Auto-remove duplicate item
    print(a - b)  # a 和 b 的差集
    print(a | b)  # a 和 b 的并集
    print(a & b)  # a 和 b 的交集
    print(a ^ b)  # a 和 b 中不同时存在的元素

def testDictionary():
    dictAll = {'name':'Daniel Lu', 'code':'681161', 'mail':'Daniel_E_Lu@vfc.com'}

    print(dictAll)
    print(dictAll.keys())
    print(dictAll.values())

