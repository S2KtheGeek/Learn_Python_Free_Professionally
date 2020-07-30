class Person(object):

	def __init__(self, name):
		self.name = name


	def getName(self):
		return self.name


	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	#Same as the parent class but true is returned
	def isEmployee(self):
		return True


emp = Person("STG") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Subhra_TG") # An Object of Employee
print(emp.getName(), emp.isEmployee())
