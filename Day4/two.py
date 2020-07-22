
class example2(object):
    """Outer Class"""

    def __init__(self):
        ## instantiating the 'Inner' class
        self.inner = self.Inner()

    def reveal(self):
        ## calling the 'Inner' class function display
        self.inner.inner_display("Calling Inner class function from Outer class")


    class Inner:
        """Inner Class"""

        def inner_display(self, msg):
            print(msg)

outer_class = example2()
outer_class.reveal()
