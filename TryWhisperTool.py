#!/usr/bin/python3

# 创建一个函数，计算字符串中出现最多次数的字母以及出现次数。
def count_letter(str):
    dict = {}
    for i in str:
        dict[i] = dict.get(i, 0) + 1
    max_key = max(dict, key=dict.get)
    print(max_key, dict[max_key])
    return (max_key, dict[max_key])

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


# 创建一个类，用于操作MySQL数据库，对表的字段进行增删改查。
class MySQLHelper:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

        self.conn = None
        self.cursor = None

    def connect(self):
        import pymysql
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def insert(self, table, **kwargs):
        keys = list(kwargs.keys())
        values = list(kwargs.values())
        sql = 'insert into %s (%s) values (%s)' % (table, ','.join(keys), ','.join(['%s'] * len(values)))
        self.cursor.execute(sql, values)
        self.conn.commit()


    def delete(self, table, **kwargs):
        keys = list(kwargs.keys())
        values = list(kwargs.values())
        sql = 'delete from %s where %s' % (table, ' and '.join(['%s=%s'] * len(keys)))
        self.cursor.execute(sql, values)
        self.conn.commit()


    def update(self, table, **kwargs):
        keys = list(kwargs.keys())
        values = list(kwargs.values())
        sql = 'update %s set %s where %s' % (table, ','.join(['%s=%s'] * len(keys)), ','.join(['%s=%s'] * len(keys)))
        self.cursor.execute(sql, values)
        self.conn.commit()

# 针对上面的类，写一些测试代码
def test_MySQLHelper():
    helper = MySQLHelper('localhost', 3306, 'root', '123456', 'test')
    helper.connect()
    helper.insert('user', name='小明', age=18)
    helper.update('user', name='小明', age=19)
    helper.delete('user', name='小明')
    helper.close()
