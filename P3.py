#!/usr/bin/python3
import platform
from typing import List
import sys
import datetime
import json
from FuncCollection import *
from Basic import *
from Snake import *
from CPerson import *
from CStudent import *
from FileOperation import *
from NumPyOperations import *
from PandasOperations import *
from EnjoyOpenAI import *
from TryWhisperTool import *
from TryBTYD import *


if __name__ == "__main__":
    print('命令行参数为:')
    for i in sys.argv:
        print(i)

    print(platform.system());
    print(dir(platform));

    x = datetime.datetime.now()
    print(x)
    print(x.year)
    print(x.strftime("%A"))     # weekday
    print(x.strftime("%B"))     # month

    x = datetime.datetime(2023, 5, 18)
    print(x)

    #input = 'I like python3 this small tool';
    #rw = reverseWords(input)
    #print(rw)

    #print("\n\nRecursion Example Results")
    #result = tri_recursion(7);
    #print(result);

    #testLambda();

    p1 = CPerson("Bill Gates", 66)
    p1.showAllAttr();

    s1 = CStudent("Elon Musk", 45, 7)
    s1.showAllAttr();
    s1.welcome();

    del p1;
    del s1;

    #testJson();
    #testRegEx();
    #testTryExcept();
    #testInput();
    #testStringFormat();
    #testReadFile();
    #testAppendFile();
    #testWriteFile();
    #testRemoveFile();

    #testNumPyBase();
    #testNumPyElementPickUp();
    #testNumPyArrayCut();
    #testNumPyDataType();
    #testNumPyCopyView();
    #testNumPyShape();
    #testNumPyIter();
    #testNumPyEnum();
    #testNumPyConcat();
    #testNumPyStack();
    #testNumPyArraySplit();
    #testNumPySearch();
    #testNumPySort();
    #testNumPyArrayFilter();
    #testNumPyRandom();
    #testNumPyUFunc();
    #testNumPyMathBasic();
    #testNumPyStdVar();
    #testNumPyPercentile();
    #testNumPyUniformHist();
    #testNumPyNormalHist();
    #testNumPyScatter();


    #testSciPyLinRegress();
    #testNumPyPolyfit();
    testPandasLinearRegression();

    genImageFromDallE('A cute baby with a lovely puppy.', '512x512');
    #enjoyChatGPT('How about the weather in Shanghai?');

    # Use CodeWhisper tool
    count_letter('aaabbbbcccd')
    test_count_letter()

    check_phone('18516157327')
    check_phone('185161573279')
    check_phone('18516157327a')
    test_check_phone()

    helloBTYD()






