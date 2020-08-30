import tkinter as tk
from tkinter import ttk
from tkinter import *

root = Tk()
root.geometry('1550x650')
root.configure(background='#C0C0C0')
root.title('Mishan 1841030')

def btnClickFunction():
    pass
with open("paragraphRegex.txt", "r") as f:
 Label(root, text=f.read()).place(x=10, y=50)

Label(root, text='REGEX OPERATION', bg='#FF0000', font=('times new roman', 15, 'bold')).place(x=50, y=10)

Button(root, text='CLICK ME', bg='#228B22', height=1, width=14, font=('MV Boli', 16, 'normal'),command=btnClickFunction).place(x=180, y=160)

Label(root, text='Total Paragraph', bg='#FF0000', font=('times new roman', 15, 'bold')).place(x=50, y=230)
Label(root, text='End With E', bg='#FF0000', font=('times new roman', 15, 'bold')).place(x=50, y=300)
Label(root, text='Capital Letter', bg='#FF0000', font=('times new roman', 15, 'bold')).place(x=50, y=370)


root.mainloop()