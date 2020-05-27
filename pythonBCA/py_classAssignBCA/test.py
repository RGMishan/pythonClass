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

