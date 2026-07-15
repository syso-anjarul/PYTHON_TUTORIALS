class ListandTupple(object):
    """this class is created for list and tupple excersice"""
    def diff_types_list(self):
        li1=[1,2,3,4,'Anjarul','Mou']
        print('first=%d,last=%s' %(li1[0],li1[5]))
    def listfromrange(self):
        l=list(range(2,9,2))
        print(l)

    def displayListinReverseorder(self):
        l=[1,2,3,4,5,6,7,8,9]
        for i in range(len(l)-1,-1,-1):
            print(l[i])
    
    def listRepetion(self):
        l=[0]
        print(l*3)
        l1=[[1,2,3]]*3
        print(l1[0][0])
        print(l1)
        print([[0,0,0]]*3)

    def list_methods(self):
        num=[10,20,30,40,50,60]
        # append
        num.append(70)
        print(num)
        #insert
        num.insert(0,100)
        print(num)
        #copy
        num2=num.copy()
        print(num2)
        num3=num.extend(num2)
        print(num3)
        n=num.count(10)
        print(n)
        num.remove(20)
        print(num)
        num.pop()
        print(num)
        num.sort()
        print(num)
        num.reverse()
        
        print(num)

    def biggest_smallest(self):
        list=[10,20,22,1,222]
        big=list[0]
        small=list[0]
        for i in range(len(list)):
            if list[i] > big:
                big=list[i]
            elif list[i]<small:
                small=list[i]
        print(big,small)

    def find_occurance(self):
        list=[1,1,2,3,4]
        r=1
        count=0
        for i in list:
            if i==r:
                count +=1
        print(count)

    def find_common_intwoList(self):
        list1=[1,2,3,4,5]
        list2=[3,4,5,6,7,8]
        set1=set(list1)
        set2=set(list2)
        num=set1.intersection(set2)
        print(num)
    def nested_list(Self):
        mat=[[1,2,3],[4,5,6],[7,8,9]]
        for i in mat:
            for c in i:
                print(c,end=' ')
            print()
        mat[0][0]=10
        print(mat)

litp=ListandTupple()
litp.diff_types_list()
litp.listfromrange()
litp.displayListinReverseorder()
litp.listRepetion()
litp.list_methods()
litp.biggest_smallest()
litp.find_occurance()
litp.find_common_intwoList()
litp.nested_list()