print ("Python")
print ("Assignment 2")

print ('Task 0')

myString = "Hello! \nWelcome to Python class on STRINGS.\nThis is our 2nd Lab class."
print (myString)

print("\nTask 1")
print("Built-in String Function")

#1 Start With
sli = myString.startswith("elc")
print(sli) #print false as the string start with Hello
#2
sli = myString.startswith("Hel")
print(sli) #print True as the string start with Hello
#3
cou = myString.count("class")
print(cou) # print 2 by counting "class" character in string
#4
fin = myString.find("on")
print(fin) # print 23 by getting the index of "on" from string
#5
myString2 = " Joining this string"
jon = "+".join(myString2)
print(jon) # join all character of string with (+)
#6
myString3 = "     Strip Me     "
stp = myString3.strip()
print(stp) # Remove the white space from the string

print("\nTask 2")
print("\nIndex Operator")
result = myString.index('to Python')
print("Substring 'to Python' is in:", result, "position.")

print("\nLogical Operator")
str1 = "Python"
str2 = "Programming"
if str1 == "Python" or str2 == "Prog" :
    print("One Condition Match")

if str1 == "Python" and str2 == "Prog" :
    print("Both Condition Match")

print("\nMembership Operator")
if "Welcome" in myString:
    print("(Welcome) found in myString")
if "Mishan" not in myString:
    print("(Mishan) not found in myString")

print("\nIdentity Operator")
print(type(myString))
num = 5
num1 = "5"
num2 = 5.0
num3 = True
print(type(num))
print(type(num1))
print(type(num2))
print(type(num3))

print("\nConcatenating Operator")
new = myString + myString2
print(new)
