# importing libraries and modules
import xml.etree.ElementTree as ET
from xml.dom import minidom
from tkinter import *
from tkinter import filedialog

# using file dilogue to open file
getfile = filedialog.askopenfilename()

# parsing the xml file and getting child tag
xmlfile = minidom.parse(getfile)
child = xmlfile.getElementsByTagName('movie')

# importing and reading file from above getfile
tree = ET.parse(getfile)
xmlroot = tree.getroot()

# Creating a display for Tkinter
root = Tk()
root.title('XML MOVIES')
root.geometry('1200x500')
root.configure(background="white")

# function to create table
def tablefunc():
    x = "XML Title : " + xmlroot.attrib['shelf']
    rootname = Label(root, text=x, font=("Helvetica", 12),width = 50, background="white",borderwidth = 2, relief="solid", highlightbackground="blue")
    rootname.place(x = 120,y=80)
    frame = Frame(root,width=1000,height=500,borderwidth=2)
    frame.place(x=40,y=150)
    # creation of the table as the title given
    row = ['Movie Name','Year','IMDB Rating','Description']
    for i in range(0,1):
        for j in range(0, 4):
            e = Entry(frame, width=18,font=('Arial',13,'normal'))
            e.grid(row=i, column=j)
            if(j==3):
                e.configure(width=65)
            e.insert(END,row[j])
    # appending the data from the xml in table
    for i in range(0,len(child)):
        row.clear()
        row.append(child[i].attributes['title'].value)
        row.append(xmlroot[i][2].text)
        row.append(xmlroot[i][4].text)
        row.append(xmlroot[i][5].text)
        for j in range(0, 4):
            e = Entry(frame, width=18,font=('Arial',13,'bold'))
            e.grid(row=i+1, column=j)
            if(j==3):
                e.configure(width=65)
            e.insert(END,row[j])

# Creation of Label and button to load the file saved
label = Label(root,background="silver", text = "Load XML file",font=('Bahnschrift',15))
label.place(x = 70,y=20)
b1 = Button(root,text="Load", font=('Bahnschrift',10),command = lambda:tablefunc(),width = 15)
b1.place(x = 200,y=18)

root.mainloop()