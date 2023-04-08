#!/usr/bin/python3

class CPerson:
  def __init__(self, name, age):  # 相当于C++构造函数
    self.name = name
    self.age = age

  def showAllAttr(self):
    print('---CPerson::showAllAttr()---Begin---')
    print(self.name)
    print(self.age)
    print('---CPerson::showAllAttr()---End---')




