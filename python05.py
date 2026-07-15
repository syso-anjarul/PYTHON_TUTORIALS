class String_Characters(object):
    """this class is created for practicing strings and character questions"""

    #access elements of string in forward and reverse order while while loop
    def access_elements(self):
        str="this is the pythons string"
        len2=len(str)
        i=0
        while i<len2:
            print(str[i],end='')
            i +=1
        while len2>i:
            print(str[len2-1])
            len2-=1
        print('*************************')

    #access the chars using for loop
    def access_forloop(self):
        str="core python"
        for i in range(len(str)):
            print(str[i],end='')
        print('**************************')

    #check if sub string present in main string
    def checkSubStringInMainString(self):
        str="core python in string"
        sub='core'
        if sub in str:
            print('sub is present')
    
    #find first occurrence of sub string in the main string using find
    def first_occurence(self):
        str="core pythons in the pythons string"
        sub='pythons'
        index =str.find(sub)
        print(index)

     #find first occurrence of sub string in the main string using index
    def first_occurence_using_index(self):
        str="core pythons in the pythons string"
        sub='pythons'
        index =str.index(sub,0,len(str))
        print(index)
    
    # all positions of the substring
    def all_positions_of_subString(self):
        str="this is the core python series"
        listview =str.split(' ')
        for sub in listview:
            print('substrin:-', sub,'-index: ', listview.index(sub))

    def joining_string(self):
        string=("anjarul","mou")
        str='-'.join(string)
        print(str)

    # sort group of string in alphbetical order
    def sorting_strings(self):
        str="India Russia China Delhi Kolkata Ahmedabad"
        listCity=str.split(' ')
        listCity.sort()
        print(listCity)
    #length of string without using len function
    def len_string(self):
        str='core'
        len=0
        for i in str:
            len +=1
        print(len)
    # insert substring in a particular position
    def insertSubstring(self,position:int):
        str="core python"
        list=str.split()
        sub='learn'
        list.insert(position,sub)
        print(list)
        # str=str(list)
        str=' '.join(list)

        print(str)

st=String_Characters()
st.access_elements()
st.access_forloop()
st.checkSubStringInMainString()
st.first_occurence()
st.first_occurence_using_index()
st.all_positions_of_subString()
st.joining_string()
st.sorting_strings()
st.len_string()
st.insertSubstring(2)