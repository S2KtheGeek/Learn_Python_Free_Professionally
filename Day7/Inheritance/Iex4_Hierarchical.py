class Parent(object):
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Parent):
      def func3(self):
          print("this is function 3")

ob = Child()
ob1 = Child2()
ob.func1()
ob.func2()
ob1.func1()
ob1.func3()
