#NumPy::numpy is an open-source Python library that provides scientific and 
#mathematical computing capabilities. It's known for its support for multi-dimensional 
#arrays and matrices, and for its many high-level mathematical functions


##checking version of numpy
import numpy as np 
print(np.__version__)


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


x=arr[-2:3:1]
print(x)
# [] 

x=arr[-2:3:-1]
print(x)
#[8 7 6 5 4]

print(arr[-2:10])
#[8 9]


#indexing in numpy
import numpy as np
multi_arr = np.array([[10,20,30,40],
                      [40,50,70,90],
                      [60,10,70,80],
                      [30,90,40,30]])
multi_arr

multi_arr[1,2] #To access the values at row 1 and col 2
multi_arr[1,:] # row 1 and all columns
multi_arr[:,1] #all rows and a 1 col

x=multi_arr[:3,::2]
print(x)


#Integer array indexing ###############
arr=np.arange(35).reshape(5,7) #5 rows and 7 col
print(arr)

#Boolean array indexing
import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr)
#output:: [[ 0  1  2  3]
#        [ 4  5  6  7]
#       [ 8  9 10 11]]




#########################################
rows=np.array([False,True,True]) #second and third row
rows
wanted_rows=arr[rows,:]
print(wanted_rows
 #OUTPUT=>>[[ 4  5  6  7]
 #          [ 8  9 10 11]]    


rows=np.array([True,False,True]) #it will give first and third row
rows
wanted_rows=arr[rows,:]
print(wanted_rows)
 #OUTPUT=>>[[ 0  1  2  3]
 #          [ 8  9 10 11]]


rows=np.array([False,True,True]) #second and third row
rows
wanted_rows=arr[rows,:]
print(wanted_rows)
 #OUTPUT=>> [[ 4  5  6  7]
 #           [ 8  9 10 11]]


#####################################
#numpy.asarray():
#Use asarray()
list=[20,40,60,80]
array=np.asarray(list)
print("Array::: ",array)
 #OUTPUT=>> Array:::  [20 40 60 80]

print(type(array))
 #OUTPUT=>> <class 'numpy.ndarray'>


############################################
#Numpy Array Properties
#ndarray.shape
#ndarray.size
#ndarray.itemsize
#ndarray.dtype

#ndarray.shape
array=np.array([[1,2,3],[4,5,6]])
array
print(array.shape)
#(2,3)
#Resize the array
array=np.array([[10,20,30],[40,50,60]])
array.shape=(3,2)
print(array)
#output:: [[10 20]
#         [30 40]
#         [50 60]]

#reshape usage
array=np.array([[10,20,30],[40,50,60]])
new_array=array.reshape(3,2)
print(new_array)
# output::[[10 20]
#         [30 40]
#          [50 60]]

##################################################
#Arithmetic Operation
import numpy as np
arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,2,3,4])
#add()
add_arr=np.add(arr1,arr2)
print(f"Adding two arrays:\n{add_arr}")
#OUTPUT=>> Adding two arrays:
 #[[ 1  3  5  7]
# [ 5  7  9 11]
# [ 9 11 13 15]
# [13 15 17 19]]



#subtract()
import numpy as np
arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,2,3,4])
sub_array=np.subtract(arr1,arr2)
print(f"Substrating two array :\n{sub_array}")
#output:: Substrating two array :
 #[[-1 -1 -1 -1]
 #[ 3  3  3  3]
 #[ 7  7  7  7]
 #[11 11 11 11]]


#multiplication
import numpy as np
arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,2,3,4])
mul_array=np.multiply(arr1,arr2)
print(mul_array)



##divide()
div_array=np.divide(arr1,arr2)
print(div_array)

