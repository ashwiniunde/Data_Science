'''
Matplotlib::Matplotlib is a popular data visualization library in Python. 
It provides a variety of tools to create static, interactive, and 
animated plots and graphs. It is widely used by data scientists, analysts, 
and engineers to visualize data in meaningful ways, which helps with better analysis and insights.
'''

#Write a python program to draw linewith suitable label in the
import matplotlib.pyplot as plt
X=range(1,50)
Y=[value *3 for value in X]
print("value of X:")
print(*range(1,50))

'''
this is equivalent to -
i in range (1,50)
print(i,end=' ')
'''
print("Values of Y(thrice of X) ::")
print(Y)

######################
#plot lines and/or marker to the axes
plt.plot(X,Y)
#set the x axis label of current axis 
plt.xlabel('x-axis')
##set the y axis label of current axis
plt.ylabel('y-axis')
#set a title
plt.title('Draw a line.')
#Display the figure
plt.show()


################################
import matplotlib.pyplot as plt

x=[1,2,3]

y=[2,4,1]
#plot lines and/or maker to the axes
plt.plot(x,y)
###set the x axis label of current axis
plt.xlabel('x-axis')
###set the y axis label of current axis
plt.xlabel('y-axis')
#Set a title
plt.title('Sample graph!')
#display fig
plt.show()

##############################################
#Write a python program to plot two or more lines
#on same plot with suitable legends of each line
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]

#ploting the line 1 point
plt.plot(x1,y1,label="line 1")
#ploting the line 2 points
plt.plot(x2,y2,label="line 2")
plt.xlabel('x-axis')
#set the y axis label to current axis.
plt.ylabel('y-axis')
#set the title 
plt.title('two or more line')
#show legend on plot
plt.legend()
#display a fig
plt.show()

##########################
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]

#ploting the line 1 point
plt.plot(x1,y1,label="line 1")
#ploting the line 2 points
plt.plot(x2,y2,label="line 2")
plt.xlabel('x-axis')
#set the y axis label to current axis.
plt.ylabel('y-axis')
#set 
plt.title('two or more line with diff widths and color')
#display fig
plt.plot(x1,y1,color='blue',linewidth=3,label='line-width-2')
plt.plot(x2,y2,color='red',linewidth=5,label='line-width-2')


import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]

#ploting the line 1 point
plt.plot(x1,y1,label="line 1")
#ploting the line 2 points
plt.plot(x2,y2,label="line 2")
plt.xlabel('x-axis')
#set the y axis label to current axis.
plt.ylabel('y-axis')
#set 
plt.title('two or more line with diff widths and color')
#display fig
plt.plot(x1,y1,color='blue',linewidth=3,label='line1-dotted',linestyle='dotted')
plt.plot(x2,y2,color='red',linewidth=5,label='line2-dashed',linestyle='dashed')
plt.title('graph')
plt.legend()
plt.show()

##################################################
#25/04/2024
#Introducing marker
import matplotlib.pyplot as plt
x=[1,4,5,6,7]
y=[2,6,3,6,3]
plt.plot(x,y,color='red',linestyle='dashed',linewidth=3,
         marker='o',markerfacecolor='blue',markersize=12)
#set y limit of axis
plt.ylim(1,8)
plt.xlim(1,8)

plt.xlabel('x=axis')
plt.ylabel('y-axis')
plt.title('Display marker')
plt.show()
###################################
#vertical bar graph
import matplotlib.pyplot as plt
x=['java','python','PHP','js','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,7.6]
x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color='blue')
plt.xlabel("Languages")
plt.ylabel("popularity")
plt.title("pooularity of programming language \n"+
          "Worldwide,Oct 2017 compared to year ago")
plt.xticks(x_pos,x)#horizontal
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()
#################################################
import matplotlib.pyplot as plt
x=[5,9,2,4,1]
y=[9,7,3,4,1]
a=[i for i, _ in enumerate(x)]
plt.bar(a,y)
plt.xlabel("x--axis")
plt.ylabel("y--axis")
plt.title("BAR graph")
plt.xticks(a,y)
plt.minorticks_on()
plt.legend()
plt.show()
###################################################################
##Horizontal graph ----to do horizonatal we use barh() and yticks()
import matplotlib.pyplot as plt
x=['java','python','PHP','js','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,7.6]
x_pos=[i for i,_ in enumerate(x)]
plt.barh(x_pos,popularity,color='green')
plt.xlabel("Languages")
plt.ylabel("popularity")
plt.title("pooularity of programming language \n"+"Worldwide,Oct 2017 compared to year ago")
plt.yticks(x_pos,x)#horizontal
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()
#####################################################################3

import matplotlib.pyplot as plt
x=['java','python','PHP','js','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,7.6]
x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color=['red','black','green','blue','yellow','cyan'])
plt.xlabel("Languages")
plt.ylabel("popularity")
plt.title("pooularity of programming language \n"+
          "Worldwide,Oct 2017 compared to year ago")
plt.xticks(x_pos,x)#horizontal
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()
#####################################################################3

#Histogram ::data should symmetrical normally distributed
#how data is distributed
#data is skewed distributed
import matplotlib.pyplot as plt
blood_sugar=[113,85,90,150,149,88,93,115,135,80,77,82,77,82,129 ]
plt.hist(blood_sugar,rwidth=0.8)
plt.hist(blood_sugar,rwidth=0.5,bins=4)
########################
import matplotlib.pyplot as plt
list1=[211,23,67,45,123,234]
plt.hist(list1 ,bins=20)


'''
80-100 normal
100-125 pre diaable
125-150 Diabetic
'''


plt.xlabel("Sugar Level")
plt.ylabel("Number of patients")
plt.title("Blood Sugar Chart")

plt.hist(blood_sugar,bins=[80,100,125,150],rwidth=0.95,color='green')

############################################################
#Boxplot :: 
    #import libraries
import matplotlib.pyplot as plt
import numpy as np
   #create dataset
np.random.seed(10)
data=np.random.normal(100,20,200)
fig=plt.figure(figsize=(10,7)) 
#creating plot
plt.boxplot(data)
plt.show()
#################################################
import matplotlib.pyplot as plt
import numpy as np
#creating dataset
 
np.random.seed(10)
data_1=np.random.normal(100,10,200)
data_2=np.random.normal(90,20,200)
data_3=np.random.normal(80,30,200)
data_4=np.random.normal(70,400,200)
data=[data_1,data_2,data_3,data_4]
fig=plt.figure(figsize=(10,7)) 
#creating axes instance
ax=fig.add_axes([0,0,1,1])
#creating plot
plt.boxplot(data)
bp=ax.boxplot(data)
plt.show()



 
