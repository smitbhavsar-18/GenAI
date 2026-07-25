import numpy as np

#Task 1: Createing Numpy Array

onearray = np.arange(1,11)
print(onearray)

twoarray = np.arange(1,10).reshape(3,3)
print(twoarray)

array_list = [10, 20 ,30, 40, 50]

np_array = np.array(array_list)
print(np_array)

print(onearray.shape)
print(twoarray.shape)
print(np_array.shape)

#Task 2 : Math Operations

A = np.array([10,20,30,40])
B = np.array([1,2,3,4])

print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A**2)