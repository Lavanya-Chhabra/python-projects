# Restaurant System
import pymongo as py
client=py.MongoClient("mongodb://localhost:27017/")
db=client["dbcafe"]

def menunbill(name,phone):
        items=["1. Pizza","2. Red Sauce Pasta","3. White Sauce Pasta","4. Mix Sauce Pasta","5. Manchurian","6. Chilli Patato","7. Momos","8. Noodles","9. Desi Macaroni","10. Pahado Wali Maggi"]
        pricing=[199,199,199,299,149,149,199,99,49,599]
        print(f"Welcome {name}!\n")
        print("Our Menu:-\n")
        for i,j in enumerate(items):
            print(f"{j}")
            print("\t"*5,f"₹{pricing[i]}")
        item1=0
        item2=0
        item3=0
        item4=0
        item5=0
        item6=0
        item7=0
        item8=0
        item9=0
        item10=0
    
        itemquantity1=0
        itemquantity2=0
        itemquantity3=0
        itemquantity4=0
        itemquantity5=0
        itemquantity6=0
        itemquantity7=0
        itemquantity8=0
        itemquantity9=0
        itemquantity10=0
    
        i=1
        while(i==1):
            print("")
            choice=input("Enter Item No. =")
            if(choice.isdigit() and int(choice)>0):
                ch=int(choice)
                match ch:
                    case 1:
                        item1=1
                        print("Pizza is Selected.")
                        itemquantity1=int(input("Enter the Quantity"))
                        if(itemquantity1<=0):
                            print("Please enter a valid number.")
                    case 2:
                        item2=1
                        print("Red Sauce Pasta is Selected.")
                        itemquantity2=int(input("Enter the Quantity"))
                        if(itemquantity2<=0):
                            print("Please enter a valid number.")
                    case 3:
                        item3=1
                        print("White Sauce Pasta is Selected.")
                        itemquantity3=int(input("Enter the Quantity"))
                        if(itemquantity3<=0):
                            print("Please enter a valid number.")
                    case 4:
                        item4=1
                        print("Mix Sauce Pasta is Selected.")
                        itemquantity4=int(input("Enter the Quantity"))
                        if(itemquantity4<=0):
                            print("Please enter a valid number.")
                    case 5:
                        item5=1
                        print("Manchurian is Selected.")
                        itemquantity5=int(input("Enter the Quantity"))
                        if(itemquantity5<=0):
                            print("Please enter a valid number.")
                    case 6:
                        item6=1
                        print("Chilli Patato is Selected.")
                        itemquantity6=int(input("Enter the Quantity"))
                        if(itemquantity6<=0):
                            print("Please enter a valid number.")
                    case 7:
                        item7=1
                        print("Momos is Selected.")
                        itemquantity7=int(input("Enter the Quantity"))
                        if(itemquantity7<=0):
                            print("Please enter a valid number.")
                    case 8:
                        item8=1
                        print("Noodles is Selected.")
                        itemquantity8=int(input("Enter the Quantity"))
                        if(itemquantity8<=0):
                            print("Please enter a valid number.")
                    case 9:
                        item9=1
                        print("Desi Macaroni is Selected.")
                        itemquantity9=int(input("Enter the Quantity"))
                        if(itemquantity9<=0):
                            print("Please enter a valid number.")
                    case 10:
                        item10=1
                        print("Pahado Wali Maggi is Selected.")
                        itemquantity10=int(input("Enter the Quantity"))
                        if(itemquantity10<=0):
                            print("Please enter a valid number.")
                    case _:
                        print("Please enter a valid item no.")
            else:
                print("Please enter a valid no.")
            i=int(input("Press 1: to order more else Press 0 ="))

        total=0
        print("Your Final Order is :-")
        print(f"{"Items":<25}{"Quantity":<20}{"Price":<20}{"Total":<13}")
        allorder=[]

        if(item1>0):
            itemtotal=itemquantity1*pricing[0]
            total += itemtotal
            obj1={
                "Item":items[0],
                "Quantity":itemquantity1,
                "Item Price":pricing[0],
                "Item Total":itemtotal
            }
            allorder.append(obj1)
            print(f"{items[0]:<25}{itemquantity1:<20}₹{pricing[0]:<19}₹{itemtotal:<13}")
        if(item2>0):
            itemtotal=itemquantity2*pricing[1]
            total += itemtotal
            obj1={
                "Item":items[1],
                "Quantity":itemquantity2,
                "Item Price":pricing[1],
                "Item Total":itemtotal
            }
            allorder.append(obj1)
            print(f"{items[1]:<25}{itemquantity2:<20}₹{pricing[1]:<19}₹{itemtotal:<13}")
        if(item3>0):
            itemtotal=itemquantity3*pricing[2]
            total += itemtotal
            obj1={
                "Item":items[2],
                "Quantity":itemquantity3,
                "Item Price":pricing[2],
                "Item Total":itemtotal
            }
            allorder.append(obj1)
            print(f"{items[2]:<25}{itemquantity3:<20}₹{pricing[2]:<19}₹{itemtotal:<13}")
        if(item4>0):
            itemtotal=itemquantity4*pricing[3]
            total += itemtotal
            obj1={
                "Item":items[3],
                "Quantity":itemquantity4,
                "Item Price":pricing[3],
                "Item Total":itemtotal
            }
            allorder.append(obj1)
            print(f"{items[3]:<25}{itemquantity4:<20}₹{pricing[3]:<19}₹{itemtotal:<13}")
        if(item5>0):
            itemtotal=itemquantity5*pricing[4]
            total += itemtotal
            obj1={
                "Item":items[4],
                "Quantity":itemquantity5,
                "Item Price":pricing[4],
                "Item Total":itemtotal
            }
            allorder.append(obj1)
            print(f"{items[4]:<25}{itemquantity5:<20}₹{pricing[4]:<19}₹{itemtotal:<13}")
        if(item6>0):
            itemtotal=itemquantity6*pricing[5]
            total += itemtotal
            obj1={
                "Item":items[5],
                "Quantity":itemquantity6,
                "Item Price":pricing[5],
                "Item Total":itemtotal
            }
            allorder.append(obj1)
            print(f"{items[5]:<25}{itemquantity6:<20}₹{pricing[5]:<19}₹{itemtotal:<13}")
        if(item7>0):
            itemtotal=itemquantity7*pricing[6]
            total += itemtotal
            obj1={
                "Item":items[6],
                "Quantity":itemquantity7,
                "Item Price":pricing[6],
                "Item Total":itemtotal
            }
            allorder.append(obj1)
            print(f"{items[6]:<25}{itemquantity7:<20}₹{pricing[6]:<19}₹{itemtotal:<13}")
        if(item8>0):
            itemtotal=itemquantity1*pricing[7]
            total += itemtotal
            obj1={
                "Item":items[7],
                "Quantity":itemquantity8,
                "Item Price":pricing[7],
                "Item Total":itemtotal
            }
            allorder.append(obj1)
            print(f"{items[7]:<25}{itemquantity8:<20}₹{pricing[7]:<19}₹{itemtotal:<13}")
        if(item9>0):
            itemtotal=itemquantity9*pricing[8]
            total += itemtotal
            obj1={
                "Item":items[8],
                "Quantity":itemquantity9,
                "Item Price":pricing[8],
                "Item Total":itemtotal
            }
            allorder.append(obj1)
            print(f"{items[8]:<25}{itemquantity9:<20}₹{pricing[8]:<19}₹{itemtotal:<13}")
        if(item10>0):
            itemtotal=itemquantity10*pricing[9]
            total += itemtotal
            obj1={
                "Item":items[9],
                "Quantity":itemquantity10,
                "Item Price":pricing[9],
                "Item Total":itemtotal
            }
            allorder.append(obj1)
            print(f"{items[9]:<25}{itemquantity10:<20}₹{pricing[9]:<19}₹{itemtotal:<13}")
        mainorder={
            "Order":allorder,
            "UserPhone":phone,
            "OrderValue":total
        }
        var=db["Orders"].insert_one(mainorder)
        print("-"*70)
        print(f"{"Grand Total":<65}₹{total:<10}")

