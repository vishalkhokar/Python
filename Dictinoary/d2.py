import copy
D={101:"AAA",102:"vishal",103:[99,88]}
v={100:"xxxxx"}
print(id(D))
for  K in D:
    if K not in v:
        v[K]=copy.deepcopy(D[K])
print(v)
print(D)
print(id(D[103][1]))
print(id(v[103][1]))
D[103][1]=11
print(v)
print(D)
print(id(D[103][1]))
print(id(v[103][1]))