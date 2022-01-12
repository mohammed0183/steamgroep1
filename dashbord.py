from tkinter import *
from tkinter import messagebox
import tkinter as tk
import json

splash_root = Tk()
splash_root.title("Welkom")
splash_root.geometry('300x200+650+250')

splash_label = Label(splash_root, text="Welkom bij Steam controller", font=("Helvetica", 16))
splash_label.pack(pady=20)



def main_window():
    splash_root.destroy()
    root = Tk()
    root.geometry("1000x800")
    root.title("Steam Dashbord")
    root.iconbitmap("Steam_icon.ico")


    photo = PhotoImage(file="steam_banner.png")
    imgLabel = Label(root, image=photo)
    imgLabel.pack(side=TOP)
    label = Label(root, text='')
    label.pack(ipadx=5, ipady=10, side=LEFT)

    def lezen():
        json_filename = 'steam.json'
        with open(json_filename, 'r') as inside:
            data = json.load(inside)
        text = json.dumps(sorted(data, key=lambda k: int(k['appid']), reverse = False), indent=2)

        root = tk.Tk()

        txt = tk.Text(root, font="Times32")
        root.title('Steam')
        txt.pack()
        txt.insert('end', text)


    def fun():
        funn = Tk()
        funn.geometry("1000x800")
        root.quit

    def x1():
        json_filename = 'steam.json'
        with open(json_filename, 'r') as inside:
            data = json.load(inside)

        x =  json.dumps(sorted(data, key=lambda k: int(k['average_playtime']), reverse = True), indent=2)
        root = tk.Tk()

        txt = tk.Text(root, font="Times32")
        root.title('Steam')
        txt.pack()
        txt.insert('end', x)

    def x2():
        messagebox.showinfo("Vrienden", "Red Button clicked")
    def x3():
        messagebox.showinfo("Mijn planning", "Red Button clicked")
    def x5():
        json_filename = 'steam.json'
        with open(json_filename, 'r') as inside:
            data = json.load(inside)

        x =  json.dumps(sorted(data, key=lambda k: int(k['positive_ratings']), reverse = True), indent=2)
        root = tk.Tk()

        txt = tk.Text(root, font="Times32")
        root.title('Steam')
        txt.pack()
        txt.insert('end', x)

    lezenn = Button(root, text='lezen', font=('italic', 10), fg='white', bg=
    "Black",command=lezen)
    lezenn.place(x=450, y=300)
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

splash_root.after(3000, main_window)

mainloop()