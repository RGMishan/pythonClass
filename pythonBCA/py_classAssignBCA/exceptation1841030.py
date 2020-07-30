import sys 

print("Python Practice Program")
print("Mishan Regmi 5BCA A '1841030'\n")

#try 1
#Handling the exception thrown using try and except blocks.
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("An error occurred!")

#try 2
#using try and except block and finally block to print 'All Done.'
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't divide by Zero!")
finally:
    print('All Done!') 

#try3
#Using a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
            
        
    print('Thank you, your number squared is: ',n**2)

ask()