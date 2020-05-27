#Practice Questions: 1
#Exploring operators in Python(Operators: arithmetic, logical relational , Boolean operator, index  

print("Lab 1 Python")
print("Domain: Income Evaluation\n")
print("Arithmetic Operator\n")

#Introducning User
name = input("Enter your name: ")
print("Welcome back", name)

#Getting Salary Detail
salary1 = input("Enter your salary of month April:")
salary2 = input("Enter your salary of month May  :")
salary1 = int(salary1)
salary2 = int(salary2)

print("\nThe salary of April and May total is:", salary1 + salary2)
expenses = input("Enter the expenses of month April:")
expenses = int(expenses)
saving = salary1 - expenses
print("Your total saving of April is:", saving)

rate = input("Enter the interest rate of your bank:")
rate = float(rate)
print("Checking if your bank has good rate of interest.....")
if rate > 7.5:
 print(True)
 print("Rate is good.")
else:
 print(False)
 print("Try SBI bank they give 7.6%pm.")
print("Your interest in April month is:", (saving*(1/12)*rate)//100 )

print("\nLogical Operator")
if (salary1 < salary2 and saving > 500):
 print("You are earning good and saving money.")
elif (salary1 > salary2 or saving < 500):
 print("You need to earn more or save money.")
elif (not(salary1 < salary2 and saving > 500)):
 print("Need to look for next job and save more money")

print("Index Operator")
lst = [] #Initialized List
  
# number of elements as input 
n = int(input("Enter number of household item you bought today: ")) 

for i in range(0, n): 
 item = str(input("Enter item :")) 
 lst.append(item) # adding the element 

print("You bought carrot in",lst.index('carrot') , "position.") 

i = 0
print("\nContinue")
while i < len(lst):
 print(lst[i])
 i+=1
 continue

print("\nBreak")
i = 0
while i <len(lst):
 if lst[i] == "mango":
  print("\nMango found.")
  break
 i+=1
