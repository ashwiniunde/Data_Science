#NumPy::numpy is an open-source Python library that provides scientific and 
#mathematical computing capabilities. It's known for its support for multi-dimensional 
#arrays and matrices, and for its many high-level mathematical functions

#Array In numpy
#Create ndarray
import numpy as np
arr=np.array([10,20,30,40,50])
#This is an 1 dimensional array which will be printed with help of numpy
print(arr)
#OUTPUT=>>[10 20 30 40 50]


# 2 dimensional array is calles Matrix
import numpy as np
arr1=np.array([[10,20,30],[40,50,60]])
print(arr1)
#OUTPUT=>>[[10,20,30] [40,50,60]]


#More than 2 dimensional array is called Tensor
#Creating Multidimesional array
import numpy as np     
arr2=np.array([[[10,20,30],[40,50,60],[70,80,90]]])##3D array
print(arr2)
#OUTPUT=>>
#[[[10 20 30]
#  [40 50 60]
#  [70 80 90]]]


# Represent the minimum number dimension of array
import numpy as np
arr=np.array([10,20,30],ndmin=3) ## 3D array [[[ elements ]]]
print(arr)
#OUTPUT=>>array([[[10, 20, 30]]])

import numpy as np
arr=np.array([10,20,30],ndmin=2)
print(arr)
#OUTPUT=>>array([[10, 20, 30]])


#conversion of an integer into into complex number
import numpy as np
arr=np.array([1,2,3],dtype=complex) 
print(arr)
#OUTPUT=>>[1.+0.j 2.+0.j 3.+0.j]


#Finding the size of each item in the array
arr=np.array([10,20,30])
print(arr.itemsize)
#OUTPUT=>>4

arr=np.array([10.3,20.5,20.8])
print(arr.itemsize)
#OUTPUT=>>8


##Get the size and shape of array
import numpy as np
arr=np.array([[10,20,30,40],[60,70,80,90]])
print("Array size:",arr.size)
#OUTPUT=>>Array size: 8
print("Shape of array:",arr.shape)
#OUTPUT=>>Shape of array: (2, 4)


###creating array list with type float
arr=np.array([[10,20,30],[40,50,60]],dtype=float)
print("Array createed using list:",arr)
#OUTArray createed using list: [[10. 20. 30.]
 #[40. 50. 60.]]


##creating sequence ot integers using arange()
#from 0 to 20 with step of 3
#arange(start,end,increment)
arr=np.arange(0,20,3)
print("a sequential array with steps of 3::",arr)
#OUTPUT=>>a sequential array with steps of 3:: [ 0  3  6  9 12 15 18]


##Array indexing 
##accessing single element using index
arr=np.arange(11)
print(arr)
#OUTPUT=>> [ 0  1  2  3  4  5  6  7  8  9 10]
print(arr[2])
# 2
print(arr[-5])
# 6
print(arr[-2])
# 9


##multi dimensional array Indexing
import numpy as np
arr=np.array([[10,20,30,40,50],[60,70,80,90,100]])

print(arr.shape)
#(2,5)
print(arr[1,1])
# 70
print(arr[0][2])
#30
print(arr[0,4])
# 50
print(arr[1,-1])
#100


#Access array element using slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2] #start:end:in step of 2
print(x)
#OUTPUT=>>[1 3 5 7]
