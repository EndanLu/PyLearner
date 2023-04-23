#!/usr/bin/python3

import sys
import json # import JSON
import re   # import 正则表达式


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

def testIfElse():
    a = 200
    b = 66
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")

def testAndOr():
    a = 200
    b = 66
    c = 500
    if a > b and c > a:
        print("Both conditions are True")

    if a > b or a > c:
        print("At least one condition is true")

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

#Python 编程语言中有四种集合数据类型：
#列表（List）是一种有序和可更改的集合。允许重复的成员。
#元组（Tuple）是一种有序且不可更改的集合。允许重复的成员。
#集合（Set）是一个无序和无索引的集合。没有重复的成员。
#词典（Dictionary）是一个无序，可变和有索引的集合。没有重复的成员。

def testList():
    listAll: list[str] = ['item 1', 'item 2', 'item 3']  # Add type hint for total.
    listTiny = ['item tiny 1', 'item tiny 2'];  # Change list item
    listAll += listTiny
    print(listAll)

    listAll[2] = ''  # Change list item.
    print(listAll)

    # List推导式
    names = ['Bob', 'Tom', 'Alice', 'Jerry', 'Wendy', 'Jocelyn']
    new_names = [name.upper() for name in names if len(name) > 3]
    print(new_names)

    new_names.pop(1)
    print(new_names)

    # 计算30以内的被3整除的数
    multiples = [i for i in range(30) if i % 3 == 0]
    print(multiples)


def testTuple():
    tupleAll = ('windows', 123, 2.23, 'linux', 3 + 4j)
    print(tupleAll);
    print(tupleAll[-1]);    # Print the last element in the tuple.
    print(tupleAll[2:4]);

    # tupleAll[1] = 40;   # Changing tuple item is illegal.


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

    mail = dictAll.get('mail');     # Get value by key.
    print(mail);

def TestRange():
    for x in range(3):
        print(x);
    print('--------------------');

    for x in range(3,7):
        print(x);
    print('--------------------');

    for x in range(5,50,10):
        print(x);
    else:
        print('Finished Printing');

    # 计算平均成绩
#    scores = [85, 92, 78, 90, 88]
#    average_score = sum(scores) / len(scores)
#    print("平均成绩为：", average_score)

def testFuncDefaultArg(country="China"):
    print("I am from " + country)   # default parameter is "China"

def testFuncArgAsList(foodlist):
    for food in foodlist:
        print(food);
    return len(foodlist);

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)   # 递归
  else:
    result = 0
  return result


def myfunc(n):
    return lambda a: a * n

def testLambda():
    mydoubler = myfunc(2)
    mytripler = myfunc(3)

    print(mydoubler(11))
    print(mytripler(11))

def testJson():
    # JSON -> Python
    # JSON data:
    json_origin = '{ "name":"Bill", "age":63, "city":"Seatle", "gender":"Male"}'

    # parse x:
    parsed = json.loads(json_origin)

    # the result is a Python dictionary:
    print(parsed["gender"])

    # ---------------------------------
    # Python -> JSON
    # a Python object (dict):
    dict = {
        "name": "Bill",
        "age": 63,
        "city": "Seatle"
    }

    # convert into JSON:
    y = json.dumps(dict)

    # the result is a JSON string:
    print(y)

    # Different Python Objects -> JSON
    print(json.dumps({"name": "Bill", "age": 63}))
    print(json.dumps(["apple", "bananas"]))
    print(json.dumps(("apple", "bananas")))
    print(json.dumps("hello"))
    print(json.dumps(42))
    print(json.dumps(31.76))
    print(json.dumps(True))
    print(json.dumps(False))
    print(json.dumps(None))

    x = {
        "name": "Bill",
        "age": 63,
        "married": True,
        "divorced": False,
        "children": ("Jennifer", "Rory", "Phoebe"),
        "pets": None,
        "cars": [
            {"model": "Porsche", "mpg": 38.2},
            {"model": "BMW M5", "mpg": 26.9}
        ]
    }

    print(json.dumps(x, indent=4))


def testRegEx():
    txt = "China is a great country"
    x = re.search("^China.*country$", txt)

    if (x):
        print("YES! We have a match!")
    else:
        print("No match")

    x = re.findall("a", txt)
    print(x)

    x = re.findall("USA", txt)
    print(x)
    if (x):
        print("Yes, there is at least one match!")
    else:
        print("No match")

    str = "China is a great country"
    x = re.search("\s", str)    # Looking for a whitespace in str

    print("The first white-space character is located in position:", x.start())

    x = re.split("\s", str)     # Split str with whitespace
    print(x)

    x = re.sub("\s", "*", str)  # Replace whitespace with *
    print(x)

def testTryExcept():
    try:
        print(x)
    except NameError:
        print("Variable x is not defined")
    except:
        print("Something else went wrong")
    else:
        print("Nothing went wrong.")
    finally:
        print("Finally operation")

    #x = "hello"
    #if not type(x) is int:
    #raise TypeError("Exception message defined by Daniel: Only integers are allowed")

def testInput():
    print("Input your name: ")
    x = input()
    print("Welcome", x, "!")

def testStringFormat():     # 演示若干种用format()函数构建String的方法，个人认为最后一种最实用。
    price = 52
    txt = "The price is {} dollars."
    print(txt.format(price))

    txt = "The price is {:.2f} dollars"
    print(txt.format(price))

    quantity = 3
    itemno = 567
    price = 52
    myorder = "I want {} pieces of item number {} for {:.2f} dollars."
    print(myorder.format(quantity, itemno, price))

    age = 63
    name = "Bill"
    txt = "His name is {1}, {1} is {0} years old. \nWelcome {1}!"
    print(txt.format(age, name))

    carName = "Volvo"
    carModel = "S60"
    myorder = "I have a {carname}, it is a {model}."
    myorder = myorder.format(carname=carName, model=carModel)
    print(myorder)

