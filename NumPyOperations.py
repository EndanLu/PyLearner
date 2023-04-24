#!/usr/bin/python3

import numpy as np

def testNumPyBase():
    print("NumPy Version: " + np.__version__)

    arr = np.array([1,2,3,4,5])
    print(arr)
    print(type(arr))

    arr2 = np.array((1, 2, 3, 4, 5))
    print(arr2)
    print(type(arr2))

    arr3 = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr3)

    a = np.array(42)
    b = np.array([1, 2, 3, 4, 5])
    c = np.array([[1, 2, 3], [4, 5, 6]])
    d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

    print("array dimension: " + str(a.ndim))
    print("array dimension: " + str(b.ndim))
    print("array dimension: " + str(c.ndim))
    print("array dimension: " + str(d.ndim))

def testNumPyElementPickUp():
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print('2nd element on 1st dim: ', arr[0, 1])
    print('5th element on 2nd dim: ', arr[1, 4])
    print('Last element from 2nd dim: ', arr[1, -1])

def testNumPyArrayCut():
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr[1:5])     # Starting from element no.1, not including no.5
    print(arr[4:])      # Starting from element no.4, to the end.
    print(arr[:4])      # Starting from beginning, not including element no.4

    print(arr[1:5:2])   # Starting from element no.1, not including no.5, step is 2.
    print(arr[::2])



