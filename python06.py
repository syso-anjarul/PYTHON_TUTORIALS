class Functionstest (object):
    """this class is created to check multiple functions."""
    def factorial(self,n:int):
        result=1
        while n>0:
            result=result*n
            n -=1
        print(result)

    def primeNumber(self, n:int):
        x=1
        for i in range(2,n):
            if n%i==0:
                x=0
                break
            else:
                x=1
        if x==0:
            print('prime number')
        else:
            print('this is not prime')
    
    def nested_method(self,str):
        def nested_method():
            return 'How are you'
        str1=nested_method()+str
        print(str1)

    def returnMultiValues(self,a:int,b:int):
        sum=a+b
        product=a*b
        expo=a**b
        return sum,product,expo
    
    def func1(self, fun):
        return 'Hi, ' + fun
    
    def func2(self):
        return 'I am ok'
    
    def defaultArgument(self, a:str, x=40.45):
        print(3*'python'+'rocks')
        list=[1,3]
        print(list[-1])
        return 'The value of '+ a,x





    
func=Functionstest()
func.factorial(4)
func.primeNumber(7)
func.nested_method(' Amal')
a,b,c=func.returnMultiValues(3,4)
print(a)
print(func.func1(func.func2()))
print(func.defaultArgument('Mango'))
