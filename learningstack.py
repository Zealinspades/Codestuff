"""
print ("test")

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print (x + y + z)
#applebananacherry
print (x)
print (y)
print (z)
#same thing just seperated by lines because of separate print calls
#you can assign a string to a variable
#cannot print x = 5 and y = John with x+y
lessononex = ("John")
lessononey = 5
print (lessononex, lessononey)
print (lessononex + lessononex)
#output John 5 , you can print anything with commas but only accepts '+' with same data type

""" 

'''
x = "awesome"

def myFunc() : 
    x = "fantastic"
    print ("Python is " + x)

myFunc()

# returns 'fantastic' as x because more local definitions override global definitions
'''
'''
x = "Awesome"

def myFunc() :
    global x
    x = "fantastic"

myFunc()

print ("Python is " + x)
# global calls inside functions can manually override otherwise global variables if used as part of a function
'''

"""
## print (type(y)) can be used to identify the current typing of a variable

a = 1.234664

x = int(a) #force the assigned variable to be that of the designated data type

print (x)

# result is '1'
"""
'''
#print ("I wandered lonely as a cloud
#       that floats on high oer vales and hills")

# Does NOT function

a = """I wandered lonely as a cloud
that float on high oer vales and hills"""

print (a)

#DOES function
#multi-line prints are possible to assign to a variable without the use of multiple print commands but only with the use of triple quotes
#strings are arrays of letters

a = "Hello, World!"
print (a[0])

# prints first letter in the string, H
# had to use triple apostrophes here because of the presence of multiline string
'''

'''
for x in "banana" :

    # for every numbered index of the array of 'banana'? Why does 'x' work here?
    
    print (x)
    print (len(x))
    print ("nan" in x)
    print ("n" in x)
    if "n" in x :
        print ("There's an n here!")
    if "a" not in x :
        print ("There's no a!!")
'''

#cycles through each letter in the word and prints them with each loop iteration
# prints the length of each tested array, which is one character with len()
# 'nan' is checked to see if it is in the selection of tested string and returns false because it is checking single letters
# 'n' returns true because there are several 'n's
# when an n is tested for x, prints with 'in'
# when each letter is checked, if it is not an 'a', prints there's no a


'''
x = "Hello, World!"
print (x[:5])
#Hello - from 0-4, being 0=H, 1=e, 2=l, 3=l, 4=o respectively
#'until five is reached but not inclusive'

print (x[2:])
#llo, World! - from position 2 to the end
# 'from true position 2 to the end'
# why tf is it different between these two examples

print (x[-5:-2])
#orl

print (x.upper())
#HELLO, WORLD!
#upper, lower, strip, etc are functions native to python that can be called on like methods of the print function?

print (x.replace("H", "J"))
#Jello, World!

print (x.split(","))
# returns ['Hello', ' World!'], making two separate instances of strings - so split makes an array of arrays?
'''
'''
x = 5

a = "Hello"
b = "World"
c = a + " " + b
d = f"It is day number {x}"

print (c)
print (d)
# c == "Hello" + " " + "World"
# can only use non-string variables with f-strings
'''
'''
txt = print(f"the price is {20 * 12} dollars!")
#240
print (txt)
#None

#GOOD LESSON
# this successfully prints the string because the print function is called as part of the assignment with f-string as argument
# txt is assigned the value 'none' because print does not return a value, it's just a function
# A FUNCTION IS ALWAYS CALLED WHEN ASSIGNMENT IS ATTEMPTED
'''
'''
txt = (f"the price is {20 * 12} dollars!")
print (txt)

#prints as expected, because x is being assigned a string variable with an f-string argument
''' 

# print ("We are the so called \"Vikings\" from the north.")
# We are the so called "Vikings" from the north.
# successfully escaped the print function's illegal characters (") with a backslash

