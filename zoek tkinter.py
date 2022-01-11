import tkinter
import datetime
import json

from datetime import datetime
from tkinter import *
import tkinter.messagebox as messagebox
tijd=datetime.now()
print(tijd)
def inzenden():
 x = e_name.get()
 m = int(x)

 with open('steam.json') as json_file:
  data = json.load(json_file)
 if m == '':
  messagebox.showinfo('Zoek status', 'Het veld Appid moet verplicht worden ingevuld.')


 else:
  for i in data:
   if i['appid'] == int(m):
    print(i['appid'])
    print(i['name'])
    print(i['release_date'])
    print(i['english'])
    print(i['developer'])
    print(i['publisher'])
    print(i['platforms'])

   break
 e_name.delete(0, "end")




root = Tk()
root.geometry('600x300');
root.title('zoeken');
naam = Label(root, text = "Voer de appid in.", font=('bold', 10) )
naam.place(x=20, y=30)
e_name = Entry()
e_name.place(x=150,y=30)
inzenden=Button(root, text='zoeken', font=('italic', 10), fg='white', bg=
"Black",command=inzenden)
inzenden.place(x=20, y=140)
tkinter.mainloop()