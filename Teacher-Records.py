# Teacher Records
import pymongo as py
client=py.MongoClient("mongodb://localhost:27017/")
db=client["dbschool"]
tb=db["tbteacher"]
turn=True
while(turn):
    print("Press 1: to insert a teacher's record")
    print("Press 2: to update a teacher's record")
    print("Press 3: to delete a teacher's record")
    print("Press 4: to display teacher's record")
    print("Press 5: to Exit")
    choice=int(input("Enter your choice"))

    if(choice==1):
        lt=[]
        turn1=1
        while(turn1):
            ID=int(input("Enter Teacher's ID="))
            Name=input("Enter Teacher's Name=")
            Subject=input("Enter the Subject=")
            Phone=int(input("Enter Phone no.="))
            Address=input("Enter the Address=")
            Salary=int(input("Enter the Salary="))
    
            dict={
                "ID":ID,
                "Name":Name,
                "Subject":Subject,
                "Phone":Phone,
                "Address":Address,
                "Salary":Salary
            }
            lt.append(dict)

            print("Press 1: to add another record.")
            print("Press 0: to Exit.")
            turn1=int(input("Enter your choice="))
            
        tb.insert_many(lt)
        
    if(choice==2):
        turn2=True
        name=input("Enter the Name of the record you want to update=")
        print("Press 1: to update ID")
        print("Press 2: to update Name")
        print("Press 3: to update Subject")
        print("Press 4: to update Phone No.")
        print("Press 5: to update Address")
        print("Press 6: to update Salary")
        print("Press 7: to Exit")
        choice1=int(input("Enter your choice="))
        while(turn2):
            if(choice1==1):
                ID=input("Enter new ID for the record=")
                tb.update_one({"Name":name},{"$set":{"ID":ID}})
                turn2=False14
            if(choice1==2):
                Name=input("Enter new Name for the record=")
                tb.update_one({"Name":name},{"$set":{"Name":Name}})
                turn2=False
            if(choice1==3):
                Subject=input("Enter new Subject for the record=")
                tb.update_one({"Name":name},{"$set":{"Subject":Subject}})
                turn2=False
            if(choice1==4):
                Phone=input("Enter new Phone for the record=")
                tb.update_one({"Name":name},{"$set":{"Phone":Phone}})
                turn2=False
            if(choice1==5):
                Address=input("Enter new Address for the record=")
                tb.update_one({"Name":name},{"$set":{"Address":Address}})
                turn2=False
            if(choice1==6):
                Salary=input("Enter new Salary for the record=")
                tb.update_one({"Name":name},{"$set":{"Salary":Salary}})
                turn2=False
            if(choice1==7):
                turn2=False
                
    if(choice==3):
        print("Press 1: to delete a record")
        print("Press 2: to delete all records")
        choice2=int(input("Enter your choice="))
        while(turn3):
            if(choice2==1):
                name=input("Enter the name whose record you want to delete=")
                tb.delete_one({"Name":name})
                print("Press 1: to delete another record")
                print("Press 0: to Exit")
                turn3=int(input("Enter your choice="))
            if(choice2==2):
                tb.delete_many({})
                turn3=0
        
    if(choice==4):
        turn3=1
        while(turn3):
            print("Press 1: to Display all records")
            print("Press 2: to Display any 1 records")
            choice3=int(input("Enter your choice="))
            if(choice3==1):
                result=tb.find()
                for dict in result:
                    print(dict)
                turn3=0
            if(choice3==2):
                name=input("Enter the Name of the record you want to display=")
                result=tb.find_one({"Name":name})
                print("Press 1: to Display another record")
                print("Press 0: to Exit")
                turn3=int(input("Enter your choice="))
            
    if(choice==5):
        turn=False