'''
x = "test"
print(x.center(20))
print(x.capitalize)

#apparently center wants arguments for how far away the center is - pretty cool
'''
'''
print(10 > 9)
print(9 == 7)
print(1 < 2)
#True, False, True.
#Python passes the boolean evaluation to print as an argument and it is printed

x = 100
y = 2

if x / y == 50 :
    print ("x / y is 50!")
else :
    print ("x / y is not 50!")

print (bool("Hello!"))
# A boolean is default true because it is asking 'is this itself',
# only empty strings and 0 are 'False' - list following
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 

while bool ("yes") :
    print ("test success")
    break
#test success
'''

'''
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) 

# This is a class that says 'the length of it's 'self' when called
# The function __len__ (self) always returns 0, meaning 'length zero'

# myobj is initialized with the function myclass()
# print calls on the boolean function to evaluate myobj as a true/false, which calls the 
# ...myclass() function, which 

Okay so here's my understanding - __len__ is a 'magic method', one of two that is called on 
when python is asked to evaluate the bool condition of a class.
> does myclass define __bool__, it does not
> does myclass define __len__, it does
> what value does the __len__ definition return?
> 0
> therefore the class returns a 'false' value

'''
'''
x = 200
print (isinstance(x, int))
# print function is called with isinstance as an argument, which checks if x is an integer
# returns true, print function prints 'True'
'''


'''

x = 0.2
while True :
    x += 0.2
    print (x)
    if round (x) == 10 :

        print ("x is interpreted as int 10")
        break'''

'''
while True:
    x += 0.2
    print(f"x = {x:.10f}")  # Print x with 10 decimal places for clarity
    if round(x) == 10:
        print("x is interpreted as int 10")
        break
'''

'''
print (f"15 goes into 101 {101 // 15} times")
print (f"with {(101 % 15)} remaining.")
print (f"The calculation is: {101 // 15} * 15 = {(101 // 15)*15}, and {(101 // 15)*15} + {(101 % 15)} = 101")

#just testing out modulos and floor divisions --
modulos are 'how much remains after this division is finished'
floor division is 'how many whole times can this be divided ignoring the remainder'
'''
'''
&= is used for bitwise AND operations - for example
6 in binary is 0110, 3 in binary is 0011
the result of an AND bitwise operator is
0010
eg.

a = 6
b = 3
a &= b
print (a)

#output is 2, as 2 = 0010

Similarly, |= is a bitwise OR operator
^= is a bitwise XOR operator
>>= is a bitwise right shift assignment
<<= is a bitwise left shift assignment
'''

'''
thislist = ["apple", "banana", "cherry"]
print (thislist)

print (len(thislist))
#list is of length three
print (type(thislist))
#<class 'list'>
'''

'''
list1 = ["abc", 34, True, 40, "male"]
print (list1)
# prints list 1

print (list1[2:4])
#True, 40 - items located 2 and 3

print (list1[-1:-4])
#doesn't work as you're asking it to count backwards I guess

print (list1[-4:-1])
# 34, True, 40 - items located at -1 through -4 counting from the end

if "male" in list1 :
    print ("There's some truth in this list.")

else :
    print ("Error has occurred.")

#prints 'there's some truth --' as it exists in the list


print ("pop begins")

while (n := len(list1)) :
    print (list1.pop())
# assign the length of list1 to n, and evaluates n as the same value
# length is 5, which is 'True' to the while loop so it prints the last element in the list,
# then removes it from the list.
# the loop comes around again with 4..3..2..1 length, then 0, which evaluates as false in python

print (list1[2:4])
# as the list has been popped, it returns nothing, or [] (empty array)

print (bool(list1))
# python returns [] to the boolean, which is equivalent to false

list1 = [i for i in range(1,6)]
'''
'''
#this is not code below
expression FOR item IN iterable if condition
expression is evaluated for each item in the iterable
for item in iterable loops over each item in the iterable
the iterable here being the range from 1-6

so in [i for i in range(1,6)]
The initial 'i' is the expression that gets evaluated and included in the resulting list
1. for i in range(1,6) means iterate over the sequence generated by the range(1,6), which is 1-5
2. the i before the for keyword is the expression that is evaluated for each element in the
    iterable range
3. the results of the expression 'i' for each iteration are collected into a new list


'''

list1[0] = "Test Tube"
print (list1)

''