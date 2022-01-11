from tkinter import *
from tkinter import messagebox
import tkinter as tk
import json


def lezen():
    hoofdframe.pack_forget()
    lezenframe.pack()
    imgLabel.pack_forget()
    json_filename = 'steam.json'
    with open(json_filename, 'r') as inside:
        data = json.load(inside)
    text = json.dumps(data, indent=2)
    txt = tk.Text(root, font="Times32")
    root.title('Steam')
    txt.pack()
    txt.insert('end', text)

def hoofd():
    lezenframe.pack_forget()
    hoofdframe.pack()
    imgLabel.pack()


def fun():
    funn = Tk()
    funn.geometry("1000x800")
    root.quit

def x1():
    messagebox.showinfo("Meest gespeeld", "Red Button clicked")
def x2():
    messagebox.showinfo("Vrienden", "Red Button clicked")
def x3():
    messagebox.showinfo("Mijn planning", "Red Button clicked")
def x5():
    messagebox.showinfo("Aanbevelingen", "Red Button clicked")

root = Tk()
hoofdframe = LabelFrame(root, text="Steam")
hoofdframe.pack(ipadx=500,
    ipady=50,
    expand=False,
    side=BOTTOM)

photo = PhotoImage(file="steam banner.png")
imgLabel = Label(root, image=photo)
imgLabel.pack(side=TOP, pady=10)


lezenn = Button(hoofdframe, text='Lezen', font=('italic', 10), fg='white', bg=
"Black",command=lezen)
lezenn.grid(row=5, column=4, pady=50)

inzenden = Button(hoofdframe, text='Mijn vrienden', font=('italic', 10), fg='white', bg=
"Black",command=fun )
inzenden.grid(row=7, column=2, pady=10, padx= 46)

x1 = Button(hoofdframe, text='Meest gespeeld', font=('italic', 10), fg='white', bg=
"Black",command=x1)
x1.grid(row=7, column=3, pady=10, padx= 46)

x2 = Button(hoofdframe, text='Vrienden', font=('italic', 10), fg='white', bg=
"Black",command=x2)
x2.grid(row=7, column=4, pady=10, padx= 46)

x3 = Button(hoofdframe, text='Mijn planning', font=('italic', 10), fg='white', bg=
"Black",command=x3)
x3.grid(row=7, column=5, pady=10, padx= 46)

x5 = Button(hoofdframe, text='Aanbevelingen', font=('italic', 10), fg='white', bg=
"Black",command=x5)
x5.grid(row=7, column=6, pady=10, padx= 46)

root.geometry("900x500")

lezenframe = LabelFrame(root, text="")
lezenframe.pack(pady=20)

gaterug = Button(lezenframe,text= "Terug naar hoofdmenu", font=('italic', 10), fg='white', bg=
"Black",command=hoofd)
gaterug.grid(row=1, column=4)


mainloop()