def printbill(arr,ordervalue):
    print("Your Last order :-")
    print(f"{"Items":<25}{"Quantity":<20}{"Price":<20}{"Total":<13}")
    for x in arr:
        print(f"{x["Item"]:<25}{x["Quantity"]:<20}₹{x["Item Price"]:<19}₹{x["Item Total"]:<13}")
    print("-"*70)
    print(f"{"Grand Total":<65}₹{ordervalue:<10}")
        

print("Welcome to LAV Cafe!!")
print("Press 1: for New Customer.")
print("Press 2: for Existing Customer.")
print("Press 3: for Checking Order.")
mainchoice=input("Enter Your Choice =")
if(mainchoice.isdigit()):
    ch=int(mainchoice)
    match ch:
        case 1:
            Name=input("Enter Your Name =")
            Email=input("Enter Your Email =")
            Phone=input("Enter Your Phone no. =")
            Address=input("Enter Your Address =")
            if(Phone.isdigit() and len(Phone)==10):
                alreadyexist=db["Users"].find_one({"Phone":Phone})
                if(alreadyexist==None):
                    obj={
                        "Name":Name,
                        "Email":Email,
                        "Phone":Phone,
                        "Address":Address
                    }
                    var=db["Users"].insert_one(obj)
                    menunbill(Name,Phone)
                else:
                    print("Customer already registered.")
            else:
                print("Please enter a valid phone number.")
    
        case 2:
            Phone=input("Enter Your Phone no.")
            if(Phone.isdigit() and len(Phone)==10):
                alreadyexist=db["Users"].find_one({"Phone":Phone})
                if(alreadyexist==None):
                    print("No regidtered customer found please register")
                else:
                    Name=alreadyexist["Name"]
                    menunbill(Name,Phone)
            else:
                print("Please enter a valid phone number.")
                
        case 3:
            Phone=input("enter your phone no. =".title())
            if(Phone.isdigit() and len(Phone)==10):
                var=db["Users"].find_one({"Phone":Phone})
                if(var==None):
                    print("no registered customer found.".title())
                else:
                    sort=db["Orders"].find().sort("_id",-1)
                    order=db["Orders"].find_one({"UserPhone":Phone})
                    printbill(order["Order"],order["OrderValue"])
            else:
                print("please enter a valid number.".title())
                
        case _:
            print("Wrong choice.")
    
else:
    print("Please enter a valid number.")   