#####################################
#To perform Reciprocal operation
import numpy as np
arr1=np.array([50,10.3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print(f"  Array  reciprocal function to array:\n{rep_arr1}")
#Array  reciprocal function to array:
#[0.02       0.09708738 0.2        1.         0.005     ]


########################
#numpy.power()
arr1=np.array([3,10,5])
pow_arr1=np.power(arr1,3)
print(f"The power of {arr1} is:\n{pow_arr1}")
# [  27 1000  125]


arr1=np.array([3,10,5])
arr2=np.array([3,2,1])
print("My second array is :\n",arr2)
pow_arr2=np.power(arr1,arr2)
print(pow_arr2)
#OUTPUT=>>[ 27 100   5]


#To perform mod function on numpy array
import numpy as np
arr1=np.array([7,20,13])
arr2=np.array([3,5,2])
arr1
#OUTPUT=>>array([ 7, 20, 13])
arr1.dtype  #dtype('int32')
#mod()
mod_arr=np.mod(arr1,arr2)
print("After applying mod function to array",mod_arr)
#After applying mod function to array [1 0 1]

from numpy import empty 
a=empty([3,3])
print(a)


#create zero array
from numpy import zeros
a=zeros([3,5])
print(a)


#creaete one array
from numpy import ones
a=ones([5])
print(a)
# [1. 1. 1. 1. 1.]


#create array with vstack
from numpy import array
from numpy import vstack
#create first list
a1=array([1,2,3])
print(a1)
#second list
a2=array([5,6,7])
print(a2)
#vertical stack
a3=vstack((a1,a2))
print(a3)
print(a3.shape) #(2,3)

###############################################
#create array with hstack
from numpy import array
from numpy import hstack
a1=array([1,2,3])
print(a1)
#second list
a2=array([4,5,6])
print(a2)
#creaet horozontal stack
a3=hstack((a1,a2))
print(a3)
print(a3.shape)


##stack overflow ::online platform to correct mistake
#index data
from numpy import array
data=array([10,20,30])
print(data[5]) ## array index out of bond
print(data[2]) # 30
print(data[0]) #10

###imp nb
from numpy import array
data=array([[11,22],[33,44],[55,66]])
print(data)
print(data[0, ]) #0 th row and all columns
#[11 22] 


#############################
#slice a 1D array
from array import array
data=array([11,22,33,44,55])
print(data[1:4])

print(data[-2:])
print(data[:-2])


###################
#split input and output data
from numpy import array
data=array([[11,22,33],
           [44,55,66],
           [77,88,99]])
#separate data
X,y=data[:,:-1],data[:,-1]
X
#array([[11, 22],
#      [44, 55],
#     [77, 88]])
y
#array([33, 66, 99])
#data[:,:-1] all rows and remove -1  col

##########################################
#broadcasting scalar to 1D array
from numpy import array
a=array([1,2,3])
print(a)
#define scalar
b=2
print(b)
#broadcast
c=a+b #addition of 2 in element of a as 1+2=3
print(c)


#vector 
'''What is  vector L1 Norm
    The l1 norm is calculated as the sum of the 
    absolute vector values,
    where the absulute value of scalar uses the notation|a1|
    tn effect the norm
    is a calculation of manhattan dist
    from the origin of vector
    ||v||1=|a1|+|a2|+|a3|
'''
from numpy import array
from numpy.linalg import norm
#define vector
a=array([1,2,3])
print(a)
#calculate norm
l1=norm(a,1)
print(l1)


#vector L2 norm
'''
the notation of l2 norm of a vector 


to calculate 
take the square root of 

'''
from numpy import array
from numpy.linalg import norm
#define vector
a=array([1,2,3])
print(a)
#calculate norm
l2=norm(a) #1+4+9=14 under root of 14 is 3.74
print(l2)

##########################################
#triangular matrices
from numpy import array
from numpy import tril
from numpy import triu
#define square matrix
M=array([
    [1,2,3],
    [1,2,3],
    [1,2,3]
    ])
print(M)
#lower triangular matrix


#####Diagonal matrix
from numpy import array
from numpy import diag
#define square matrix
M=array([
    [1,2,3],
    [1,2,3],
    [1,2,3]])
print(M)
#extract diagonal vector
d=diag(M)
print(d)
#create diagonal matrix from vector
D=diag(d)
print(D)
#########################
#identity matrix
from numpy import identity
I=identity(3)
print(I)
#[[1. 0. 0.]
 #[0. 1. 0.]
 #[0. 0. 1.]]
##############
lower=tril(M)
lower
print(lower)
#[[1 0 0]
# [1 2 0]
 #[1 2 3]]
#upper triangular matrix
upper=triu(M)
print(upper)
# [[1 2 3]
 #[0 2 3]
 #[0 0 3]]
######################


#####Diagonal matrix
from numpy import array
from numpy import diag
#define square matrix
M=array([
    [1,2,3],
    [1,2,3],
    [1,2,3]])
print(M)
#extract diagonal vector
d=diag(M)
print(d)
#create diagonal matrix from vector
D=diag(d)
print(D)
#########################
#identity matrix
from numpy import identity
I=identity(3)
print(I)
#[[1. 0. 0.]
 #[0. 1. 0.]
 #[0. 0. 1.]]
##############
