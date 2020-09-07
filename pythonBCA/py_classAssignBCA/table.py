from tkinter import *

class Table:
  def __init__(self, root):
      # creating table
      for i in range(total_rows):
          for j in range(total_columns):
              self.e = Entry(root, width=20,  bg='white',fg='black',font=('Ariel', 14, 'normal'))
              self.e.grid(row=i, column=j)
              self.e.insert(END, lst[i][j])
              
lst = [('Timings', '8:00-9:00', '9:00-10:00','11:00-12:00', '12:00-1:00', '2:00-3:00','3:00-4:00'),
       ('Monday', 'Python', 'Multemedia','CN', 'MA/GA', 'Python Lab','Python Lab'),
       ('Tuesday', 'Machine Leanring', 'Multimedia','Mobile Lab', 'Mobile Lab', 'CC Lab','CC Lab'),
       ('Wednesday', 'Python', 'CN','Project lab', 'Project Lab', 'Ml Lab','ML Lab'),
       ('Thursday', 'Mobile App', 'Machine Learning','Python lab', 'Python Lab', 'Mobile Lab','Mobile Lab'),
       ('Friday', 'CN', 'Multimedia','Python', 'MA/GA', 'Project','Project'),
       ('Saturday', 'Python', 'Mobile App','Multimedia', 'CN', 'Cloud','-')]

total_rows = len(lst)
total_columns = len(lst[0])

root = Tk()
root.title('5th SEM BCA A & B')
t = Table(root)
root.mainloop()