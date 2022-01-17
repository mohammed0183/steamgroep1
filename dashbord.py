from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import json
import webbrowser

w=Tk()
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


w.overrideredirect(1)



#############progressbar          33333333333333333333333333333
def new_win():
  # w.destroy()

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

        root.destroy()
        new_win()
    def vragen():
        webbrowser.open('https://discord.gg/ptBRjBHM', new=2)


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

        hoofdframe.pack_forget()
        lezenframe.pack()
        imgLabel.pack_forget()
        json_filename = 'steam.json'
        with open(json_filename, 'r') as inside:
            data = json.load(inside)
        text = json.dumps(sorted(data, key=lambda k: int(k['positive_ratings']), reverse = True), indent=2)
        txt = tk.Text(root, font="Times32")
        root.title('Steam')
        txt.pack()
        txt.insert('end', text)


    root = Tk()
    root.title('Steam')
    root.iconbitmap('Steam.ico')
    hoofdframe = LabelFrame(root, text="Steam")
    hoofdframe.pack(ipadx=500,
        ipady=50,
        expand=False,
        side=BOTTOM)

    photo = PhotoImage(file="steam_banner.png")
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

    x6 = Button(hoofdframe, text='Vragen?', font=('italic', 10), fg='white', bg=
    "#5865F2",command=vragen)
    x6.grid(row=9, column=4, pady=10, padx= 46)

    root.geometry("900x500")

    lezenframe = LabelFrame(root, text="")
    lezenframe.pack(pady=20)

    gaterug = Button(lezenframe,text= "Terug naar hoofdmenu", font=('italic', 10), fg='white', bg=
    "Black",command=hoofd)
    gaterug.grid(row=1, column=4)

    mainloop()



def bar():

    l4=Label(w,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)

    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1

    w.destroy()
    new_win()




progress.place(x=-10,y=235)




#############
# frame 333333333333333333333333
#
###########





'''

def rgb(r):
    return "#%02x%02x%02x" % r
#Frame(w,width=432,height=241,bg=rgb((100,100,100))).
'''
a='#249794'
Frame(w,width=427,height=241,bg=a).place(x=0,y=0)  #249794
b1=Button(w,width=10,height=1,text='Get Started',command=bar,border=0,fg=a,bg='white')
b1.place(x=170,y=200)


######## Label

l1=Label(w,text='STEAM',fg='white',bg=a)
lst1=('Calibri (Body)',18,'bold')
l1.config(font=lst1)
l1.place(x=50,y=80)

l2=Label(w,text='INTERFACE',fg='white',bg=a)
lst2=('Calibri (Body)',18)
l2.config(font=lst2)
l2.place(x=155,y=82)

l3=Label(w,text='PROGRAMMED',fg='white',bg=a)
lst3=('Calibri (Body)',13)
l3.config(font=lst3)
l3.place(x=50,y=110)




w.mainloop()


