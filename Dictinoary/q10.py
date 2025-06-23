NumberValue={
    'a':-1,
    'b':-200,
    'c':0
}
newmaxi=None
for j in NumberValue:
    newmaxi=NumberValue[j]
    break
for i in NumberValue:
    if newmaxi < NumberValue[i]:
        newmaxi=i
        
print(newmaxi)