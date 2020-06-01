print("Lab 2 Python")
print("Mishan Regmi 1841030 5 BCA 'A'\n")
print("Calculations \n")

import math

print(" 1. Simple Calculator\n 2. Scientific Calculator\n 3. Company Program\n Type 'done' if you are done")
m = 0
while m < 1:
  ch = input("\nChoose your calculation. ")
  if ch != 'done':
    if ch == '1':
      print("A Simple Calculator\n")
      def add(n1, n2): 
          return n1 + n2 

      def sub(n1, n2): 
          return n1 - n2 

      def mult(n1, n2): 
          return n1 * n2 

      def div(n1, n2): 
          return n1 / n2 
        
      print("Please select operation:\n")
      print(" 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n \nEnter 'done' if you are done.") 
      i = 0

      while i < 1:
        choice = input("\nSelect operations:")
        if choice != 'done':  
          num1 = int(input("\nEnter first number: ")) 
          num2 = int(input("Enter second number: ")) 
        
          if choice == 1: 
            print("Result:", num1, "+", num2, "=", add(num1, num2)) 
        
          elif choice == 2: 
            print("Result:", num1, "-", num2, "=", sub(num1, num2)) 
        
          elif choice == 3: 
            print("Result:", num1, "*", num2, "=",  mult(num1, num2)) 
        
          elif choice == 4: 
            print("Result:", num1, "/", num2, "=", div(num1, num2)) 
          else: 
            print("Invalid input. Please enter again.") 
        else:
          i = i + 1
          break
    elif ch == '2':
      print ("\nA Simple Scientific Calculator")
      print('''
      Operator Available
      ^     for power
      r     for root
      %     for modulus
      pie   for Pie
      sin   for sin (trig)
      cos   for cos (trig)
      tan   for tan (trig)
      !     for factorial 
      ln    for ln (natural log)
      ''')
      firstNumber = float(input("Enter first number: "))
      op = input("Enter the operator: ").lower()
      secondNumber = float(input("Enter second number: "))

      if op == "^":
          print (firstNumber, "^", secondNumber, "=", firstNumber ** secondNumber )
      elif op == "r":
          print (firstNumber, "root", secondNumber, "=", secondNumber ** (1 / firstNumber) )
      elif op == "%":
          print (firstNumber, "%", secondNumber, "=", firstNumber % secondNumber )
      #factorial
      elif op == "!":
          theNumber = firstNumber = secondNumber 
          secondNumber = 1
          while firstNumber > 1:
              secondNumber *= firstNumber 
              firstNumber = firstNumber - 1  
          print ("n!(", theNumber, ")=", secondNumber )
      elif op == "sin":
          print ("sin(", secondNumber, ")=", math.sin(secondNumber ))
      elif op == "cos":
          print ("cos(", secondNumber, ")=", math.cos
          (secondNumber ))
      elif op == "tan":
          print ("tan(", secondNumber, ")=", math.tan(secondNumber ))
      elif op == "pie" or op == "pi":
          print ("Pie =", math.pi)
      elif op == "ln":
          print ("ln(", secondNumber , ")= ", math.log(secondNumber))
      else:
          print ("incorrect operator") 
      
    elif ch == '3':
      print("\nBank Application\n")
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
  else:
    m = m + 1
    print("\nThank You Program Closed")
    break
