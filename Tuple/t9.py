def CountOccur(t,no):
    if no not in t:
        print("No Such element exist")
        return -1
    iCnt=0
    for i in range (len(t)):
        if t[i]==no:
            iCnt=iCnt+1
    return iCnt        
def main():
    print("Enter the size of tuple")
    siz=int(input())
    t=()
    print("Enter the element in a tuple")
    for i in range(0,siz):
        value=input()
        t=t+(value,)
    print(t)
    print("Enter the Number to be count")
    no=(input())
    ans=CountOccur(t,no)
    print("total occurence of "+no+ " is " + str(ans))
if __name__=="__main__":
    main()