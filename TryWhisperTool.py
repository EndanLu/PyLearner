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
    print('count_letter检毕通过')

# 创建一个检验手机号是否合法的函数
def check_phone(phone):
    if len(phone) == 11:
        if phone.startswith('1') and phone.isdigit():
            return True
        else:
            return False
    else:
        return False

# 为check_phone函数添加单元检测代码
def test_check_phone():
    assert (check_phone('13800138000') == True)
    assert (check_phone('13800138000a') == False)
    assert (check_phone('13800138000aa') == False)
    assert (check_phone('1380013') == False)
    print('check_phone检毕通过')



