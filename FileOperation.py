#!/usr/bin/python3

def testReadFile():
    #f = open("LinuxRef\\modify_commit.txt", "r")
    f = open("README.md", "r")
    print(f.read())
    f.close()
    print("*****************************")

    f = open("README.md", "r")
    print(f.readline())
    print(f.readline())
    f.close()
    print("*****************************")

    f = open("README.md", "r")
    for line in f:
        print(line)
    f.close()
    print("*****************************")
