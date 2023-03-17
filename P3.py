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

    input = 'I like python3 this small tool';
    rw = reverseWords(input)
    print(rw)

    #testList();
    #testTuple();
    #testSet();
    #testDictionary();
    #testTypeConversion();

    AverageCalc();
    #Snake();