#!/usr/bin/python3
from typing import List
import sys
from FuncCollection import *
from Basic import *
from Snake import *

if __name__ == "__main__":
    print('命令行参数为:')
    for i in sys.argv:
        print(i)

    #input = 'I like python3 this small tool';
    #rw = reverseWords(input)
    #print(rw)

    #testList();
    #testTuple();
    #testSet();
    #testIfElse();
    #testAndOr();
    #testDictionary();
    #testTypeConversion();

    #AverageCalc();
    #TestRange();

    #testFuncDefaultArg()
    #testFuncDefaultArg("Japan")

    #fruits = ['Apple', 'Banana', 'Orange', 'S60'];
    #fruit_qty = testFuncArgAsList(fruits);
    #print(fruit_qty);

    result = tri_recursion(6);
    print(result);