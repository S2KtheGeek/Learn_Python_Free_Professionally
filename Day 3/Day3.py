'''Hello guys in todays session we will primarily learn about
Functions
How Functions Helps Us
Reusability of the code using functions
Functions as first class objects

What is function?
A function is a block of codes which has some instructions and takes an input
following those instructions it returns an output. On the basis of this defination
a fucntions are of two types: pure and impure. Pure functions are those which
returns a value and impure are those which doesn't return a value.

Syntax
def function_name(arg1, arg2, ....):
    Function Statements

def pure_func(a, b):
    c = a + b
    return(c)

def impure_func(a, b):
    c = a + b
    print(c)

def func_name(args,...): -> Function Signature
(args,....)-> Function Parameters
'''

def add(a, b): #formal arguments
    c = a + b
    print (c)

#To call a function just wirte the function name and pass proper args
add(5, 10)#actual arguments

def even_odd(n):
    if n % 2 == 0:
        print (n,' Is an even number')
    else:
        print (n,' Is an odd number')

even_odd(21)
even_odd(23)

def check_prime(n):
    flag = 0
    for i in range(1, n): #it will go from 1 to n - 1
        if n % i == 0:
            flag += 1
        else:
            continue
    if flag == 1:
        print("prime")
    else:
        print("Not Prime")

check_prime(3)

def check_prime(n):
    flag = 0
    for i in range(2, n//2): #it will go from 1 to n - 1
        if n % i == 0:
            flag = 1
            break
        else:
            continue
    if flag == 0:
        print("prime")
    else:
        print("Not Prime")

check_prime(97)

#A function can return multiple values
def sum_diff(a, b):
    s = a + b
    d = a - b
    return s , d

print(sum_diff(10, 5))
print(type(sum_diff(10, 5)))

def fact(n):
    factorial = 1
    while n >= 1:
        factorial *= n #factorial = factorial * n
        n -= 1 #n = n - 1

    return (factorial)

print(fact(5))

#functions as first class objects
first = fact(7) #storing the returned value of the function to a variable
second = check_prime(fact(6)) #passing a function as the argument of another function
#defining a function inside another function
def display(msg):
    def message():
        return('STG Youtube Channel')
    result = msg + message()
    return result

print(display('Welcome to '))

#returning a function from the function
def mass():
    print('Welcome to the Mass!!')
def disp():
    return mass

val = disp()
print(val)
print(val())

#Call by Value
facto = fact(8)
print(facto)
#Call by refernce
num = 8
print(fact(num))

#Positional Arguments
def attach(s1, s2):
    s3 = s1 + s2
    print('If Position is kept constant:', s3)
    s4 = s2 + s1
    print('If Position is changed:', s4)

attach('STG', 'YouTube')

#Keyword Arguments
def simple_interest(principal, rate_of_interest, time):
    simple_interest = (principal * rate_of_interest * time) / (100*12)
    print(simple_interest)

simple_interest(principal=5500.23, rate_of_interest=5, time=12)

#Default Arguments
def simple_interest1(principal, rate_of_interest=5, time=12):
    simple_interest = (principal * rate_of_interest * time) / (100*12)
    print(simple_interest)

simple_interest1(5500.23)


#Variable Length arguments
def var_add(a, *args):
    s = 0
    s += a
    for i in args:
        s += i
    print('Sum of the elements=', s)

var_add(5, 6)
var_add(5, 6, 7)
var_add(5, 6, 7, 32, 45)

#Local and Global Variable and Global Keywords
value = 23
def printing():
    global value
    print('Variable', value )
    value = 20
    print('Local Variable', value )

def pg():
    global value
    print('Variable', value )


printing()
pg()

