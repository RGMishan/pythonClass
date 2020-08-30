from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry('850x550')
root.title("Student Info Center")
root.configure(background="silver")

#Entry widget object

textin=StringVar()

#Dictionaries

exlist={'Mishan':'Developer','Deep':'Designer','Rohan':'Managing Director','Aastha':'Financial Manager','A':'Actor',
        'B':'Baseball Player','C':'Comedian'}

def clk():
     entered = ent.get()
     output.delete(0.0,END)
     try:
          textin = exlist[entered]
     except:
          textin = 'SORRY NO INFO \n AVAILABLE!!!!!!!!\n'
     output.insert(0.0,textin)

def ex():
   tkinter.messagebox.showinfo("Program",'Exit')
   exit()
     
def exitt():
     tkinter.messagebox.showinfo("Program",'Exit')
     exit()   

def me():
     text='\n XYZ \n OKAY \n Nice'
     saveFile=open('text.txt','w')
     saveFile.write(text)
     print('This are the entries::',text)
     
   
def hel():
   help(tkinter)
   
def cont():
     tkinter.messagebox.showinfo("Developed By",'\n 1.Mishan Regmi\n 2.Arjun Adhikari \n')

def clr():
     textin.set(" ")

menu = Menu(root)
root.config(menu=menu)

subm = Menu(menu)
menu.add_cascade(label="File",menu=subm)
subm.add_command(label="Save")
subm.add_command(label="Exit",command=ex)


subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Contributors",command=cont)


lab=Label(root,text='Name :',font=('none 20 bold'))
lab.grid(row=0,column=1,sticky=W)

ent=Entry(root,width=20,font=('none 18 bold'),textvar=textin,bg='white')
ent.grid(row=0,column=2,sticky=W)


but=Button(root,padx=2,pady=2,text='Submit',command=clk,bg='powder blue',font=('none 18 bold'))
but.place(x=100,y=90)


but4=Button(root,padx=2,pady=2,text='Clear',font=('none 18 bold'),bg='powder blue',command=clr)
but4.place(x=220,y=90)



output=Text(root,width=20,height=8,font=('Time 20 bold'),fg="black")
output.place(x=100,y=200)


labb=Label(root,text='Results',font=('non 18 bold'))
labb.place(x=0,y=180)


but1=Button(root,padx=2,pady=2,text='Exit',command=exitt,bg='powder blue',font=('none 18 bold'))
but1.place(x=200,y=470)

root.mainloop()