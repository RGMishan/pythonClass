import re
import collections
'''
# 1.Explore any 5 string functions in python.
# 2. Given a paragraph
#Python is an interpreted, high-level, general-purpose programming language. Guido van Rossum is the 
#father of python. In the year 1991 pytthon was officially released. Python's design philosophy
#emphasizes code readability with its notable use of significant whitespace.Python follows
#object-oriented approach. Python is famous as all purpose programming language.


#Perform the following tasks:


#5. Find a mechanism to give the count of total number of characters excluding whitespaces.

# 3. Write a program in python to mimic any word game.

print("Lab 2 Python")
print("Mishan Regmi 5BCA A '1841030'")

print("\nQuestion 1")
name = input("Enter your name: ")
sur = input("Enter your surname: ")

cap = name.capitalize() #Capitalize the first letter
print("After capitilization: ", cap)
name = name.capitalize()
sur = name.capitalize()

check = name.endswith('an') #Check the last letter
print("Checking the end string of name. ", check)
text = "\nThis is the string you can you to check next function."
print(text)
part = input("\nEnter string to search from text.")
found = text.find(part) #gives the index of the sting to be found

print("The string is found at ", found) 

print("\nMy name is {} .And surname is {}".format(name,sur)) #format the input

start = sur.startswith('R') #check if the string start with 
print("Checking the surname starting string. " ,start) 

text2 = " "
a = '12345'
joining = text2.join(a)
print("The String after join is: ", joining)
'''
print("\nQuestion Number 2")

para = open("C:\\Users\\Mishan RG\\Desktop\\PyClassNew\\pythonBCA\\py_classAssignBCA\\lab3file.txt", 'r')


reading = "Python is an interpreted, high-level, general-purpose programming language. Guido van Rossum is the\nfather of python. In the year 1991 pytthon was officially released. Python's design philosophy\nemphasizes code readability with its notable use of significant whitespace.Python follows\nobject-oriented approach. Python is famous as all purpose programming language."
print(reading)
#1 find the most repeated character in the paragraph and turn it to caps. Break the paragraph into lines.
print("The most repeating character is :", collections.Counter(reading).most_common(1)[0])

#2 After splitting into lines find total number of words, lines and characters in the given input.
lineList = len(reading.split('\n'))
print("The number of lines are: ", lineList)

res = len(reading.split()) 
print("The number of words in string are:", res)

cou = len(reading)
print("The number of character are: ",cou)

#3 split the first line using coma as the delimiter.

lines = para.readlines()
firstLine= lines[0]

commaSep = firstLine.split(",")
print(commaSep)

#4 Fetch the word “Python or python ” from the number of lines (give the word to be searched as user
#  input) replace the word as 'PyThOn'. use suitable inbuilt functions to perform the tasks.
'''
while True:
    string = reading 
    count = len(re.findall("[a-zA-Z_]+", string))
    if line == "Done": #command to terminate the loop
        break
    print (count)
print ("Terminated")
'''
textAgain = "Python is an interpreted, high-level, general-purpose programming language. Guido van Rossum is the father of python. In the year 1991 pytthon was officially released. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Python follows object-oriented approach. Python is famous as all purpose programming language." 

def checking(str, userIn):
 str = str.split()          
 str2 = [] 
 for i in str:              
  if userIn not in str2: 
   str2.append(userIn) 
 print('Frequency of', userIn,'is :', str.count(str2))
 print(str2)
ask = input("Enter the word to search.")
checking(textAgain,ask)