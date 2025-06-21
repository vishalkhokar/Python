print("Welcome To Hotel Ranak")
print("----------")
print("Our Menu")
print("----------")
MenuItem={
    "DalBati":390,
    "Haldi":350,
    "Pizza":300,
    "Cold-Coffee":60,
    "3Rice":200
}
for i in MenuItem:
    print(i,MenuItem[i])

OrderPlaced={}
print("Your Order Please")
for j in MenuItem:
    PlaceOrder=input()
    if PlaceOrder  in MenuItem:
        print("Enter the Quantity")
        try:
            Quantity=int(input())
        except Exception :
            print("Please enter Numeric Value")  
            Quantity=int(input())  
        OrderPlaced[PlaceOrder] = MenuItem[PlaceOrder] * Quantity
    elif PlaceOrder=="done": 
        break
    else :
        print("No Such Dish Available")
    
Orderlist=len(OrderPlaced)
if Orderlist==0:
        exit(0)
    
print((OrderPlaced))

TotalBill=0
for i in OrderPlaced:
    a=OrderPlaced[i]
    TotalBill= a +  TotalBill
    
print("Bill Amount is ",TotalBill)