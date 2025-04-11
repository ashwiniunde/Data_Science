# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 15:21:47 2025

@author: ashwi
"""
#Pandas: Pandas is a powerful, open-source Python library 
 # for data manipulation and analysis, particularly known
 # for its flexible data structures like Series (1D labeled
 # array) and DataFrames (2D labeled data). 

"""
Series: A one-dimensional labeled array capable of holding
       data of any type (integers, strings, Python objects,etc.). 
DataFrame: A two-dimensional labeled data structure, similar 
      to a table with rows and columns, used for storing and 
      manipulating tabular data.
"""
import pandas as pd
import numpy as np
technologies = {
'Courses':["Spark","Pyspark","Hadoop","Pyhton"],
'Fee':[20000,25000,26000,22000],
'Duration':['','40days',np.nan,None],
'Discount':[1000,2300,1500,1200]
}

indexes=['r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=indexes)

print(df)
"""
nan is atype 
np.nan float
"" empty sstring
"""
df=pd.DataFrame(technologies,index=indexes)
df2=df.dropna()
print(df2)

################################
#How to clean empty string

#first drop rows with Nan (np.nan and None)
df_clean = df.dropna(subset=['Duration'])

#Then drop row with empty sting
df_clean = df_clean[df_clean['Duration'] != '']
print(df_clean)
########################

##Changes  all colums to same type in Pandas
#df.astype(str) convert all cols into string

df = df.astype(str)
print(df.dtypes)
"""
Courses     object or string
Fee         object
Duration    object
Discount    object
dtype: object
"""

###################################

#changes type for one or multiple columns in pandas
#change type for one or multiple cols

df=df.astype({"Fee":int,"Discount":float})
print(df.dtypes)

"""
Courses      object
Fee           int32
Duration     object
Discount    float64
dtype: object

Why does it become int32 ?

Pandas internally choosses the most efficient
platform-dependent Numpy dtype that corresponding to 
python int. This depends on your operating system
and python numpy version.
on 32 - bit system int usuually maps to int 32
on 64- bit system int often maps to int 64

"""

# we can explicitely control the dtype like below
df=df.astype({"Fee":"int64","Discount":"float64"})
print(df.dtypes)
"""
print(df.dtypes)
Courses      object
Fee           int64
Duration     object
Discount    float64
dtype: object

"""
############################################
#Convert all datatypes for all cols in a list

df=pd.DataFrame(technologies)
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
df.dtypes
"""  
Courses      object
Fee         float64
Duration     object
Discount    float64
dtype: object

converted into float col fee and discount
"""
#by using a loop
for col in ['Fee','Discount']:
    df[col] = df[col].astype('float')
df.dtypes

#####################################################
#raise or Ignore Error when convert cols type fail

df=df.astype({'Courses':int},errors='ignore')
#here we ignore the error i.e convert str to int 
df.dtypes
#Generate error
df=df.astype({'Courses':int},errors='raise')
df.dtypes
##########################################################
#using DataFrame .to_numeric() to  convert numerical types 
#convert feed col to numeric type

df['Fee'] = pd.to_numeric(df['Fee'])
df.dtypes

#np.nan : float() data types : by default convert into float64
#convert multiple numeric types using apply() method
#convert fee and discount in numeric

df=pd.DataFrame(technologies)
df.dtypes
df[['Fee','Discount']]= df[['Fee','Discount']].apply(pd.to_numeric)
df.dtypes

##########################################
#Quick examples of Get the number of rows in DataFrame
rows_count=len(df.index)
rows_count # 4
rows_count=len(df.axes[0])
rows_count # 4

###################################################
df=pd.DataFrame(technologies)
row_count=df.shape[0]
col_count=df.shape[1]
row_count
col_count


###############################################
#pandas Apply fun to cols
# Below are quick ex
# unsing Dataframe.apply() to apply function add col

import pandas as pd
import numpy as np
data=[(3,5,7),(2,4,6),(5,8,9)]
df=pd.DataFrame(data,columns=['A','B','C'])
df

def add_3(x):
    return x+3 
df2=df.apply(add_3)
df2

###########################################
#Using apply function single col
def add_4(x):
    return x+4
df["B"]= df["B"].apply(add_4)
df["B"]

# for multiple cols
df=pd.DataFrame(data,columns=['A','B','C'])
df[["A","B"]]=df[["A","B"]].apply(add_4)
df[["A","B"]]

df=pd.DataFrame(data,columns=['A','B','C'])

#apply lamda function to each column
df2=pd.DataFrame(data,columns=["A","B","C"])
df2=df.apply(lambda x:x+10)
df2
##################################
#apply lambda function to single columns
#using Dataframe .apply() and lambda function
df["A"] =df["A"].apply(lambda x:x-2)
df
#######################################
#using pandas.DataFrame colums
#to apply functio cols
# Using DataFrame.transform()
def add_2(x):
    return x+2 
df=df.transform(add_2)
df 

#########################################
#using pandas.DataFrame.map() to single columns
df["A"] = df["A"].map(lambda A:A/2)
df

#################################################################
#################################################################
#Using Numpy  function on Single Columns
# Using DataFrame.apply() & [] operator


import pandas as pd
import numpy as np
data=[(3,5,7),(2,4,6),(5,8,9)]
df=pd.DataFrame(data,columns=['A','B','C'])
df

"""
  A  B  C
0  3  5  7
1  2  4  6
2  5  8  9
"""
df['A']=df['A'].apply(np.square)
print(df)
"""
   A  B  C
