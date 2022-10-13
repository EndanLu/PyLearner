#!/usr/bin/python3
from typing import List
import sys
from FuncCollection import reverseWords
from Basic import testBasic

if __name__ == "__main__":
    print('命令行参数为:')
    for i in sys.argv:
        print(i)

    input = 'I like python3'
    rw = reverseWords(input)
    print(rw)

    testBasic()