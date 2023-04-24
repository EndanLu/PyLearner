#!/usr/bin/python3

import datetime

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

def testAppendFile():
    f = open("testing.txt", "a")
    current = datetime.datetime.now()
    current = current.strftime("%c")

    newLine = "New Line Appended at {time}"
    newLine = newLine.format(time=current)

    f.write(newLine)
    f.close()

    f = open("testing.txt", "r")
    print(f.read())
    f.close()

def testWriteFile():
    f = open("testing.txt", "w")
    f.write("Woops! I have deleted the content!")
    f.close()

    # open and read the file after the appending:
    f = open("testing.txt", "r")
    print(f.read())
    f.close()
