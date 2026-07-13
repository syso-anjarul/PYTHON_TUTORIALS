from playwright.sync_api import Page,Expect 
class Encapsulation:
    """this class is designed for OOPS concepts implementation.We will understand and practice 
    Encapsulation, Abstruction, Class and Object, Inheritance and Polymorphism.
    
    Encapsulation is the biding variables and methods together, and not exposing the entire 
    functionality """

    def __init__(self):
        self.Name="anjarul"
        self.url="https://google.com"
        self.__p="privateNumber"
    
    def login(self):
        print(self.Name)
        print(self.url)
        print(self._Encapsulation__p) #this is called name mangling Abstruction

e=Encapsulation()
e.login()
print(e._Encapsulation__p)



