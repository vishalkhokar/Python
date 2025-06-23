person={
    'Name':'vishal',
    'age':'29',
    'xyz':'abc'
}
xyz=person.copy()
temp=None
for i in xyz:
    temp=i
    i=person[i]
    person[i]=temp    

for j in xyz:
    del person[j]

print(person)   