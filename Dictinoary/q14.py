scores={}
for i in range(4):
    print("Enter the key")
    key=input()
    print("Enter the value")
    v1=input()
    scores[key]=v1
    
print(scores.items())
scores =dict(sorted(scores.items(), key=lambda item:item[1], reverse=1))
print(scores)