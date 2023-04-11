#!/usr/bin/python3
import CPerson
from CPerson import *

class CStudent(CPerson):
    def __init__(self, name, age, grade):
        super().__init__(name, age);    # 调用父类构造函数，注意无需填写参数self。
        self.grade = grade;

    def showAllAttr(self):
        print('---CStudent::showAllAttr()---Begin---')
        super().showAllAttr();  # 显式调用父类函数。
        print(self.grade);
        print('---CStudent::showAllAttr()---End---')

    def welcome(self):
        print('Welcome', self.name, 'from grade of', self.grade)