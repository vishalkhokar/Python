data="india is My Country"
#D=dict([(chr(a),0) for a in range(ord('A'),ord('Z')+1)])
#smalld=dict([(chr(a),0) for a in range(ord('a'),ord('z')+1)])
D={chr(a):0 for a in range(ord('A'),ord('Z')+1 )} | {chr(a):0 for a in range(ord('a'),ord('z')+1)}
print(type(D))
for i in data:
    if i  in D :
      D[i]=D[i]+1     
for k,j in D.items():
   if j>=1:
    print(f"{k}",j)
print(D) 
