# LMS - Library Management System 
import pymongo as py
client=py.MongoClient("mongodb://localhost:27017/")
db=client["dbLibrary"]

def DateTime():
    from datetime import datetime
    current_datetime = datetime.now()
    return current_datetime

def User(ph,name):
    print("\nPress 1: To Rent Books")
    print("Press 2: To Return Books")
    print("Press 3: To Purchase Books")
    print("Press 4: To Go Back\n")
    f=1
    while(f):
        ch5=input("Enter Your Choice =")
        if(ch5.isdigit()):
            ch5=int(ch5)
            f=0
            match ch5:
                case 1:
                    print("\n-"*150)
                    print("RENT WINDOW".center(130))
                    print("-"*150,"\n")
                    rent1=[]
                    grandtotal=0
                    ch6=1
                    while(ch6==1):
                        sno=input("Enter the Serial No. of the book =")
                        tb=db["Books"]
                        book=tb.find_one({"SNo":sno})
                        if(book!=None):
                            qty=int(input("Enter the no. of copies you want of the book ="))
                            week=int(input("Enter the no. of weeks you want the book for ="))
                            rent=book["Rental_Price_Per_Week"]
                            total=rent * qty * week
                            grandtotal += total
                            obj2={
                                "SNo":sno,
                                "Book_Name":book["Book_Name"],
                                "Quantity":qty,
                                "Weeks":week,
                                "Rent":rent,
                                "Total_Rent":total
                            }
                            rent1.append(obj2)
                            av=book["Available"] - qty
                            rn=book["Rent"] + qty
                            tb.update_one({"SNo":sno},{"$set":{"Available":av}})
                            tb.update_one({"SNo":sno},{"$set":{"Rent":rn}})   
                        else:
                            print("No Book Found.")
                        ch6=int(input("Press 1: To Rent Another Book else Press 0 ="))
                    if(rent1):
                        dt=DateTime()
                        billno=BillNo()
                        rent2={
                            "Phone":ph,
                            "Bill_No":billno,
                            "Rent":rent1,
                            "Grand_Total":grandtotal,
                            "Date&Time":dt,
                            "Return":{
                                "Status":None,
                                "Date&Time":None
                            },
                            "Fine":{
                                "Amount":None,
                                "Status":None
                            }
                        }
                        db["Rent"].insert_one(rent2)
                        PrintBill(rent1,rent2,billno)
                    User(ph,name)
                        
                case 2:
                    print("\n-"*150)
                    print("RETURN WINDOW".center(130))
                    print("-"*150,"\n")
                    ta=1
                    while(ta):
                        bn=input("Enter the Bill No. =")
                        tb=db["Rent"].find_one({"Bill_No":bn})
                        if(tb!=None):
                            ta=0
                            if(tb["Return"]["Status"]==None):
                                lt=tb["Rent"]
                                for item in lt:
                                    weeks=item["Weeks"]
                                    gdays=weeks * 7
                                    then=tb["Date&Time"]
                                    from datetime import datetime
                                    now= datetime.now()
                                    duration= now - then
                                    days= duration.days
                                    totalfine=0
                                    if(days>gdays):
                                        fine=Fine(days,item)
                                        totalfine += fine
                                    else:
                                        Return(item)
                                if(totalfine!=0):
                                    print(f"Your Total Fine: ₹{totalfine}")
                                    db["Rent"].update_one({"Bill_No":bn},{"$set":{"Fine":{"Amount":totalfine}}})
                                    db["Rent"].update_one({"Bill_No":bn},{"$set":{"Fine":{"Status":"Payed"}}})
                                    for item in lt:
                                            Return(item)    
                                db["Rent"].update_one({"Bill_No":bn},{"$set":{"Return":{"Status":"Returned"}}})
                                db["Rent"].update_one({"Bill_No":bn},{"$set":{"Return":{"Date&Time":now}}})
                                print("Books Successfuly Returned")
                                
                            else:
                                print("Books Already Returned.")
                        else:
                            print("No Entry Found.")
                        ta=int(input("Press 1: to return more books else Press 0: to go back ="))
                    User(ph,name)
                    
                case 3:
                    print("\n-"*150)
                    print("PURCHASE WINDOW".center(130))
                    print("-"*150,"\n")
                    pc=[]
                    grandtotal=0
                    ch6=1
                    while(ch6):
                        sno=input("Enter the Serial No. of the book =")
                        tb=db["Books"]
                        book=tb.find_one({"SNo":sno})
                        if(book!=None):
                            qty=int(input("Enter the no. of copies you want of the book ="))
                            total=(book["Retail_Price"])*qty
                            grandtotal += total
                            obj={
                                "SNo":sno,
                                "Book_Name":book["Book_Name"],
                                "Quantity":qty,
                                "Price":book["Retail_Price"],
                                "Total":total
                            }
                            pc.append(obj)
                            qt=book["Quantity"] - qty
                            av=book["Available"] - qty
                            tb.update_one({"SNo":sno},{"$set":{"Available":av}})
                            tb.update_one({"SNo":sno},{"$set":{"Quantity":qt}})
                        else:
                            print("No Book Found.")
                        ch6=int(input("Press 1: To Purchase Another Book else Press 0 ="))
                    if(pc):
                        dt=DateTime()
                        billno=BillNo()
                        mobj={
                            "Phone":ph,
                            "Bill_No":billno,
                            "Purchase":pc,
                            "Grand_Total":grandtotal,
                            "Date&Time":dt
                        }
                        db["Purchase"].insert_one(mobj)
                        Purchase(pc,mobj,billno)
                    User(ph,name)
                       
                case 4:
                    Start()
                    
                case default:
                    print("Please Enter a Valid Choice.")

        else:
            print("Please Enter a Digit.")
    

