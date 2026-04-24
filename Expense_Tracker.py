
print("Expense Tracker")
expenses=[]
print("====Menue====")
while True:
 print("1. Add Expense\n2. View All Expense\n3. View Total Expense\n4. Exit")
 
 choice=int(input("Please Enter your choice:"))
 

 if choice==1:
    date= input("What was the date? ")
    catagory=input("What did you buy? ")
    food=input("What you eat? ")
    payment=int(input("How much do you pay? "))

    expense= {
    "date" : date,
    "catagory" : catagory,
    "food" : food,
    "payment" : payment
     } 
    expenses.append(expense)
    print("Expenses added sucessfully")

 choice=int(input("enter your choice"))

 if choice==2:
        
        total= sum([expense["payment"] for expense in expenses])
        print ("Your total expenses is ",total)
        

                
 elif choice!=4:
     print("Plz give all the expenses info first")
 break

else :
    print("Goodby")
 

