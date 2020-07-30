#Function Overloading
class Cucumber():
     def type(self):
       print("Vegetable")
     def color(self):
       print("Red")
class Apple():
     def type(self):
       print("Fruit")
     def color(self):
       print("Red")

def func(obj):
       obj.type()
       obj.color()

obj_cucumber = Cucumber()
obj_apple = Apple()
func(obj_cucumber)
func(obj_apple)