def Books():
    print("\nPress 1: To Add Books")
    print("Press 2: To Edit Books")
    print("Press 3: To Display All Books")
    print("Press 4: To Find Books")
    print("Press 5: To Delete Books")
    print("Press 6: To Go Back\n")
    b=1
    while(b):
        choice1=input("Enter Your Choice")
        if(choice1.isdigit()):
            ch1=int(choice1)
            b=0
            match ch1:
                case 1:
                    AddBook()
                case 2:
                    print("\n-"*150)
                    print("EDIT WINDOW".center(130))
                    print("-"*150,"\n")
                    EditBook()
                case 3:
                    print("\n-"*150)
                    print("ALL BOOKS".center(130))
                    print("-"*150,"\n")
                    AllBooks()
                case 4:
                    print("\n-"*150)
                    print("SEARCH WINDOW".center(130))
                    print("-"*150,"\n")
                    FindBook()
                case 5:
                    print("\n-"*150)
                    print("DELETE WINDOW".center(130))
                    print("-"*150,"\n")
                    DeleteBook()
                case 6:
                    Start()
                case default:
                    print("Please Enter a Valid Choice.")
                    b=1    
        else:
            print("Please Enter a Valid Choice.")

def AddBook():
    tb=db["Books"]
    ch2=1
    while(ch2==1):
        btype=input("Enter the Type of the Book =")
        name=input("Enter the Name of the Book =")
        sno=input("Enter the Serial No. of the Book =")
        available=int(input("Enter the No. of Books Available ="))
        rent=int(input("Enter the No. of Books on Rent ="))
        pp=int(input("Enter the Publish Price of Book ="))
        rp=int(input("Enter the Retail Price of Book ="))
        renp=int(input("Enter the Rental Price of Book ="))
        
        obj1={
            "Book_Type":btype,
            "Book_Name":name,
            "SNo":sno,
            "Quantity":available + rent,
            "Available":available,
            "Rent":rent,
            "Publish_Price":pp,
            "Retail_Price":rp,
            "Rental_Price_Per_Week":renp,
        }
        tb.insert_one(obj1)
        c=1
        while(c):
            ch2=input("Press 1: To Add More Books else Press 0: To Go Back =")
            if(ch2.isdigit):
                ch2=int(ch2)
                c=0
            else:
                print("Please Enter a Valid Choice.")
    if(ch2==0):
        Books()

def FindBook():
    tb=db["Books"]
    ch3=1
    while(ch3==1):
        sno=input("Enter the Serial No. of the Book =")
        result=tb.find_one({"SNo":sno})
        print(f"{"Book Type":<15}{"Book Name":<25}{"SNo.":<10}{"Quantity":<15}{"Available":<15}{"Rent":<10}{"Publish Price":<20}{"Retail Price":<20}{"Rental Price (per week)":<20}")
        print(f"{result["Book_Type"]:<15}{result["Book_Name"]:<25}{result["SNo"]:<10}{result["Quantity"]:<15}{result["Available"]:<15}{result["Rent"]:<10}{result["Publish_Price"]:<20}{result["Retail_Price"]:<20}{result["Rental_Price_per_week"]:<20}")
        d=1
        while(d):
            ch3=input("Press 1: To Find More Books else Press 0: To Go Back =")
            if(ch3.isdigit):
                ch3=int(ch3)
                d=0
            else:
                print("Please Enter a Valid Choice.")
    if(ch3==0):
        Books()
        
