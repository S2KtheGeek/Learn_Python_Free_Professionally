'''
There are total 5 types of inheritance:
Single Inheritance: A base or clind class directly inheriting from the parent or super class.
Multilevel Inheritance: The same thing we see in case of a child and grand parent.
Hierarchical Inheritance: This is when a parent class is inherited by two or more child classes.
Multiple Inheritance: When a child class inherits from multiple parent classes, it is called multiple inheritance.
Hybrid Inheritance: Mixture of any two or more of the above methods.
'''
#Grand Parent Class
class Base(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name

# Inherited or Sub class -> Father Class
class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def getAge(self):
        return self.age

# Inherited or Sub class -> Grand Child Class
class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def getAddress(self):
        return self.address

g = GrandChild("STG", 24, "Kolkta")
print(g.getName(), g.getAge(), g.getAddress())
