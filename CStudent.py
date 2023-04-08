#!/usr/bin/python3
import CPerson
from CPerson import *

class CStudent(CPerson):
    def __init__(self, name, age, grade):
        CPerson.__init__(self, name, age);    # 调用父类构造函数
        self.grade = grade;

    def showAllAttr(self):
        print('---CStudent::showAllAttr()---Begin---')
        CPerson.showAllAttr(self);
        print(self.grade);
        print('---CStudent::showAllAttr()---End---')