def DeleteBook():
    tb=db["Books"]
    ch4=1
    while(ch4==1):
        print("Press 0: To Delete All Books.")
        print("Press 1: To Delete few Books.")
        delete=int(input("Enter Your Choice ="))
        if(delete==1):
            sno=input("Enter the Serial No. of the Book =")
            result=tb.delete_one({"SNo":sno})
            print("Entry Successfully Deleted.")
            e=1
            while(e):
                ch4=input("Press 1: To Delete More Books else Press 0: To Go Back =")
                if(ch4.isdigit):
                    ch4=int(ch3)
                    e=0
                else:
                    print("Please Enter a Valid Choice.")
        elif(delete==0):
            tb.delete_many({})
        else:
            print("Please Enter a Valid Choice.")
    if(ch4==0):
        Books()
            
def AllBooks():
    tb=db["Books"]
    result=tb.find()
    print("-"*150)
    print(f"{"Book Type":<18}{"Book Name":<28}{"SNo.":<10}{"Quantity":<15}{"Available":<15}{"Rent":<10}{"Publish Price":<20}{"Retail Price":<20}{"Rental Price":<20}")
    for dict in result:
        print("-"*150)
        print(f"{dict["Book_Type"]:<18}{dict["Book_Name"]:<28}{dict["SNo"]:<10}{dict["Quantity"]:<15}{dict["Available"]:<15}{dict["Rent"]:<10}₹{dict["Publish_Price"]:<20}₹{dict["Retail_Price"]:<20}₹{dict["Rental_Price_Per_Week"]:<20}")
    print("-"*150)
    Books()
    
def EditBook():
    tb=db["Books"]
    edit=1
    while(edit):
        sno=input("Enter SNo. of the book =")
        exist=tb.find_one({"SNo":sno})
        if(exist!=None):
            print("Press 1: To Edit Book Type.")
            print("Press 2: To Edit Book Name.")
            print("Press 3: To Edit Serial Number.")
            print("Press 4: To Edit No. of Available Books.")
            print("Press 5: To Edit No. of Rented Books.")
            print("Press 6: To Edit Publish Price.")
            print("Press 7: To Edit Retail Price.")
            print("Press 8: To Edit Rental Price/Week.")
            print("Press 9: To Exit\n")
            ch=int(input("Enter Your Choice ="))
            match ch:
                case 1:
                    field="Book_Type"
                    value=input("Enter New Value =")
                case 2:
                    field="Book_Name"
                    value=input("Enter New Value =")
                case 3:
                    field="SNo"
                    value=input("Enter New Value =")
                case 4:
                    field="Available"
                    value=int(input("Enter New Value ="))
                case 5:
                    field="Rent"
                    value=int(input("Enter New Value ="))
                case 6:
                    field="Publish_Price"
                    value=int(input("Enter New Value ="))
                case 7:
                    field="Retail_Price"
                    value=int(input("Enter New Value ="))
                case 8:
                    field="Rental_Price_Per_Week"
                    value=int(input("Enter New Value ="))
                case 9:
                    pass
            tb.update_one({"SNo":sno},{"$set":{field:value}})
            if(field=="Available"):
                value += exist["Rent"]
                tb.update_one({"SNo":sno},{"$set":{"Quantity":value}})
            if(field=="Rent"):
                value += exist["Available"]
                tb.update_one({"SNo":sno},{"$set":{"Quantity":value}})
            print("Field Successfully Edited.")
        else:
            print("No Book Found.")
        edit=int(input("Press 1: to edit more else Press 0: To Go Back ="))
    if(edit==0):
        Books()
        
def BillNo():
    import uuid
    random_uuid = uuid.uuid4()
    bn=str(random_uuid)
    return bn

def PrintBill(lt,dic,bn):
    print("\nYour Bill :-\n")
    print(f"Bill No.: {bn}\n")
    print(" "*53,dic["Date&Time"],"\n")
    print("Phone No. : ",dic["Phone"],"\n")
    print(f"{"Book Name":<25}{"SNo.":<10}{"Quantity":<15}{"Weeks":<10}{"Rent":<10}{"Total Rent":<10}")
    for item in lt:
        print(f"{item["Book_Name"]:<25}{item["SNo"]:<10}{item["Quantity"]:<15}{item["Weeks"]:<10}₹{item["Rent"]:<9}₹{item["Total_Rent"]:<10}")
    print("-"*80)
    print(f"{"Grand Total":<70}₹{dic["Grand_Total"]:<10}")

