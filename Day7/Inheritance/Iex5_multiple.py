class Base1(object):
    def __init__(self):
        self.str1 = "STG"
        print("In Base1")

class Base2(object):
    def __init__(self):
        self.str2 = "YouTube"
        print("In Base2")

class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("In Derived")

    def printStrs(self):
        print(self.str1, self.str2)


obj = Derived()
obj.printStrs()
