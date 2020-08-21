from tkinter import *

from tkinter import ttk

 

class View(ttk.Frame):

 

   def __init__(self, *args, **kwargs):

       ttk.Frame.__init__(self, *args, **kwargs)

 

       global years, money, interest, entry, entry1, entry2

 

       years = StringVar()

       money = StringVar()

       interest = StringVar()

 

 

       search = ttk.Button(self, text="Calc", command=self.new_window)

       search.grid(column=0, row=0, sticky=W)

 

       search = ttk.Button(self, text='Clear', command=self.launchf)

       search.grid(column=1, row=0, sticky=W)

 

       entry = ttk.Entry(self, width=6, textvariable=years)

       entry.grid(column=1, row=1, sticky=W)

       entry1 = ttk.Entry(self, width=6, textvariable=money)

       entry1.grid(column=1, row=2, sticky=W)

       entry2 = ttk.Entry(self, width=6, textvariable=interest)

       entry2.grid(column=1, row=3, sticky=W)

 

       ttk.Label(self, text='Years: ').grid(column=0, row=1, sticky=W)

       ttk.Label(self, text='Amount: ').grid(column=0, row=2, sticky=W)

       ttk.Label(self, text='Intrest Rate: ').grid(column=0, row=3, sticky=W)

 

   def launchf(self):

       entry.delete(0, END)

       entry1.delete(0, END)

       entry2.delete(0, END)

 

   def new_window(self):

       window = Toplevel(self)

 

       try:

           y = float(years.get())

           m = float(money.get())

           i = float(interest.get())

           ro = 1

           col = 0

           col1 = 1

           col2 = 2

           col3 = 4

 

           while y > 0:

               val = (i/100)*m

               m+= val

               rval = ttk.Label(window, text= round(val, 2)).grid(column=col, row=ro, sticky=N)

               mval = ttk.Label(window, text=round(m, 2)).grid(column=col2, row=ro, sticky=NE)

               midval = ttk.Label(window, text='-').grid(column=col1, row=ro, sticky=NW)

               ro+=1

               y-=1

               if ro >= 31:

                   col += 7

                   col1 += 7

                   col2 += 7

                   col3 += 7

                   ro = 1

 

       except ValueError:

            pass

 

name = '__main__'

if name == '__main__':

   root = Tk()

   view = View(root)

   view.pack(side='top', fill='both', expand=True)

   root.title('Compounding Intrest Calculator')

   root.mainloop()