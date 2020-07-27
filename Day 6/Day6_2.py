class Visible(object):
  def isVisible(self):
    return 'This is Visible ->Public'

  def _alsoVisible(self):
    return 'This is also visible -> Protected'

  def __isNotVisible(self):
    return 'This is not visible ->Private'

#Outside class
Check = Visible()
print(Check.isVisible())
print(Check._alsoVisible())
#print(Check.__isNotVisible())
#AttributeError: 'Visible' object has no attribute '__isNotVisible'

print(Check.isVisible())
print(Check._alsoVisible())
print(Check._Visible__isNotVisible())
#Changing the name causes it to access the function
