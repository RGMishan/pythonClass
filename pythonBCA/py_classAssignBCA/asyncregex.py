import tkinter as tk
from tkinter import ttk
from tkinter import *
import re

root = Tk()
root.geometry('1550x650')
root.configure(background='#C0C0C0')
root.title('Mishan 1841030')

def btnClickFunction():
    with open("paragraphRegex.txt", "r") as f:
      Label(root, text=f.read()).place(x=10, y=50)
      
      #regex1 copunting paragraph
      paragraph = re.split(r'[\n]', f)
      para = len(paragraph)

      #regex2 coutnting number
      words = re.split(r'[ \n,?.!]', f)

      countnum = 0
      for w in range(len(words)):
          if re.search(r'[0-9]', words[w]):
             countnum += 1
             print(words[w])
      print("\nWords having numerals are", countnum)

      #regex3 end with e
      countE = 0
      for i in range(len(words)):
          if re.search(r'e$', words[i]):
            countE += 1
            print(words[i])
      print("\nWords which end with letter 'e' are", countE )

      #number 1 counting paragraph
      Label(root, text=para, bg='#FF0000', font=('times new roman', 15, 'bold')).place(x=50, y=230)
      #number 2 counting number
      Label(root, text=countnum, bg='#FF0000', font=('times new roman', 15, 'bold')).place(x=50, y=300)
      #number 3 end with e
      Label(root, text=countE, bg='#FF0000', font=('times new roman', 15, 'bold')).place(x=50, y=370)



Label(root, text='REGEX OPERATION', bg='#FF0000', font=('times new roman', 15, 'bold')).place(x=50, y=10)

#label1 = Label(root, text='Total Paragraph', bg='#FF0000', font=('times new roman', 15, 'bold')).place(x=50, y=230)
#label2 = Label(root, text='End With E', bg='#FF0000', font=('times new roman', 15, 'bold')).place(x=50, y=300)
#label3 = Label(root, text='Capital Letter', bg='#FF0000', font=('times new roman', 15, 'bold')).place(x=50, y=370)

Button(root, text='CLICK ME', bg='#228B22', height=1, width=14, font=('MV Boli', 16, 'normal'),command=btnClickFunction).place(x=180, y=160)

root.mainloop()
