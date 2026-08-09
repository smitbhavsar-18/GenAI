import numpy as np

#Task 1: Createing Numpy Array

onearray = np.arange(1,11)
print("1d array:", onearray)

twoarray = np.arange(1,10).reshape(3,3)
print("2d array:", twoarray)

array_list = [10, 20 ,30, 40, 50]

np_array = np.array(array_list)
print("1d array:", np_array)

print("shape of 1d array:", onearray.shape)
print("shape of 2d array:", twoarray.shape)
print("shape of 1d array from list:", np_array.shape)

#Task 2 : Math Operations

A = np.array([10,20,30,40])
B = np.array([1,2,3,4])

print("sum :" , A+B)
print("difference :" , A-B)
print("product :" , A*B)
print("quotient :" , A/B)
print("square :" , A**2)

#Task 3: Mathematical Functions

values = np.array([2,4,6,8,10])

print("square root :" , np.sqrt(values))
print("exponential :" , np.exp(values))
print("logarithm :" , np.log(values))
print("sum :" , np.sum(values))
print("cumulative sum :" , np.cumsum(values))


#Task 4: Aggeregate Functions

data = np.array([[10,20,30],[40,50,60],[70,80,90]])

print("sum along axis 1 :" , np.sum(data, axis=1))
print("sum along axis 0 :" , np.sum(data, axis=0))
print("minimum :" , np.min(data))
print("maximum :" , np.max(data))
print("mean :" , np.mean(data))

#Task5 : Stactistical Operations

marks = np.array([75,85,90,66,72,99,95,60])

print("mean :" , np.mean(marks))
print("median :" , np.median(marks))
print("variance :" , np.var(marks))
print("standard deviation :" , np.std(marks))
print("maximum :" , np.max(marks))
print("minimum :" , np.min(marks))
print("range :" , np.max(marks) - np.min(marks))

#Task 6:Percentiles & sorting

print("sorted :" , np.sort(marks))
print("25th percentile :" , np.percentile(marks, 25))
print("50th percentile :" , np.percentile(marks, 50))
print("75th percentile :" , np.percentile(marks, 75))

avg = np.mean(marks)
count = 0
for mark in marks:
    if mark > avg:
        count += 1
print("Number of students above average marks :" , count)

#Task 7 :Sales Analysis

sales =np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

print("Total sales :" , np.sum(sales))
print("Average sales :" , np.mean(sales))
print("Maximum sales :" , np.max(sales))
print("Minimum sales :" , np.min(sales))
print("standard deviation of sales :" , np.std(sales))

avg = np.mean(sales)
count = 0
for sale in sales:
    if sale > avg:
        count += 1
print("Number of sales above average :" , count)