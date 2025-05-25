def bubbleSort(data):
    j=0
    while(j<len(data)):
       temp=None
       for i in range(0, len(data)-1):
            if data[i] > data[i+1]:
                temp=data[i+1]
                data[i+1]=data[i]
                data[i]=temp
       j=j+1        
    return data
def main():
   try: 
    print("Enter the Size of List")
    siz=int(input())
    data=[]
    print("Enter the Element in List")
    for i in range(siz):
        no=int(input())
        data.append(no)
    sorteddata= bubbleSort(data)
    print(sorteddata)   
   except ValueError as vobj:
       print("Invalid Element entereed",vobj)
if __name__=="__main__":
    main()
