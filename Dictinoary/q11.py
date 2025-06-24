list1=[]
for i in range(4):
    print("Enter the name ")
    name=input()
    list1.append(name)
print(list1)

dict1={}
print(type(dict1))
for j in list1:
    firstLetter=j[0].upper()
    if firstLetter not in dict1:
        dict1[firstLetter]=[]
    dict1[firstLetter].append(j)    
print(dict1)
         