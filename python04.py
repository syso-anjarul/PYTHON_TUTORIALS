class InstanceMethod():
    """this class majorly focus on Instance methods like accessor and mutator"""
    #accessor means the getter method, which doesnot modify the variables
    def getName(self):
        return self.name
    
    #mutator methods modify the variabl values

    def setName(self,name):
        self.name =name

    def display():
        pass

ins=InstanceMethod()
ins.setName("Anjarul")
print(ins.getName())
