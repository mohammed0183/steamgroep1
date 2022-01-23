import tkinter
import datetime
import json

from datetime import datetime
from tkinter import *
import tkinter.messagebox as messagebox

def inzenden():
 x = int(e_name.get())
 with open('steam.json') as json_file:
  data = json.load(json_file)
 for i in data:
  if i['appid'] == x:
   print(i['appid'])
   print(i['name'])
   print(i['release_date'])
   print(i['english'])
   print(i['developer'])
   print(i['publisher'])
   print(i['platforms'])
   text =(i['name'])

   txt = tkinter.Text(root, font="Times32")

   txt.pack()
   txt.insert('end', text)
   break



 e_name.delete(0, "end")

root = Tk()
root.geometry('600x300')
root.title('zoeken')
naam = Label(root, text = "Voer de appid in.", font=('bold', 10) )
naam.place(x=20, y=30)
e_name = Entry()
e_name.place(x=150,y=30)
inzenden=Button(root, text='zoeken', font=('italic', 10), fg='white', bg=
"Black",command=inzenden)
inzenden.place(x=20, y=140)
tkinter.mainloop()
