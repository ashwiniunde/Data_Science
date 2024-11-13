import matplotlib.pyplot as plt
fig = plt.figure()
songs_69.plot()
plt.legend()

###############################################
fig=plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()
################################################
import numpy as np
data = pd.Series(np.random.randn(500),name='500_ramdom')
fig = plt.figure()
ax = fig.add_subplot(111)
data.hist()
###################
############### DATA FRAME ###############
## 4/4/2024 ##
#What is Pandas data frame?

'''
It is 2D DS
an immutable ,heterogeneous tabular
DS with labled 

'''

##TO check version of pandas
import pandas as pd
pd.__version__
#####################################
#create using constructor
#CREATE pandas dataframe from list
import pandas as pd
technologies=[["Spark",20000,"30days"],["pandas",20000,"40days"]]
df=pd.DataFrame(technologies)
print(df)
"""WE have not given label to columns and indexs DF BY Default assign 
incremental sequence number as label 
here we have given col name and row index while displaying data"""

col_names=["course","free","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=col_names,index=row_label)
print(df)
#################################
df.dtypes


#######################################################
#you can also assign custom 
#data type to column
#set custom to dataframe
import pandas as pd
technologies={
    'course':["Spark","Pyspark","Hadoop","Python","pandas","Oracle","java"],
    'fee':[2000,25000,5000,60000,59000,76987,9000],
    'duration':['10days','20days','30dyas','40days','50days','60days','70days'],
    'discount':[12.2,23.3,56.8,45.4,56.6,6.3,78.2]
    }
df=pd.DataFrame(technologies)
df
print(df.dtypes)


#Convert all types to all possible types
df2=df.convert_dtypes()  #object to string
print(df2.dtypes)
####change all col to same types
df=df.astype(str)
print(df.dtypes)


#change one or multiple columns############ERRROR
df=df.astype({
    "fee":int,"discount":float})
print(df.dtypes)
#Convert data types for all columns in a list#############ERROR
df=pd.DataFrame(technologies)
df.dtypes
cols=['fee','discount']
df[cols]=df[cols].astype('float')
df.dtypes
##Ignores error
df=df.astype({'course':int},errors='ignore')
df.dtypes
#Generate error
#### raise error
df=df.astype({'course':int},errors='raisee')
df.dtypes

#Convert feed col to numeric type
df=df.astype(str)
print(df.dtypes)
df['discount']=pd.to_numeric(df['discount'])
df.dtypes
#####################################################
import pandas as pd
#create DF from dictionary
df.to_csv('data_file.csv')
#############################
df=pd.read_csv('data_file.csv')
#############################
#pandas DF basuc operations
#create DF with null/none to work with example
import pandas as pd
import numpy as np
technologies=({
    'course':["Spark","Pyspark","Hadoop","Python","pandas",None,"Spark","python"],
    'fee':[234,568,7889,7989,np.nan,50000,5600,5600],
    'duration':['30days','55dasy','34days','78dasy','16dasy','56days','','67days'],
    'discount':[2000,7000,6700,67000,5600,600,67900,7000]
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
print(df)
##########################
##5/4/2024
#data frame properties
df.shape
#(8,4)
df.size
#32
df.columns
df.columns.values
df.index
df.dtypes
df.info
#######Training on ML (offline)#########
##1)understanding ,objectives
##2)Data dict
##3)EDA-Exploratory data analysis
##4)Data processing
###5)Model building
##6)Evalution
##7)Deployment
###8)monitoring maintainance
####################################
#Accessing one columns contents
df['fee']
df['duration']
##Accessing 2 columns contents
cols=['fee','duration']
df[cols]
df[['fee','duration']]
#select certain rows and assign it to another dataframe
df2=df[:6]  #show rows from 0 to 5
df2
df3=df[6:]  #show rows from 6 onwards
df3
####################
#df[roes,columns]
#df[:,:]
#df[:] only for rows
df[:]
#df[:,:2] all rows and frist,second columns
#
#accessing certain cell from duration
df['duration'][5]
df['fee'][5]
#Substracting specific values from a column
df['fee']=df['fee']-500
df['fee']
df['discount']=df['discount']-20
df['discount']

###Pandas to manipulate DF
#describe DF
#Describe DF for all numeric cols
df.describe()
#It will show 5 number summary
########################################
#rename()-Renames pandas DF columns
df=pd.DataFrame(technologies,index=row_labels)
#Assign new header by setting new col
df.columns=['A','B','C','D']
df
#############################
#rename col name using rename() method
df=pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']
df
df2=df.rename({'A':'C1','B':'C2'},axis=1)
df2=df.rename({'C':'C3','D':'C4'},axis='columns')
df2=df.rename(columns={'A':'C1','B':'C2'})
df2
#################
#drop rows and cols 
df=pd.DataFrame(technologies,index=row_labels)
#Drop rows bt label
df1=df.drop(['r1','r2'])
df1
#Delete rows and columns by position
df1=df.drop(df.index[1])
df1

df1=df.drop(df.index[[1,3]])
df1

#Delete rows by index range
df1=df.drop(df.index[2:1])
df1
#Whenn you have default index for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1
df1=pd.DataFrame(technologies)
df1=df.drop


#####10/04/2024#####
#to check version of pandas
import pandas as pd
pd._version_

import pandas as pd
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
df=pd.DataFrame(technologies)
print(df)

#explicitely using parameteer anem labels
import pandas as pd
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
df2=df.drop(labels=["fee"],axis=1)
df2
#alternatively u can also use columns instead of labels
df2=df.drop(columns=['fee'],axis=1)
df2
#drop column by index
print(df.drop(df.columns[1],axis=1))
df=pd.DataFrame(technologies)

#using inplace=true
df.drop(df.columns[2],axis=1,inplace=True)
print(df)

##########################################
#DROP two or more columns by label name
df2=df.drop(["Courses","fee"],axis=1)
print(df2)

##########################################
#Drop two or more columns by index
df=pd.DataFrame(technologies)
df
df2=df.drop(df.columns[[0]],axis=1)
print(df2)

############################
#drop columns from list of columns
df=pd.DataFrame(technologies)
print(df.columns)
liscol=['Courses','fee']
df2=df.drop(liscol,axis=1)
print(df2)

#########################
#remove columns from DataFrame inplace
df=pd.DataFrame(technologies)
df.drop(df.columns[1],axis=1,inplace=True)
df

#############################
#pandas select rows by index (position/label)
#accesing rows/columns using index=>iloc is used
#accessing columns using name=>loc

import pandas as pd
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
row_labels=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_lables)
print(df)

df=pd.DataFrame(technologies,index=row_labels)
#below are quick exampels
#df.iloc[startrow:endrow,startcolumn:endcolumn]
df2=df.iloc[:,0:2]
df2
df3=df.iloc[:,0:1]
df3
#this line uses the slicing operator to get dataframe items by index
#the first slice operator[:]indicates to return all rows
#the second slice operator specifies that only columns 
#between 0and 2(excluding 2)should be returned

df2=df.iloc[0:2,:]
df2
#in this case, the first slice is[0:2]
#requesting only rows 0 through 1 of the dataframe.
#the second slice[:]indicates that all columns are required

#slicing specifies rows and columns using iloc attribute
df3=df.iloc[1:2,1:3]
df3
#another example
df3=df.iloc[:,1:3]
df3
#the second operator [1:3] yeilds 1 and 3 only
#select rows by integer index
df2=df.iloc[2] #select Row by index
df2


###11/04/2024
df2=df.iloc[[2,3,6]]#select rows by index list
df2
df2=df.iloc[1:5]#select rows by int index range
df2
df2=df.iloc[:1]#select first row
df2
df2=df.iloc[:3]#select first 3 rows
df2
df2=df.iloc[-1:]
df2
df2=df.iloc[::-1]#show all rows by reverse 
df2
df2=df.iloc[::1] #show all rows by index wise
df2
df2=df.iloc[::2]
df2
df2=df.iloc[::]
df2
df2=df.iloc[-3:] #show last 3 rows
df2
df2=df.iloc[-1:] #show last one row
df2
#############################################
##select rows by index label 
df2=df.loc[['r2']] #select row by label
df2
df2=df.loc[['r2','r3','r6']]  #select rows by index label
df2
df2=df.loc['r1':'r5']
df2
df2=df.loc['r1':'r5':2] #select alternate rows with index label
df2
############################################
#pandas select col by name or index
#By using df[] Notation
df2=df['Courses']
df2
###select multiple columns
df2=df[["Courses","fee","Duration"]]
df2
#using loc[] to take column slice
#loc[] syntax to slice column
#df.loc[:,start:stop:step]
##select multiple columns
df2=df.loc[:,["Courses","fee","Duration"]] #error
df2
#select random columns
df2=df.loc[:,["Courses","Duration","Discount"]]
df2
#select col between 2 columns
df2=df.loc[:,'Courses':'Discount']
df2
#select col by range
df2=df.loc[:,'Duration']
df2
##selet all col upto durationdf2=df.loc[:,'Duration']
df2=df.loc[:,:'Duration']
df2
##select alternate columns
df2=df.loc[:,::2]
df2
#########################################################
#pandas.DataFrame.query() by example
#Query all rows with courses equals 'Spark'
df2=df.query("Courses=='spark'")
print(df2) 
########################################
#not equal to condition
df2=df.query("Courses!='spark'")
df2
########################################
#pandas add col DF
import pandas as pd
import numpy as np

technologies={'Courses':["spark","pyspark","hadoop","python","pandas"],
              'Fee':[20000,25000,26000,22000,24000],
              'Discount':[11.8,23.7,13.4,15.7,12.5]
              }
df=pd.DataFrame(technologies)
print(df)

###########################
##pandas add col DF 
#Add new col to DataFrame
tutor=['ram','sai','sham','om','alok']
df2=df.assign(TutorsAssigned=tutor)
print(df2)
#########################################
#add multiple col to DF
MNCcompanies=['TATA','HCL','INFOSYS','GOOGLE','AMAZON']
df2=df.assign(MNC=MNCcompanies,tutor=tutor)
df2
#######################
#Derive new column from Existing column using lambda function
df=pd.DataFrame(technologies)
df2=df.assign(Discount_percent=lambda x: x.Fee * x.Discount/100)
print(df2)

##################################
#Append col to existing DF
#Add new col to existing DF
df=pd.DataFrame(technologies)
df["MNCcompanies"]=MNCcompanies
print(df)
###################################
#inserting col at sepecific location
df=pd.DataFrame(technologies)
df.insert (0,'Tutors',tutor)
print(df)
######################################
######################################
#Rename multiple columns
import pandas as pd
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
df=pd.DataFrame(technologies)
df.columns
print(df.columns)


df.rename(columns={'Courses':'Course_list'})
df
df.rename(columns={'Courses':'Course_list'},axis='columns')
df.columns
print(df.columns)


######################
##15/04/2025##

import pandas as pd
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
df=pd.DataFrame(technologies)
df.columns
print(df.columns)
############################################
##########################################
#quick exampl of get the number of rows inDF
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count
column_count=len(df.axes[1])
column_count

######################################
df=pd.DataFrame(technologies)
row_count=df.shape[0] #number of rows
row_count
col_count=df.shape[1]#number of columns
print(row_count)
print(col_count)

####################################333
#pandas apply function to col
#using DF.apply() to apply function add col
import pandas as pd
import numpy as np
data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]}
df=pd.DataFrame(data)
print(df)


