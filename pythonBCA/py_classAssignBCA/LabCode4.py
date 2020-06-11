import sys 
from heapq import heappop, heappush

print("Lab 4 Python")
print("Mishan Regmi 5BCA A '1841030'\n")


#À. Explore various built-in functions used for sorting in python. How sort() is different from sorted()?
# type1
n=int(input("Enter the number of the employee: ")) 

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
n=int(input("\nEnter the amount of goods bought: ")) 

#create a empty list to store values
A=[]  
print("\nName the goods")
for i in range(n): 
 A.append(input(""))

for i in range(len(A)): 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
     
    A[i], A[min_idx] = A[min_idx], A[i] 

print ("\nSorted goods are:") 
for i in range(len(A)): 
    print("%s" %A[i]) 

#heap sort
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



