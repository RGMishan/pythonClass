# Import tkinter 
from tkinter import *
class LoanCalculator: 

    def __init__(self): 

        window = Tk() # Create a window 
        window.title("Loan Calculator") # Set title 
        # create the input boxes. 
        Label(window, text = "Rate of Interest").grid(row = 1, column = 1, sticky = W) 
        Label(window, text = "Time (In Years)").grid(row = 2, column = 1, sticky = W) 
        Label(window, text = "Principle Amount").grid(row = 3, column = 1, sticky = W)  
        Label(window, text = "Simple Interest").grid(row = 4, column = 1, sticky = W) 

        # for taking inputs 
        self.annualInterestRateVar = StringVar()  
        Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 1, column = 2) 
        self.numberOfYearsVar = StringVar() 

        Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 2, column = 2) 
        self.loanAmountVar = StringVar() 

        Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2) 
        self.monthlyPaymentVar = StringVar() 
        lblMonthlyPayment = Label(window, textvariable = self.monthlyPaymentVar).grid(row = 4, column = 2, sticky = E) 

        self.totalPaymentVar = StringVar() 
        lblTotalPayment = Label(window, textvariable = self.totalPaymentVar).grid(row = 5, column = 2, sticky = E) 
        
        # create the button 
        btComputePayment = Button(window, text = "Compute Payment", bg="red", command = self.computePayment).grid( row = 6, column = 2, sticky = E)  
        window.mainloop() # Create an event loop 

    # compute the total payment. 
    def computePayment(self): 

        monthlyPayment = self.getMonthlyPayment( 
        float(self.loanAmountVar.get()), 
        float(self.annualInterestRateVar.get()), 
        int(self.numberOfYearsVar.get())) 

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f')) 
        totalPayment = float((loanAmount * numberOfYears * monthlyInterestRate) / 100) 

        self.totalPaymentVar.set(format(totalPayment, '10.2f')) 
  
    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):  
        # compute the monthly payment. 
        monthlyPayment = (loanAmount * numberOfYears * monthlyInterestRate) / 100 
        return monthlyPayment; 
        root = Tk() # create the widget 
  
 # call the class to run the program. 
LoanCalculator() 