0   9  5  7
1   4  4  6
2  25  8  9
"""

###########################################
# Using Numpy.square() Method
# Using numpy.square()  and [] operator
df['A']=np.square(df['A'])
df
"""
   A  B  C
0   81  5  7
1   16  4  6
2  625  8  9
"""
#######################################
# Pandas groupby() with Examples
import pandas as pd
technologies={'Courses':["spark","Pyspark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
              'Fee':[22000,25000,23000,24000,26000,25000,25000,22000,1500],
              'Duration':["30days","50days","55days","40days","60days","35days","30days","50days","40days"],
              'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
              }

df = pd.DataFrame(technologies)
print(df)
"""
 Courses    Fee Duration  Discount
0    spark  22000   30days    1000.0
1  Pyspark  25000   50days    2300.0
2   Hadoop  23000   55days    1000.0
3   Python  24000   40days    1200.0
4   Pandas  26000   60days    2500.0
5   Hadoop  25000   35days       NaN
6    Spark  25000   30days    1400.0
7   Python  22000   50days    1600.0
8       NA   1500   40days       0.0
"""

# Use groupby for single column to compute the sum of similar type row
df2=df.groupby(['Courses']).sum()
df2
"""
 Fee  Discount
Courses                 
Hadoop   48000    1000.0
NA        1500       0.0
Pandas   26000    2500.0
Pyspark  25000    2300.0
Python   46000    2800.0
Spark    25000    1400.0
spark    22000    1000.0
"""
# For multiple col
df2 = df.groupby(['Courses','Duration']).sum()
print(df2)
"""
  Fee  Discount
Courses Duration                 
Hadoop  35days    25000       0.0
        55days    23000    1000.0
NA      40days     1500       0.0
Pandas  60days    26000    2500.0
Pyspark 50days    25000    2300.0
Python  40days    24000    1200.0
        50days    22000    1600.0
Spark   30days    25000    1400.0
spark   30days    22000    1000.0
"""
#Add index to the gruopby data
# add row index to the group by result
df2 = df.groupby(['Courses','Duration']).sum().reset_index()
print(df2)

"""
 Courses Duration    Fee  Discount
0   Hadoop   35days  25000       0.0
1   Hadoop   55days  23000    1000.0
2       NA   40days   1500       0.0
3   Pandas   60days  26000    2500.0
4  Pyspark   50days  25000    2300.0
5   Python   40days  24000    1200.0
6   Python   50days  22000    1600.0
7    Spark   30days  25000    1400.0
8    spark   30days  22000    1000.0
"""

###############################################
#Pandas Get col names from DataFrame
import pandas as pd
import numpy as np

technologies = {
'Courses':["Spark","Pyspark","Hadoop","Pyhton","Pandas"],
'Fee':[22000,25000,23000,24000,26000],
'Duration':['30days','50days','30days',None,np.nan],
'Discount':[1000,2300,1000,1200,2500]
}
df=pd.DataFrame(technologies)
print(df)

#get th list of all col names from headers
col_headers= list(df.columns.values)
print("The Column Header:",col_headers)
"""
The Column Header: ['Courses', 'Fee', 'Duration', 'Discount']
"""

# Using list(df) to get the col headers as l list
col_headers= list(df.columns)
col_headers
"""
['Courses', 'Fee', 'Duration', 'Discount']
"""

# Using list(df) to get col name
col_headers= list(df)
col_headers
#  ['Courses', 'Fee', 'Duration', 'Discount']


#########################################
#Pandas shuffle DataFrame Rows
technologies = {
'Courses':["Spark","Pyspark","Hadoop","Pyhton","Pandas","Oracle","java"],
'Fee':[20000,25000,26000,22000,24000,21000,22000],
'Duration':['30days','40days','35days','40days','60days','50days','55days'],
'Discount':[1000,2300,1500,1200,2500,2100,200]
}

df=pd.DataFrame(technologies)
print(df)
"""
 Courses    Fee Duration  Discount
0    Spark  20000   30days      1000
1  Pyspark  25000   40days      2300
2   Hadoop  26000   35days      1500
3   Pyhton  22000   40days      1200
4   Pandas  24000   60days      2500
5   Oracle  21000   50days      2100
6     java  22000   55days       200
"""
#Shuffle th Dataframe rows and return all rows
df1 = df.sample(frac = 1)
df1

"""
index will shuffled here
Courses    Fee Duration  Discount
2   Hadoop  26000   35days      1500
6     java  22000   55days       200
3   Pyhton  22000   40days      1200
5   Oracle  21000   50days      2100
4   Pandas  24000   60days      2500
0    Spark  20000   30days      1000
1  Pyspark  25000   40days      2300
"""

df1 = df.sample(frac = 1).reset_index()
print(df1)

"""
index  Courses    Fee Duration  Discount
0      2   Hadoop  26000   35days      1500
1      3   Pyhton  22000   40days      1200
2      4   Pandas  24000   60days      2500
3      5   Oracle  21000   50days      2100
4      6     java  22000   55days       200
5      1  Pyspark  25000   40days      2300
6      0    Spark  20000   30days      1000
"""
# Drop shuffle index
df1=df.sample(frac = 1).reset_index(drop=True)
print(df1)

"""
Courses    Fee Duration  Discount
0   Oracle  21000   50days      2100
1     java  22000   55days       200
2    Spark  20000   30days      1000
3   Pandas  24000   60days      2500
4   Hadoop  26000   35days      1500
5   Pyhton  22000   40days      1200
6  Pyspark  25000   40days      2300
"""

#############################################################
   






