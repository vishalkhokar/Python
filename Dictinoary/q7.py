print("Enter  the string")
str1=input()
Output={}
for i in str1:
    if i not in Output:
        Output[i]=1
    elif i in Output:
        valuecnt=Output.get(i)
        Output[i]=int(valuecnt) + 1
        
print(Output)     