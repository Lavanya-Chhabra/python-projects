# Banking System
class bank:
    def openaccount(self,x,y):
        self.accno=x
        self.balance=y

    def deposit(self,money):
        self.balance=self.balance+money

    def withdraw(self,money):
        if(money>self.balance):
            print("Insufficient Balance")
        else:
            self.balance=self.balance-money 

    def checkbalance(self):
        print("Account No.=",self.accno)
        print("Balance",self.balance)

cust1=bank()
cust2=bank()
cust3=bank()

cust1.openaccount(101,10000)
cust2.openaccount(202,20000)
cust3.openaccount(303,30000)

choice=1
while(choice!=4):
    print("Press 1: for deposit")
    print("Press 2: for withdrawal") 
    print("Press 3: for checkbalance") 
    print("Press 4: for exit")
    choice=int(input("Enter your choice=")) 
    
    if(choice==1):
        print("Press 1 for customer 1")
        print("Press 2 for customer 2")
        print("Press 3 for customer 3")
        choice1=int(input("Enter your choice="))
        money=int(input("Enter the amount="))
        if(choice1==1):
            cust1.deposit(money)
        if(choice1==2):
            cust2.deposit(money)
        if(choice1==3):
            cust3.deposit(money)
    if(choice==2):
        print("Press 1 for customer 1")
        print("Press 2 for customer 2")
        print("Press 3 for customer 3")
        choice1=int(input("Enter your choice="))
        money=int(input("Enter the amount="))
        if(choice1==1):
            cust1.withdraw(money)
        if(choice1==2):
            cust2.withdraw(money)
        if(choice1==3):
            cust3.withdraw(money)
        
    if(choice==3):
        print("Press 1 for customer 1")
        print("Press 2 for customer 2")
        print("Press 3 for customer 3")
        choice1=int(input("Enter your choice="))
        if(choice1==1):
            cust1.checkbalance()
        if(choice1==2):
            cust2.checkbalance()
        if(choice1==3):
            cust3.checkbalance()        