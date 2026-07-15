class Dictionary(object):
    """this class is created for practicing all dictionaries"""
    def dic_operations(self):
        dic={}
        #add k, v in the dic
        dic.update({'Anjarul':'Male','Mou':'female'})
        print(dic)

        #get value from  key
        keyy=dic.get('Anjarul')
        print(keyy)

        #update any value
        dic.update({'Anjarul':"new"})
        print(dic)

        #get all keys
        for k in dic.keys():
            print(k)

        #get all values
        for v in dic.values():
            print(v)

        for k, v in dic.items():
            print(k,v)

    #sum of values
    def sumOfValues(self):
        dic={
            'anjarul':10,
            'mou':20,
            'Arisha':30

        }
        sum=0
        for i in dic.values():
            sum +=i
        print(sum)
    #loop iterares
    def loopIterates(self):
        dic={
            'r':'Red',
            'y':'Yellow',
            'b':'black'
        }
        for k in dic:
            print(k)
        for k in dic:
            print(dic[k])
    #occurance of letters in the strings
    def occuranceLetters(self):
        str='Core Python'
        str.lower()
        dic={}
        for i in str:
            dic[i]=dic.get(i,0)+1

        for k,v in dic.items():
            print(k,'-',v)
        
        print(dic.get('b',0))
        print(dic['C'])

    def palindrome(self, str):
        str=str.lower()
        left=0
        right=len(str)-1
        while left < right:
            if str[left] != str[right]:
                return False
            left +=1
            right -=1
        return True



dic=Dictionary()
dic.dic_operations()
dic.sumOfValues()
dic.loopIterates()
dic.occuranceLetters()
print(dic.palindrome('Madam'))