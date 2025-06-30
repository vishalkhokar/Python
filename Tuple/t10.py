def CountOccur(t):
    a=()
    for i in range(len(t)):
        x=t[i] * t[i]
        a=a+(x,)
    print(a)     
def main():
    print("Enter the size of tuple")
    siz=int(input())
    t=()
    print("Enter the element in a tuple")
    for i in range(0,siz):
        value=int (input())
        t=t+(value,)
    ans=CountOccur(t)
    print(ans)
if __name__=="__main__":
    main()