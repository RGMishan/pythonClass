import tkinter as tk
import re
import random
from tkinter import Tk, Label, Entry, ttk, Button, scrolledtext, Text

window = Tk()
window.geometry("850x450")
names = open("names.txt").read().splitlines()
startingwith = Label(window, text="Starting with")
startingwith.grid(row=0, column=0, padx=10, pady=10)
window["bg"] = "silver"

n = tk.StringVar()
alpha = ttk.Combobox(window, width=20, textvariable=n)
alpha['values'] = (
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
'Y', 'Z')
alpha.grid(column=1, row=0, padx=20)

def load_list():
    print(type(names))
    for name in names:
        if re.search(r'^[mM]', name):
            startingwithM.insert(tk.END, (name+"\n"))
        if re.search(r'^[pP]', name):
            startingwithP.insert(tk.END, (name+"\n"))
        if re.search(r'^[nN]', name):
            startingwithN.insert(tk.END, (name+"\n"))

ans = Label(window, text="Name", font=('Times New Roman', 16))
ans.grid(row=1, column=2, sticky="w", padx=10)

def click1():
    fa = alpha.get()
    while True:
        rn = random.choice(names)
        if re.search(r'^{}'.format(fa), rn):
            print(rn)
            ans['text'] = rn
            break

generate = Button(window, text="Generate", command=click1)
generate.grid(column=2, row=0, padx=10, sticky="w")

startingwithans = Label(window, text="Suggested Name Starting with & letter : ")
startingwithans.grid(row=1, columnspan=2, padx=0, pady=10)

startingwithM = Text(window, width=30, height=20)
startingwithM.grid(row=2, columnspan=2, padx=20, pady=20)
startingwithM.insert(tk.END, "       Starting with M     \n\n")

startingwithP = Text(window, width=30, height=20)
startingwithP.grid(row=2, column=2, padx=20, pady=20)
startingwithP.insert(tk.END, "       Starting with P     \n\n")

startingwithN = Text(window, width=30, height=20)
startingwithN.grid(row=2, column=10, padx=20, pady=20)
startingwithN.insert(tk.END, "       Starting with N     \n\n")

load_list()
window.mainloop()
