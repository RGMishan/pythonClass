from tkinter import *
from tkinter import messagebox 
root = Tk() 
root.geometry("800x500") 
  
w = Label(root, text ='Christ University', font = "50")  
w.pack() 
  
menubutton = Menubutton(root, text = "Login As", bg='grey')    
    
menubutton.menu = Menu(menubutton)   
menubutton["menu"]= menubutton.menu   
  
var1 = IntVar() 
var2 = IntVar() 
  
menubutton.menu.add_checkbutton(label = "Student", variable = var1)   
menubutton.menu.add_checkbutton(label = "Teacher", variable = var2)
    
menubutton.pack()   

#button
print("\n\n")
w = Label(root, text ='Choose Langauge', font = "30")  
w.pack() 
  
Checkbutton1 = IntVar()   
Checkbutton2 = IntVar()   
  
Button1 = Checkbutton(root, text = "Python", variable = Checkbutton1,onvalue = 1,offvalue = 0,height = 2, width = 8)
Button2 = Checkbutton(root, text = "Java",variable = Checkbutton2,onvalue = 1,offvalue = 0,height = 2,width = 8)
    

Button1.pack()   
Button2.pack()   

w.pack()  
messagebox.askretrycancel("Testing Network!!!", "Try again?")  

#radio
x = Label(root, text ='Select Your Gender', font = "30") 
x.pack()
v = StringVar(root, "1") 

# Dictionary to create multiple buttons 
values = {"Male" : "1",  "Female" : "2"} 

for (text, value) in values.items(): 
    Radiobutton(root, text = text, variable = v, value = value).pack(side = TOP, ipady = 5) 

#ScrollBar
z = Label(root, text ='Scroll Please', font = "50")  
z.pack() 
scroll_bar = Scrollbar(root) 
  
scroll_bar.pack( side = RIGHT, fill = Y ) 
   
mylist = Listbox(root,  yscrollcommand = scroll_bar.set ) 
   
for line in range(10, 25): 
    mylist.insert(END, "18410" + str(line)) 
  
mylist.pack( side = TOP, fill = None ) 
  
scroll_bar.config( command = mylist.yview ) 

root.mainloop()