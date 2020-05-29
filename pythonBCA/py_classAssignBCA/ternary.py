# l = starting index
# r = length of our list
# key = element to be searched
# ar = name of the list

def ternarySearch(l, r, key, ar): 
    if (r >= l): #confirming the length of list is correct
        mid1 = l + (r - l) //3 # looking for mid1
        mid2 = r - (r - l) //3 # looking for mid 2
        if (ar[mid1] == key):  #checking match with mid 1
            return mid1     
        if (ar[mid2] == key):  #checking match with mid 2
            return mid2 
        if (key < ar[mid1]): #if key is less than mid 1
            return ternarySearch(l, mid1 - 1, key, ar) #another iteration and search on beofre mid 1
            return ternarySearch(mid2 + 1, r, key, ar) #another iteration and search on after mid 1
        else:  
            return ternarySearch(mid1 + 1, mid2 - 1, key, ar) #search in mid 2
    return -1
#initialize of value for the search
ar = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]  #list
l = 0 #starting index
r = 9 #end index
key = 7 #value to be searched
p = ternarySearch(l, r, key, ar) #the function 
print("Index of", key, "is", p) 