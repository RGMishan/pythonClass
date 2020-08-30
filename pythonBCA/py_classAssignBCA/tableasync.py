from tkinter import *  
  
class Table: 
    def __init__(self,root): 
          
        # code for creating table 
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                self.e = Entry(root, width=20, fg='blue', 
                               font=('Arial',16,'bold')) 
                  
                self.e.grid(row=i, column=j) 
                self.e.insert(END, lst[i][j]) 
  
# take the data 
lst = [(1,'Mishan','Regmi',21), 
       (2,'Yobah','Bertrand',20), 
       (3,'Peter','Josh',20), 
       (4,'Rachna','Shrestha',21), 
       (5,'Shubham','Sharma',21)] 
   
# find total number of rows and 
# columns in list 
total_rows = len(lst) 
total_columns = len(lst[0]) 
   
# create root window 
root = Tk() 
t = Table(root) 
root.mainloop() 