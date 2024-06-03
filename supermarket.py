from datetime import datetime

name=input("Enter your name:")

lists='''
Rice         Rs 20/kg
oil          Rs 80/liter
sugar        Rs 30/kg
salt         Rs 20/kg
paneer       Rs 110/kg
green gram   Rs 15/kg
colgate      Rs 85/each
maggi        Rs 50/kg
Boost        Rs 90/each
'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':20,'oil':80,
       'sugar':30,'salt':20,
       'paneer':110,'green gram':15,
       'colgate':85,'maggi':50}
option=int(input("for List of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))          
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
    if finalamount!=0:
        for i in range(len(pricelist)):
            print(i,ilist[i],qlist[i],plist[i])
            
    






