#!/usr/bin/python3

class CPerson:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def showAllAttr(self):
    print(self.name)
    print(self.age)

class CStudent(CPerson):
  pass;


