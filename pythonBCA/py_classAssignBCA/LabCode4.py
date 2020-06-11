import sys 
'''
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
print("The difference in sort nd sorted is that sort() will sort the given list\n")
print("And the sorted will make a new variable and store value there.\n")
print("----------------------------------------------------------------")
'''

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
