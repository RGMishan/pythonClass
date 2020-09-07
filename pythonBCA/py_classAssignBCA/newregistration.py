import tkinter as tk
from tkinter import ttk
from tkinter import *
import smtplib

# this is a function which returns the selected combo box item
root = Tk()
root.geometry('400x450')
root.configure()
root.title('Student Details')

# This is the section of code which creates the main window
root.geometry('845x561')
root.configure()
root.title('')

# This is the section of code which creates the a label
Label(root, text='Name').place(x=30, y=50)


# This is the section of code which creates the a label
Label(root, text='Date of Birth').place(x=20, y=95)

# This is the section of code which creates the a label
Label(root, text='Email').place(x=22, y=157)

# This is the section of code which creates the a label
Label(root, text='Phone').place(x=23, y=219)

# This is the section of code which creates a combo box
prefix = ttk.Combobox(root, values=['Mr.', 'Mrs.', 'Ms.', 'Dr'], width=4)
prefix.place(x=306, y=44)
prefix.current(1)

# This is the section of code which creates a text input box
Namet = Entry(root)
Namet.place(x=375, y=44)

# This is the section of code which creates a spin box
Day = Spinbox(root, from_=1, to=31, width=3)
Day.place(x=306, y=90)

# This is the section of code which creates a combo box
Month = ttk.Combobox(root,
                     values=['January', 'February', 'March', 'April', 'May', 'June', 'July ', 'August', 'September',
                             'October', 'November', 'December'], width=8)
Month.place(x=362, y=90)
Month.current(0)

# This is the section of code which creates a combo box
year = ttk.Combobox(root,
                    values=['2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010',
                            '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001', '2000', '1999',
                            '1998', '1997', '1996', '1995'], width=4)
year.place(x=462, y=90)
year.current(0)

# This is the section of code which creates a text input box
email = Entry(root, width=35)
email.place(x=307, y=152)

# This is the section of code which creates a combo box
pre = ttk.Combobox(root, values=['+91', '+1', '+80', '+92', '+126'], width=3)
pre.place(x=307, y=215)
pre.current(0)

# This is the section of code which creates a text input box

phone = Entry(root)
phone.place(x=375, y=215)

# This is the section of code which creates the a label
label1 = Label(root, text='Registered Information', width=80)

label1.place(x=100, y=399)

#mailing


def btnClickFunction():
    x = prefix.get()
    name = Namet.get()
    namef = x + " " + name

    d = Day.get()
    m = Month.get()
    mo = Month.current()
    y = int(year.get())

    ''''''

    e = email.get()

    ''''''
    pr = pre.get()
    ''''''

    ph = phone.get()
    ''''''
    c = str(ph)
    b = ph[6:10]
    yr = str(y)
    ye = yr[2:4]
    dob = str(0) + str(d) + "-" + str(0) + str(mo + 1) + "-" + ye

    regno = str(0) + str(d) + str(0) + str(mo + 1) + str(ye) + "-" + b
    label1.configure(text=regno)

    def mailSender(dest, name):      
        sender = "regmimishan@gmail.com"
        to = dest
        subject = "Registration Successful"
        headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (sender, to, subject)  
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('regmimishan@gmail.com','gmailpassword1234')
        message = headers + "Hi " + name + ", thank you for registering with us!"
        s.sendmail('regmimishan@gmail.com', dest, message)
        s.quit()

    mailSender(e, namef)

    try:
        if y == 1995:

            if mo > 2:
                try:
                    b = e.split('@')
                    if b[1] == "gmail.com" or b[1] == "hotmail.com" or b[1] == "outlook.com":
                        try:
                            if pr == '+91':
                                try:
                                    int(ph)
                                    if len(ph) == 10:
                                        label1.configure(
                                            text="Hi " + namef + ", thank you for your interest and registration. You are successfully\nregistered for the event. We used your DOB " + dob + " and\n" + ph + " to generate registration ID. Your registration ID is " + regno + ". Soon\nevent details will be shared through your E-mail: " + e + ".")
                                    else:
                                        throw(ValueError)
                                except:
                                    label1.configure(
                                        text="Wrong Value (Either you've entered more than 10 digits or entered an Alphabet")
                            else:
                                throw(ValueError)
                        except:
                            label1.configure(text="Sorry Our Services are limited to India as of now.")

                    else:
                        throw(ValueError)
                except:
                    label1.configure(text="Sorry, your mail server is not supported.")
            else:
                throw(ValueError)




        elif y == 2005:

            if mo < 2:
                try:

                    b = e.split('@')
                    if b[1] == "gmail.com" or b[1] == "hotmail.com" or b[1] == "outlook.com":
                        try:

                            if pr == '+91':
                                try:
                                    ph = int(ph)
                                    if len(ph) == 10:
                                        label1.configure(
                                            text="Hi " + namef + ", thank you for your interest and registration. You are successfully\nregistered for the event. We used your DOB " + dob + " and\n" + ph + " to generate registration ID. Your registration ID is " + regno + ". Soon\nevent details will be shared through your E-mail: " + e + ".")
                                    else:
                                        throw(ValueError)
                                except:
                                    label1.configure(
                                        text="Wrong Value (Either you've entered more than 10 digits or entered an Alphabet")
                            else:
                                throw(ValueError)
                        except:
                            label1.configure(text="Sorry Our Services are limited to India as of now.")

                    else:
                        throw(ValueError)
                except:
                    label1.configure(text="Sorry, your mail server is not supported.")
            else:
                throw(ValueError)

        elif y > 1995 and y < 2005:

            try:

                b = e.split('@')
                if b[1] == "gmail.com" or b[1] == "hotmail.com" or b[1] == "outlook.com":
                    try:

                        if pr == '+91':
                            try:
                                int(ph)
                                if len(ph) == 10:
                                    label1.configure(
                                        text="Hi " + namef + ", thank you for your interest and registration. You are successfully\nregistered for the event. We used your DOB " + dob + " and\n" + ph + " to generate registration ID. Your registration ID is " + regno + ". Soon\nevent details will be shared through your E-mail: " + e + ".")
                                else:
                                    throw(ValueError)
                            except:
                                label1.configure(
                                    text="Wrong Value (Either you've entered more than 10 digits or entered an Alphabet")
                        else:
                            throw(ValueError)
                    except:
                        label1.configure(text="Sorry Our Services are limited to India as of now.")

                else:
                    throw(ValueError)
            except:
                label1.configure(text="Sorry, your mail server is not supported.")

        else:
            throw(ValueError)
    except:
        label1.configure(text="Sorry, you don't qualify the age criteria")

    print('clicked')


# This is the section of code which creates a button
Button(root, text='Submit',  height=2, width=20,
      command=btnClickFunction).place(x=166, y=299)

root.mainloop()