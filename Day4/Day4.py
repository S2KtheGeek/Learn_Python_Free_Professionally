'''
Hello guys so in todays class we will be learnig about:
Class
Object
attributes
behaviours
Self variable
constructor
Class is known as a user-defined datatype.
Variable - Instance and Class or Static
Types of methods - Instance, Class and Static
Passing members of one class to another - Advanced Concept Needed for inheritance
Nested Class - Advanced Concept

A class is a blueprint for objects. Class is known as a user-defined datatype.
An object is an instance of the class having characterstic properties(attributes) and behaviours(methods).

'''
class Example(object): #class Example:
    #Class or Static Variables
    #variable = 24


    #The attributes are written in __init__ function
    def __init__(self):
        #this is known as the constructor of the class
        self.name = 'STG'
        self.age = 20
        self.marks = 475
        self.variable = 10

    #Any other function is a method of the class
    def display(self):
        #this is known as the method of a class
        print('My name is', self.name)
        print('My age is', self.age)
        print('My marks are', self.marks)
        print("This is the variable", self.variable)

    #Mutator Methods
    def setname(self, name):
        self.name = name

    #accessor methods
    def getname(self):
        return self.name

    #Instance Method
    def modify(self):
        self.variable += 5 #self.variable = self.variable + 5




'''
    #Static Method
    @staticmethod
    def modify():
        Example.variable += 5 #Example.variable = Example.variable + 5


    #Class Method
    @classmethod
    def modify(cls):
        cls.variable += 5 #cls.variable = cls.variable + 5



    '''


class myclass:
    @staticmethod
    def mymethod(obj):
        obj.age = 54
        obj.display()

#Creating an object to access data
instance = Example()
object2 = Example()
Example.display(instance)
instance.display()

print(instance.name)
print(instance.age)
print(instance.marks)

#Class Methods
print(instance.variable)
print(object2.variable)
object2.modify()
print(instance.variable)
print(object2.variable)

#Instance Methods
instance.setname('Subhra_TheGeek')
print(instance.getname())

'''
#Static Method
print(instance.variable)
print(object2.variable)
Example.modify()
print(instance.variable)
print(object2.variable)
'''
#Passing members of one class to another
object2.display()
myclass.mymethod(object2)


