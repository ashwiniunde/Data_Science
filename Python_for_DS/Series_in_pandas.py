# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 08:26:03 2025

@author: ashwi
"""
# SERIES :A Pandas Series is basically a one-dimensional 
    # labeled array. It can hold any data type — integers, 
    # strings, floats, even Python objects.
import pandas as pd

# From a list
data = [10, 20, 30, 40]
series1 = pd.Series(data)
print(series1)
"""
0    10
1    20
2    30
3    40
dtype: int64
"""

#Adding index
data = [10, 20, 30, 40]
labels = ['a', 'b', 'c', 'd']
series2 = pd.Series(data, index=labels)
print(series2)
"""
a    10
b    20
c    30
d    40
dtype: int64

"""

#From a DIctionary
data = {'Python': 90, 'Java': 80, 'C++': 75}
series3 = pd.Series(data)
print(series3)
"""
Python    90
Java      80
C++       75
dtype: int64
"""

# Accessing elements
print(series2['b'])      # Output: 20
print(series2[1])        # Output: 20 (position-based)


#  Basic Operations
print(series2 + 5)  # # Adds 5 to each element
"""
a    15
b    25
c    35
d    45
dtype: int64
"""


print(series2 * 2)        # Multiplies each by 2

print(series2.mean())     # Average

print(series2.max())      # Maximum




data = [10, None, 30, None]
series4 = pd.Series(data)
print(series4.isnull())     # Check for NaN values
"""
0    False
1     True
2    False
3     True
dtype: bool
"""
print(series4.fillna(0))    # Replace NaNs with 0
"""
0    10.0
1     0.0
2    30.0
3     0.0
dtype: float64
"""

data = [100, 200, 300, 400]
labels = ['x', 'y', 'z', 'w']
s = pd.Series(data, index=labels)

print(s['y'])     # Label-based
print(s.iloc[1])  # Position-based


#######################################################
import pandas as pd
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
series_np = pd.Series(arr)

# Square of each element
print(series_np ** 2)

"""
0     1
1     4
2     9
3    16
4    25
dtype: int32
"""

# Natural log
print(np.log(series_np))
"""
0    0.000000
1    0.693147
2    1.098612
3    1.386294
4    1.609438
dtype: float64
"""

s = pd.Series([15, 22, 8, 99, 34, 70])
# Get all values greater than 30
print(s[s > 30])
"""
3    99
4    34
5    70
dtype: int64
"""

# Updating Values
s = pd.Series([5, 10, 15, 20])
s[2] = 100     # Change 15 to 100
print(s)

# Combine Two Series (Add/Multiply)

s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['a', 'b', 'c'])

print(s1 + s2)

"""
a    5
b    7
c    9
dtype: int64
"""

print(s1 * s2)
"""
a     4
b    10
c    18
dtype: int64
"""

#Plotting


import matplotlib.pyplot as plt

s = pd.Series([5, 10, 15, 7, 3], index=['A', 'B', 'C', 'D', 'E'])
s.plot(kind='bar', color='skyblue')
plt.title("Sample Bar Chart from Series")
plt.show()
 
