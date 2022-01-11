from tkinter import *
from tkinter import messagebox
import tkinter as tk
import json



root = Tk()
root.geometry("1000x800")


photo = PhotoImage(file="steam banner.png")
imgLabel = Label(root, image=photo)
imgLabel.pack(side=TOP)

label = Label(root, text='')
label.pack(ipadx=5, ipady=10, side=LEFT)
def lezen():
    json_filename = 'steam.json'
    with open(json_filename, 'r') as inside:
        data = json.load(inside)
    text = json.dumps(data, indent=2)
    root = tk.Tk()


    txt = tk.Text(root, font="Times32")
    root.title('Steam')
    txt.pack()
    txt.insert('end', text)



def submit():
    import json


    with open('steam.json') as json_file:
        data = json.load(json_file)
        root = tk.Tk()

        txt = tk.Text(root, font="Times32")
        root.title('Steam')
        x = input.get()


    for i in data:
        if i['appid'] == x:
            print(i['appid'])
            print(i['name'])
            print(i['release_date'])
            print(i['english'])
            print(i['developer'])
            print(i['publisher'])
            print(i['platforms'])

            txt.pack()
            txt.insert(END,i)




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



lezenn = Button(root, text='Alle Games', font=('italic', 10), fg='white', bg=
"Black",command=lezen)
lezenn.place(x=450, y=300)

input = Entry(root,  font=('italic', 10), fg='white', bg='grey')
input.place(x=420, y=350)

sub_btn=tk.Button(root,text = 'Submit', command = submit)
sub_btn.place(x=465, y=375)

inzenden = Button(root, text='Mijn vrienden', font=('italic', 10), fg='white', bg=
"Black",command=fun )
inzenden.place(x=150, y=500)



x1 = Button(root, text='Meest gespeeld', font=('italic', 10), fg='white', bg=
"Black",command=x1)
x1.place(x=300, y=500)

x2 = Button(root, text='Vrienden', font=('italic', 10), fg='white', bg=
"Black",command=x2)
x2.place(x=450, y=500)

x3 = Button(root, text='Mijn planning', font=('italic', 10), fg='white', bg=
"Black",command=x3)
x3.place(x=600, y=500)

x5 = Button(root, text='Aanbevelingen', font=('italic', 10), fg='white', bg=
"Black",command=x5)
x5.place(x=750, y=500)


mainloop()