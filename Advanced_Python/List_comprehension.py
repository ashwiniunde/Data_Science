## This code will append the ele from 0 to 19 in list
## Using for loop and >append() function
list=[]
for num in range(0,20):
    list.append(num)
print(list)


##  list comprehension
## This code will append the ele from 0 to 19 in list
## This single line of code does the same thing as the above multi-line code, but in a more concise manner
list=[num for num in range(0,20)]
print(list)


##list comprehension is used to apply transformation like here we are captlized the all words
names=["dada","mama","kaka"]
list=[name.capitalize() for name in names]
print(list)
# Output will be like this  --->>> ['Dada', 'Mama', 'Kaka']


#comprehension with if statement
def is_even(num):
    return num%2==0
list=[num for num in range(21) if is_even(num)]
print(list)  ## even number will be printed between 0 to 21
## Output --->>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


#comprehension with nested for loop 
list=[f"{x}{y}"for x in range(3) for y in range(3)]
print(list)
'''
Output --->>> ['00', '01', '02', 
                  '10', '11', '12', 
                  '20', '21', '22']
'''


##dict comprehension
dict={x:x*x for x in range(3)}
print(dict)
## Output --->>> {0: 0, 1: 1, 2: 4}








