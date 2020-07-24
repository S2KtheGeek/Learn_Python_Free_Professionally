'''
Hello guys, so today our video will be pretty short
where we will learn about OOP and what are the features
of oop

OOP or OOPS i.e. Object Oriented Programming System is a
revolutionary concept on which programming languages such as
C++, Java, Python etc. are created.

So why it was created, when had languages such as C, FORTRAN etc.?
Those languages were procedure oriented programming systems(pops)
or these were the languages where programmers used have procedures
or functions to do a job. The main task is devided into several sub tasks,
or functions also known as procedures.

In OOPS, we use classes and objects in their programs. A class
is a modeule which itself contains data and methods(functions)
to achieve the task. The main task is devided into several sub tasks,
and these are represented as classes.

Problems with POPS:
Data is exposed to whole program, so no security for data.
Difficult to relate with real world objects.
Difficult to create new data types reduces extensibility.
Importance is given to the operation on data rather than the data.

The characterstics of OOPS:
Classes and Objects
Abstraction
Encapsulations
Inheritance
Polymorphism
Dynamic Binding
Message Passing


Dunder = Double Underscores (__)
'''
class Person(object):
    #Attributes means values
    name = 'STG'
    age = 24

    #Actions Means Functions
    def __init__(self):
        self.id = 2468
        self.city = 'kolkata'
        self.__pvt = 'Pvt Var' #this is a private variable

    def display(self):
        print(self.name)
        print(self.age)
        print(self.id)
        print(self.city)

    def add(self, a, b):
        print(a + b)


class Second(Person):
    def __init__(self):
        super().__init__()

    def disp(self):
        print(self.name)
        print(self.age)


#class and objects
obj1 = Person()
obj1.display()

#Abstraction and encapsulation
print(obj1._Person__pvt)#error


#Polymorphisim
obj1.add(5,6)
obj1.add('Subhra_','TheGeek')


#Inheritance
SP = Second()
SP.disp()
