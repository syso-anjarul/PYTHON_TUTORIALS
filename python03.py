class ClassAndObject(object):
    """this class is majorly focusing on class and objects"""
    #constructor: this is used to declare and initialse the instance variables
    def __init__(self):
        self.name="Anjarul"
        self.sytle="Style"
        self.gender="Male"

    def display(self): # this is instance method as this is using self as first params
        print(self.name)

co=ClassAndObject()
co.display()