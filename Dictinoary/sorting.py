import operator
#sorting as per Keys
d={111:'BBB',333:'AAA',222:'cccc'}
print("Key are",d.keys())
print("Values are",d.values())
k=dict(sorted(d.items()))
print(k)
#Sorting as per values
v=dict(sorted(d.items(),key=operator.itemgetter(1)))
print(v)