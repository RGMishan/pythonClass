print("Lab 5 Python")
print("Mishan Regmi 1841030 5 BCA 'A'\n")
print("Calculations \n")

#DOMAIN EDUCATION FEES COLLECTION AND SCHOLARSHIP

class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print("Hello!!! Welcome to the Eduction Donation CO.") 
  
    def deposit(self): 
        amount=float(input("Enter amount you want to donate: ")) 
        self.balance += amount 
        print("\n Fees Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter the balance to withdraw (only for needy) :")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Received:", amount) 
        else: 
            print("\n Sorry You can't access that amount.") 
  
    def display(self): 
        print("\n TOTAL DONATION RECEIVED",self.balance) 
  

   
# creating an object of class 
s = Bank_Account() 
   
# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display() 

# ## Billing process QUESTION NUMBER

class Bill():
    
    ##Details of shopping stored in dictionary
    store={"9%":{"item":[],'quantity':[],'price':[]},"6%":{"item":[],'quantity':[],'price':[]},"2.5%":{"item":[],'quantity':[],'price':[]}}
    
    ##To initialize name of customer
    def __init__(self,name,number):
        
        self.Cust_name=name
        self.Cust_number=number
        
    
    ##To Insert An Element    
    def insert(self,item,gst):
        gst_perc=''
        if(gst==1):
            item[2]=item[2]+ (9/100)*item[2]
            gst_perc='9%'
            
        elif(gst==2):
            item[2]=item[2]+ (6/100)*item[2]
            gst_perc='6%'
        
        elif(gst==3):
            item[2]=item[2]+ (2.5/100.0)*item[2]
            gst_perc='2.5%'
        
        self.store[gst_perc]["item"].append(item[0])
        self.store[gst_perc]["quantity"].append(item[1])
        self.store[gst_perc]["price"].append(item[2])     
        
    ##To remove item in Stack   
    def pop(self,gst):
        gst_perc=''
        if(gst==1):
            gst_perc='9%'
            
        elif(gst==2):
            gst_perc='6%'
        
        elif(gst==3):
            gst_perc='2.5%'
        
        del self.store[gst_perc]["item"][-1]
        del self.store[gst_perc]["quantity"][-1]
        del self.store[gst_perc]["price"][-1]  
        
        
    ##To display Total Bill   
    def display(self):
        
        print("**************************************************")
        print("\nName: {}\tContact: {}".format(self.Cust_name,self.Cust_number))
        print("\n------------------------------------------------")
        print("Particulars\tQuantity\tPrice")
        print("\n------------------------------------------------")
        temp=0
        Total=0
        for i in self.store:
            temp+=1
            print("\n{} CGST {} SGST {}".format(temp,i,i))
            
            for j in range(len(self.store[i]['item'])):
                
                print("{}\t\t{}\t\t{}".format(self.store[i]['item'][j],self.store[i]['quantity'][j],self.store[i]['price'][j]))
                Total=Total+(self.store[i]['price'][j]*float(self.store[i]['quantity'][j]))
        print("\n-------------------------------------------------")
        
        print("Total\t\t\t\t{}".format(Total))
        print("**************************************************")
    
    ##Overloading len function display total quantity of item
    def __len__(self):
        return sum(self.store["9%"]['quantity'])+sum(self.store["6%"]['quantity'])+sum(self.store["2.5%"]['quantity'])
        

while True:
    
    while True:
        print("\n-----------CUSTOMER DETAILS----------")
        name=input("\nName: ")
        Number=input("Number: ")
        print("---------------------------------------\n")
        try:

            if Number.isnumeric() and name.isalpha() and len(Number)==10:
                break
            else:
                print("Invalid Input....Enter Again")
                print("Note: 4Length of Phone Number should be 10\n\tName should contain only alphabets")
        except Exception:
            print("Error occured")
        
    User=Bill(name,Number)
    
    while True:
        while True:
            try:
                choice=int(input("Choose from the following:\n\n\t1) Insert Item \n\t2) Remove Item \n\t3) Total Items in list\n\t4) Total Bill\n\t5) Exit\n\nInput: "))
                break
            except Exception:
                print("\nInvalid input...!")

        if choice==1:
            item_name=input("\nItem Name: ")
        
            while True:
                try:
                    quant=int(input("Quantity: "))
                    if quant>0:
                        break
                    else: 
                        print("Quantity should be grater than 0...")
                except Exception:
                    print("Invalid Input")

            while True:
                try:
                    price=float(input("Price: "))
                    if price>0:
                        break
                    else: 
                        print("Price cannot be negative...")
                except Exception:
                    print("Invalid Input")
            while True:
                try:
                    gst=int(input("Choose CGST% & SGST% :\n1) 9%\n2) 6%\n3) 2.5%\n\n\t"))
                    if gst ==1 or gst==2 or gst==3:
                        break
                    else:
                        print('Input only 1 or 2 or 3..')
                except Exception:
                    print("Invalid Input....")
            
            item=[item_name,quant,price]
            
            User.insert(item,gst)

        elif choice==2:
            while True:
                try:
                    print("REMOVE ITEM from list with GST percentage")
                    gst=int(input("\nChoose CGST% & SGST% :\n1) 9%\n2) 6%\n3) 2.5%\n\n\t"))
                    if gst ==1 or gst==2 or gst==3:
                        break
                    else:
                        print('Input only 1 or 2 or 3..')
                except Exception:
                    print("Invalid Input....")
            User.pop(gst)

        elif choice==4:
            User.display()
        
        elif choice==3:
            print("Total Item ",len(User))
            
        elif choice==5:
            User.display()
            
            print("\n\nThanku for your Purchase!!!")
            break
        else:
            print("Invalid Input....!")
    c=input("Input Details for Next Customer..press(Y/y) ")
    if c=='y' or c=="Y":
        pass
    else:
        break