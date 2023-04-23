#!/usr/bin/python3

def testFileOperations():
    #f = open("LinuxRef\\modify_commit.txt", "r")
    f = open("README.md", "r")
    print(f.read())
    f.close()
