'''
It is another way of creating iterators in a simple way
where it uses the key word "yield".Instead of returning
it in a defined function.
Generators are implemented using a function
'''

# Generator for all values
gen = (x for x in range(3))
print(gen)
for num in gen:
    print(num)


# generator for single values
# Using next() with Generators
gen=(x for x in range(3))
next(gen) #0
next(gen) #1
next(gen) #2


## Generator Function with yield
def range_even(end):
    for num in range(0, end, 2):
        yield num
        
for num in range_even(6):
    print(num)


#now instead of using for loop we can write create generators
gen=range_even(6)
next(gen)
next(gen)


## Chaining Generators
def lengths(itr):
    for ele in itr:
        yield len(ele)

def hide(itr):
    for ele in itr:
        yield ele * "*"
        
passwords = ["not good", "give m-pass"]

for password in hide(lengths(passwords)):
    print(password)

##take password from user and hide it
adj=input("Enter an adj:")
noun=input("Enter a noun:")
number=input("Enter a number:")
sc=input("Enter a special character:")
password=adj+noun+str(number) +sc
print("Your password is: %s"%password) 
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele* "*"
password=adj+noun+str(number)+sc    
for password in hide(lengths(password)):
    print(password,end="") 

