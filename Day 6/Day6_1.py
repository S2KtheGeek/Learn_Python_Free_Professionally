'''
Hello guys so today we will be talking about abstraction and encapsulation

Abstraction - Hiding Unnecessary information from the user

Encapsulation - Wrapping up of data members and member functions in a single unit called class

Encapsulation: — Information hiding.
Abstraction: — Implementation hiding.

_ = Single Underscore = Protected
__ = double underscore = Private

"_<className>__<attributeName>"
'''

class Person(object):
  def __init__(self):
    self.name = 'Subhra'            #Public
    self._mid = '_'                 #Protected
    self.__lastname = 'TheGeek'     #Private

  def display(self):
    return self.name +' ' + self._mid + ' ' + self.__lastname

#Outside class
P = Person()
print(P.name)
print(P.display())
print(P._mid)
#print(P.__lastname)
#AttributeError: 'Person' object has no attribute '__lastname'
#this can be done now by
print(P._Person__lastname)
