#!/usr/bin/python3

def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


def AverageCalc():
    a = [['2018102','小花','女',19,'英语'],['2018306','小莲','女',18,'数学'],['2018836','小炸','女',20,'数学']];

    total = 0.0;

    for i in a:
        total = total + i[3]

    print('Average == ', total/len(a))