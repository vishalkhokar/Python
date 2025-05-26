def BinarySearch(data,search):
    mid=len(data)//2
    if data[mid]==search:
        return mid
    right=mid
    left=mid
    
    for i in range(len(data)):
        if data[mid] < search:
            right=right+1
            if data[right]==search:
                return right
        else:
            left=left-1    
            if data[left]==search:
                return left
    else:
        return "Not found"        
def main():
   try: 
    print("Enter the Size of List")
    siz=int(input())
    data=[]
    print("Enter the Element in List")
    for i in range(siz):
        no=int(input())
        data.append(no)
    print("Enter the Number to be search")
    search=int(input())    
    data.sort()
    print(data)
    sorteddata= BinarySearch(data,search)
    print("Element found at index ",sorteddata)   
   except ValueError as vobj:
       print("Invalid Element entereed",vobj)
if __name__=="__main__":
    main()