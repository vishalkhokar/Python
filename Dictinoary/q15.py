from collections import Counter
print("Enter the Paragraph")
para=input()
para=para.lower()
spaces=para.split(" ")
newDict={}

for i in spaces:
    if i not in newDict:
        newDict[i]= 1
    else:
        newDict[i]=newDict[i] + 1

print(newDict)

highest=0
j=None
highstr=None
secondhigh=0
secondstr=None
low=0
lowstr=None
for k,j in newDict.items():
    if highest==0:
        highest=j
    if j >= highest:
       highest=j
       highstr=k
       
    if j >= secondhigh and j!=highest:
        secondhigh=j
        secondstr=k
    if j>=low and j!=highest and j!=secondhigh:
        low=j
        lowstr=k
           
print(highstr,":",highest) 
print(secondstr,":",secondhigh )
print(lowstr,":",low)