def add_3(x):
    return x+3
df2=df.apply(add_3)
df2
df2=((df.A).apply(add_3)) #only change A column by adding 3
df2
##########################

#using apply function single column
def add_4(x):
    return x+4
df["B"]=df["B"].apply(add_4)
df["B"]


#apply on multiple columns
df[['A','B']]=df[['A','B']].apply(add_4) #add 4 in  A and B column
df

#apply a lambda function to each column
df2=df.apply(lambda x:x+10) #added 10 in every column
df2


##################################
#transform fun
def add_2(x): #add  2 in each column
    return x+2
df=df.transform(add_2)
print(df)


##################################
#map() function for single column
data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]}
df=pd.DataFrame(data)
print(df)
df['A']=df['A'].map(lambda A:A/2) #It will divide column A by 2
print(df)

#############################################
#using numpy function on single column
#using DataFrame.apply and []operator
data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]}
df=pd.DataFrame(data)
print(df)
import numpy as np
df['A']=df['A'].apply(np.square) #IT will give square of column A
print(df)

########################################
#using NumPy.square() method
#Using numpy.square() and [] operator
df['A']=np.square(df['A'])
print(df)

####################################
#Pandas groupby() with Examples

import pandas as pd
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","Hadoop","spark","python","Na"],
              'fee':[22000,25000,23000,24000,26000,25000,25000,22000,1500],
              'Duration':["30days","50days","35days","40days","60days","50days","55days","30days","50days"],
              'Discount':[11.8,23.7,13.4,15.7,18.4,25.4,18.4,11.8,13.4]
              }
