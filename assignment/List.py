#list
ThisList=["book","notebook", "pen", "pencell"]
print(ThisList)

#lenth,allows duplicates
List=["book","notebook","book"]
print(List)
print(len(ThisList))

#integar,strings, and camplixe
list1=[1,2,3,4]
list2=["apple","banana","cherry"]
list3=[True,False,False]
list=["abc",34,"ture",40,"male"]

#type()
mylist=["apple","banana","cherry"]
print(type(mylist))

#list:range
print(mylist[1:])
print(mylist[-1])
print(mylist[0:])

#check if item exists
if "babana" in mylist:
    print("yes, bannana is in my list")
if "true" in list3:
    print("True")
if "pen" in ThisList:
    print("pen")
    
    
    
#change item value
ThisList[1] = "seconde item changed"
print(ThisList)
mylist[0] = "obaid"
print(mylist)
list2[2]= "papya"
print(list2)

#change a range of item values 
ThisList[0:3] = ["ahmad","obaid","salman"]
print(ThisList)
list1[0:2] = ["4","5","6"]
print(list1)

