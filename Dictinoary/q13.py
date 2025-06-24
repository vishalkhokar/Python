from collections import Counter
list1=[]
n=int(input("ENter the Size of list"))
for i in range(n):
    print("Enter the Number")
    name=input()
    list1.append(name)
print(list1)
emptyDict={}
value=0
for j in list1:
    if j not in emptyDict:
      emptyDict.update({j:value +1})
    else:
      a=emptyDict[j]+1
      emptyDict.update({j:a})    

newtest=Counter(list1)
print('hhhhhhh',newtest)
print(type(newtest))
displaydict={}
for k,v in emptyDict.items():
    if v==1:
        pass
    else:
        displaydict.update({k : v})
print()
print(displaydict)