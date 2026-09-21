# numpy is used mainly for array operation and also for mathematical operation on array

import numpy as np

arr = np.array([1,2,3])      # 1D array
print(arr)

arr2 = np.array([[1,2,3],[4,5,6]])   # 2D array
print(arr2)

arr3 = np.array([[1,2,3] , [4,5,6] , [7,8,9]])     #  2D array
print(arr3)

arr4 = np.array([[[1,2,3] , [4,5,6] , [7,8,9]] , [[10,11,12] , [13,14,15] , [16,17,18]]])   # 3D array
print(arr4)

print(arr4.shape)   # shape of the array
print("two array of 3 row , 3 columns")

print(arr[0])   # indexing 1D array
print(arr3[2,0])   # 3rd row , 1st column

# ARRAY operation
a = [1,2,3]
b = [4,5,6]
print(a+b)

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)   # addition of two array
print(a - b)  # subtraction of two array
print(a * b)  # multiplication of two array
print(a / b)  # division of two array

# numpy zero function  ,  make array of n elements but all element are zero
arr5 = np.zeros([3,3])
print(arr5)

# numpy ones function  ,  make array of n elements but all element are one
arr6 = np.ones([3,3])
print(arr6)

# numpy full function ,  make array of n elements but all elements are same and given by user
arr7 = np.full(5, 7)
print(arr7)

# numpy arrange function ,  make array of n elements but all elements are in range of given start and end
arr8 = np.arange(1, 10)
print(arr8)

# numpy linspace function ,  make array of n elements but all elements are in range of given start and end and also user can give number of elements
arr9 = np.linspace(0, 10, 5)
print(arr9)

# numpy sum , mean , max , min function
arr10 = np.array([[1,2,3] , [4,5,6] , [7,8,9]])
print(np.sum(arr10))   # sum of all elements in array
print(np.sum(arr10, axis=0))   # sum of all elements in each column   
print(np.sum(arr10, axis=1))   # sum of all elements in each row      
print(np.mean(arr10))   # mean of all elements in array
print(np.max(arr10))   # max of all elements in array
print(np.min(arr10))   # min of all elements in array


# numpy filtering 
arr11 = np.array([10, 20, 30, 40, 50])
print(arr11[arr11 > 25])