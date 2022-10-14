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


def testTypeConversion():
    x = int('3')  # str -> int
    y = float('4.2')  # str -> float
    z = str(3.0)  # float -> str

    num_int = 123
    num_str = "456"

    print("num_int 数据类型为:", type(num_int))
    print("类型转换前，num_str 数据类型为:", type(num_str))

    num_str = int(num_str)  # 强制转换为整型
    print("类型转换后，num_str 数据类型为:", type(num_str))

    num_sum = num_int + num_str

    print("num_int 与 num_str 相加结果为:", num_sum)
    print("sum 数据类型为:", type(num_sum))


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

    print(a)  # Auto-remove duplicate item
    print(b)  # Auto-remove duplicate item
    print(a - b)  # a 和 b 的差集
    print(a | b)  # a 和 b 的并集
    print(a & b)  # a 和 b 的交集
    print(a ^ b)  # a 和 b 中不同时存在的元素


def testDictionary():
    dictAll = {'name': 'Daniel Lu', 'code': '681161', 'mail': 'Daniel_E_Lu@vfc.com'}

    print(dictAll)
    print(dictAll.keys())
    print(dictAll.values())
