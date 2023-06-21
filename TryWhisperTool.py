#!/usr/bin/python3

# 创建一个函数，计算字符串中出现最多次数的字母以及出现次数。
def count_letter(str):
    dict = {}
    for i in str:
        dict[i] = dict.get(i, 0) + 1
    max_key = max(dict, key=dict.get)
    print(max_key, dict[max_key])
    return max_key, dict[max_key]

# 为count_letter函数添加单元测试代码
def test_count_letter():
    assert (count_letter('hello') == ('l', 2))
    assert (count_letter('hello world') == ('l', 3))
