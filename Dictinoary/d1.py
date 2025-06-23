D={101:"AAA",102:"vishal",103:"CCC"}
print(id(D))
for k in D:
    print(k,"------>",D.get(k))
    if(D.get(k)=="CCC"):
        D[k]=None
print(D)
print(id(D))
D[102]="BBB"
print(D)
del D[101]
print(D)