df=pd.DataFrame(technologies)
print(df)
#for single column
df2=df.groupby(['Courses']).sum()
print(df2)
#for multiple columns
df2=df.groupby(['Courses','fee']).sum() ###########ee
print(df2)

############################
#add index to th group data
#add the indexx to the rows
df2=df.groupby(['Courses','fee']).sum().reset_index() 
print(df2)

#########################################
#get the list of all column name headers as a list
column_headers=list(df.columns.values)
print("the column Header::",column_headers) #gives list of columns
############################33
#Using list(df) to get column headers as a list
column_header=list(df)
column_headers

#########################################################
######### 16/04/2024 ############ Tuesday ########
##pandas Shuffle DF rows
import pandas as pd
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,18.4,25.4,18.4]
              }
df=pd.DataFrame(technologies)
print(df)
#Pandas Shuffle Df row 
#shuffle the df rows and return all rows
df1=df.sample(frac =1) 
print(df1)
#####################################
#It will create new index starting from 0(zero)
df1=df.sample(frac=1).reset_index()
print(df1)
####################################
#drop shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
print(df1)
#######################################
#inner join show common cols
import pandas as pd
technologies={'course':["spark","pyspark","python","pandas"],
              'fee':[20000,25000,22000,30000],
              'duration':['30days','40days','35days','50days']}
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)
 