def Return(dic):
    sno=dic["SNo"]
    qty=dic["Quantity"]
    book=db["Books"].find_one({"SNo":sno})
    av=book["Available"] + qty
    rn=book["Rent"] - qty
    db["Books"].update_one({"SNo":sno},{"$set":{"Rent":rn}})
    db["Books"].update_one({"SNo":sno},{"$set":{"Available":av}})
        
def Fine(days,dic):
    rent=dic["Rent"]
    fine=(rent/2)*days
    return fine()
    
def Purchase(lt,dic,bn):
    print("\nYour Bill :-\n")
    print(f"Bill No.: {bn}\n")
    print(" "*38,dic["Date&Time"],"\n")
    print("Phone No. : ",dic["Phone"],"\n")
    print(f"{"Book Name":<25}{"SNo.":<10}{"Quantity":<15}{"Price":<10}{"Total":<10}")
    for item in lt:
        print(f"{item["Book_Name"]:<25}{item["SNo"]:<10}{item["Quantity"]:<15}₹{item["Price"]:<10}₹{item["Total"]:<10}")
    print("-"*65)
    print(f"{"Grand Total":<60}₹{dic["Grand_Total"]:<10}")

def CheckPassword(pswd):
    if(len(pswd)>=6 and any(char.isdigit() for char in pswd) and any(char.isupper() for char in pswd) and any(char.islower() for char in pswd) and any(not char.isalnum() for char in pswd)):
        return False
    else:
        return True

def CheckPhone(phone):
    if(phone.isdigit() and len(phone)==10):
        return False
    else:
        return True
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def Start():
    print("-"*150)
    print("CENTRAL LIBRARY".center(130))
    print("-"*150,"\n")
    print("Welcome to Central Library!\n")
    print("Press 1: For New Registration")
    print("Press 2: For Already Registered Users")
    print("Press 3: For Books")
    print("Press 4: To Exit\n")
    
    a=1
    while(a):
        mainchoice=input("Enter Your Choice =")
        if(mainchoice.isdigit()):
            ch=int(mainchoice)
            a=0
            match ch:
                case 1:
                    print("\n-"*150)
                    print("REGISTRATION WINDOW".center(130))
                    print("-"*150,"\n")
                    name=input("Enter Your Name =")
                    print("Choose a strong password.\nYour password should be atleast 6 characters long.\nYour password must contain uppercase and lowercase letters, numbers and a special character.\n")
                    x=True
                    while(x): 
                        pswd=input("Enter Your Password =")
                        x=CheckPassword(pswd)
                        if(x==True):
                            print("Invalid Password.\nTry Again.")
                    y=True
                    while(y):
                        phone=input("Enter Your Phone =")
                        y=CheckPhone(phone)
                        if(y==True):
                            print("Invalid Phone number.\nTry Again.")
                        exist=db["tbUsers"].find_one({"Phone":phone})
                        if(exist==None):
                            obj={
                                "Name":name,
                                "Password":pswd,
                                "Phone":phone
                            }
                            db["tbUsers"].insert_one(obj)
                            print("User Successfully Registered.")
                        else:
                            print("User Already Registered.")
                            
                    User(phone,name)
                    
                case 2:
                    y=True
                    while(y):
                        print("\n-"*150)
                        print("LOGIN WINDOW".center(130))
                        print("-"*150,"\n")
                        phone=input("Enter Your Phone =")
                        y=CheckPhone(phone)
                        if(y==True):
                            print("Invalid Phone number.\nTry Again.")
                        exist=db["tbUsers"].find_one({"Phone":phone})
                        if(exist!=None):
                            pswd=input("Enter Your Password =")
                            if(exist["Password"]==pswd):
                                print("User Found.")
                                name=exist["Name"]
                            else:
                                print("Wrong Password.")
                        else:
                            print("User Not Found.")
                        
                    User(phone,name)    
                            
                case 3:
                    print("\n-"*150)
                    print("BOOKS WINDOW".center(130))
                    print("-"*150,"\n")
                    Books()
                        
                case 4:
                    pass
                
                case default:
                    print("Please Enter a Valid Choice.")
        else:
            print("Please Enter a Digit.")

Start()
