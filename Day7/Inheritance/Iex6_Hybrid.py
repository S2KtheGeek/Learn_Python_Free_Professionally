class Parent(object):
    def func1(self):
        print("this is function 1")

class Child(Parent):
    def func2(self):
        print("this is function 2")

class Child1(Parent):
    def func3(self):
        print("this is function 3")

class Child2(Child, Child1):
    def func4(self):
        print("this is function 4")

ob = Child2()
ob.func1()
ob.func2()
ob.func3()
ob.func4()