import pandas as pd
technologies2={'course':['spark','java','python','go'],
               'discount':[2000,23000,1200,2000]}
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)
#pandas join
df3=df1.join(df2,lsuffix="_left",rsuffix="_roght")
print(df3)
###########################################
#pandas inner join DataFrame
df3=df1.join(df2,lsuffix="_left",rsuffix="_roght",how='inner')
print(df3)
#######################################
#pandas left join dataframe
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='left')
print(df3)
#pandas right join
df3=df1.join(df2,lsuffix="_left",rsuffix="_roght",how='right')
print(df3)
############################################
#Pandas Merge
import pandas as pd
technologies={'course':["spark","pyspark","python","pandas"],
              'fee':[20000,25000,22000,30000],
              'duration':['30days','40days','35days','50days']}
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)
 
import pandas as pd
technologies2={'course':['spark','java','python','go'],
               'discount':[2000,23000,1200,2000]}
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)
#using pandas merge
df3=pd.merge(df1,df2)
print(df3)

#using DataFraem.merge()
df5=df1.merge(df2) #same result as above
print(df5)
##############################################
#use pandas.concat() to connect two DF
import pandas as pd
df=pd.DataFrame({'course':["spark","pyspark","python","pandas"],
                 'fee':[20000,25000,22000,24000]})
df1=pd.DataFrame({'course':["pandas","hadoop","hyperion","java"],
                  'fee':[25000,25200,24500,24900]})
data=[df,df1]
df2=pd.concat(data) #connect 2 series 
df2
#############################4
#concat multiple DATDFRAME 
import pandas as pd
df=pd.DataFrame({'course':["spark","pyspark","python","pandas"],
                 'fee':[20000,25000,22000,24000]})
df1=pd.DataFrame({'course':["unix","hadoop","hyperion","java"],
                  'fee':[25000,25200,24500,24900]})
df2=pd.DataFrame({'duration':['30days','40days','35days','60days'],
                  'discount':[1000,2300,2500,3000]})
#append multiple df
df3=pd.concat([df,df1,df2])
print(df3)

#########################################
##18/04/2024
#write DF to excel file
df.to_excel('c/10-python/Course.xlsx')
##################################
import pandas as pd
df=pd.read_excel()

####################################
#using series.values.tolist()
col_list=df.course.values ##convert a course into list['spark','pyspark','python','pandas']
print(col_list)
col_list=df.course.values.tolist()
print(col_list)

##using series.values.tolist()
col_list=df["course"].values.tolist()
print(col_list)

##using list() function
col_list=list(df["course"])
print(col_list)

