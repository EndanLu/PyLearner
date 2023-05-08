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
    print(arr[::2])     # Step = 2.

    arr_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(arr_2d[1, 1:4])
    print(arr_2d[0:2, 2])
    print(arr_2d[0:2, 1:4])


def testNumPyDataType():
    arr = np.array([1, 2, 3, 4])
    print(arr.dtype)

    arr2 = np.array(['apple', 'banana', 'cherry'])
    print(arr2.dtype)

    arr3 = np.array([1, 2, 3, 4], dtype='S')
    print(arr3)
    print(arr3.dtype)

    # Convert data type from float to int.
    arr = np.array([1.1, 2.1, 3.1])
    newarr = arr.astype('i8')       # i4 means int32, i8 means int64.
    print(newarr)
    print(newarr.dtype)

    # Convert data type from int to bool.
    arr = np.array([1, 0, 3])
    newarr = arr.astype(bool)       # 0 is False, non-zero is True
    print(newarr)
    print(newarr.dtype)

def testNumPyCopyView():
    arr = np.array([1, 2, 3, 4, 5])
    arr_copy = arr.copy()
    arr_copy[0] = 61
    print(arr)
    print(arr_copy)

    arr_view = arr.view()
    arr_view[0] = 81
    print(arr)
    print(arr_view)

    print(arr_copy.base)        # Copy has own data, return "None"
    print(arr_view.base)        # View doesn't have own data, return the original array.

def testNumPyShape():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print("Shape of arr:", arr.shape)

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    newarr = arr.reshape(3, 4)
    print(newarr)

    newarr = arr.reshape(2, 3, 2)
    print(newarr)
    print(newarr.base)          # Reshape() return one view, not copy.

    arr = np.array([[1, 2, 3], [4, 5, 6]])
    newarr = arr.reshape(-1)    # 2D -> 1D
    print(newarr)

def testNumPyIter():
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    for x in arr:
        print(x)        # [1, 2, 3], [4, 5, 6]

    for x in arr:
        for y in x:
            print(y)    # 1, 2, 3, 4, 5, 6

    # We can also use nditer() to avoid multiple layers of for()
    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    for x in np.nditer(arr):
        print(x)

    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    for x in np.nditer(arr[:,::2]):         # 1, 3, 5, 7
        print(x)

def testNumPyEnum():
    arr = np.array(['a', 'b', 'c'])
    for idx, x in np.ndenumerate(arr):
        print(idx, x)

    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    for idx, x in np.ndenumerate(arr):
        print(idx, x)

def testNumPyConcat():
    arr_1 = np.array([1, 2, 3])
    arr_2 = np.array([4, 5, 6])
    newarr = np.concatenate((arr_1, arr_2))
    print(newarr)

    arr_3 = np.array([[1, 2], [3, 4]])
    arr_4 = np.array([[5, 6], [7, 8]])
    newarr = np.concatenate((arr_3, arr_4), axis=1)
    print(newarr)

def testNumPyStack():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])

    print("************ stack(), axis = 1 ******************")
    arr = np.stack((arr1, arr2), axis=1)
    print(arr)

    print("************ hstack() ******************")
    arr = np.hstack((arr1, arr2))
    print(arr)

    print("************ dstack() ******************")
    arr = np.dstack((arr1, arr2))
    print(arr)

    print("************ vstack() ******************")
    arr = np.vstack((arr1, arr2))
    print(arr)

def testNumPyArraySplit():
    arr = np.array([1, 2, 3, 4, 5, 6])
    newarr = np.array_split(arr, 3)
    print(newarr)
    print(newarr[0])
    print(newarr[1])
    print(newarr[2])

    arr = np.array([1, 2, 3, 4, 5, 6])
    newarr = np.array_split(arr, 4)
    print(newarr)

    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
    newarr = np.array_split(arr, 3)
    print(newarr)

    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
    newarr = np.hsplit(arr, 3)
    print(newarr)

def testNumPySearch():
    print("\n*******testNumPySearch()*******")
    arr = np.array([1, 2, 3, 4, 5, 4, 4])
    x = np.where(arr == 4)          # Find 4 in array
    print(x)

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    x = np.where(arr % 2 == 0)      # Find even number in array.
    print(x)

    x = np.where(arr % 2 == 1)      # Find odd number in array.
    print(x)

    arr = np.array([6, 7, 8, 9])
    x = np.searchsorted(arr, 7, side='right')
    print(x)

def testNumPySort():
    arr = np.array([3, 2, 0, 1])
    arr = np.sort(arr)
    print(arr)

    arr = np.array(['banana', 'cherry', 'apple'])
    arr = np.sort(arr)
    print(arr)

    arr = np.array([True, False, True])
    arr = np.sort(arr)
    print(arr)

    arr = np.array([[3, 2, 4], [5, 0, 1]])
    arr = np.sort(arr)
    print(arr)

def testNumPyArrayFilter():
    arr = np.array([61, 62, 63, 64, 65])
    x = [True, False, True, False, True]
    newarr = arr[x]
    print(newarr)

    # 找>62的数，方法一。
    arr = np.array([61, 62, 63, 64, 65])
    # 创建一个空列表
    filter_arr = []

    # 遍历 arr 中的每个元素
    for element in arr:
        # 如果元素大于 62，则将值设置为 True，否则为 False：
        if element > 62:
            filter_arr.append(True)
        else:
            filter_arr.append(False)

    newarr = arr[filter_arr]

    print(filter_arr)
    print(newarr)

    # 找>62的数，方法二。(避免迭代)
    arr = np.array([61, 62, 63, 64, 65])
    filter_arr = arr > 62
    newarr = arr[filter_arr]

    print(filter_arr)
    print(newarr)

    # 找偶数，方法一。
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    # 创建一个空列表
    filter_arr = []

    # 遍历 arr 中的每个元素
    for element in arr:
        # 如果元素可以被 2 整除，则将值设置为 True，否则设置为 False
        if element % 2 == 0:
            filter_arr.append(True)
        else:
            filter_arr.append(False)

    newarr = arr[filter_arr]

    print(filter_arr)
    print(newarr)

    # 找偶数，方法二。(避免迭代)
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    filter_arr = arr % 2 == 0
    newarr = arr[filter_arr]

    print(filter_arr)
    print(newarr)