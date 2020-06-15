import sys 
from heapq import heappop, heappush

print("Lab 4 Python")
print("Mishan Regmi 5BCA A '1841030'\n")


#À. Explore various built-in functions used for sorting in python. How sort() is different from sorted()?
# type1
n=int(input("Enter the number of the employee: ")) 
print("Enter the salary.\n")
#create a empty list to store values
listt=[]  
for i in range(n): 
 listt.append(int(input("")))
listt.sort()

print("\nThe sorted list of employee salary in ascenting order is:\n",listt)


# type2 
print("Enter the name of the employee.\n")
lis = []
for i in range(n): 
 lis.append(input(""))
 sorted_list = sorted(lis, key=len)
print("The name sorted in length is:\n", sorted_list)

print("----------------------------------------------------------------")
print("The difference in sort nd sorted is that sort() will sort the given list no return.\n")
print("And the sorted will make a new variable and store value there return the list.\n")
print("----------------------------------------------------------------")

# B. Write a program in Python to implement selection sort and Heap sort.
# Include the concept of list, functions and tuples wherever applicable.

#selection sort
print("Selection Sort\n")
n=int(input("\nEnter the amount of goods bought: ")) 

#create a empty list to store values
A=[]  
print("\nName the goods")
for l in range(n): 
 A.append(input(""))

for l in range(len(A)): 
    min_idx = l 
    for j in range(l+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
     
    A[l], A[min_idx] = A[min_idx], A[l] 

print ("\nSorted goods are:") 
for l in range(len(A)): 
    print("%s" %A[l]) 

#heap sort
print("\nHeap Sort\n")
def heap_sort(name):
    heap = []
    for element in name:
        heappush(heap, element)
    ordered = []
    # While we have elements left in the heap
    while heap:
        ordered.append(heappop(heap))
    return ordered

c=int(input("\nEnter the number of branch.")) 
company=[]  
for i in range(c): 
 company.append(input(""))
print("Company Branch in sorted order is\n",heap_sort(company))

# C. Write a program to calculate the annual sales of an e-commerce company for past 5 
# years. Display the quarterly sales of the year 2018 in decreasing order. Use the lambda
# function for performing accounting operations and user defined functions for displaying 5
# years sales and quarterly sales of 2018.

print("\n3. Company Application\n")
rev = float(input("Enter company's year revenue."))
sales = float(input("Enter the sales of the year."))
exp = float(input("Enter the total expenses of the year."))
i = 0

while i < 1:
    print("\n 1. Calculate yearly profit and Quaterly\n 2. Check Growth \nType 'done' if your work is finished")
    che = int(input("\nChoose what you want to do."))
    if che != 'done':
        if che == 1:
            profit = rev - exp
            print("\nYour profit of this year is", profit)
            firstQ = profit/4
            print("\nYour company made a profit of Rs.", firstQ ,"in the first quarter.")
        elif che == 2:
            if (profit < exp):
                print("\nCompany is growing keep working hard.")
            else:
                print("\nNeed more inprovemnt in finance management.")
        else:
            print("Invalid choice.")
            pass
    else:
        i = i + 1
        break
else:
    print("Invalid Input")
