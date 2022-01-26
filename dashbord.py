import sys
import os
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import json
import webbrowser
import tkinter
import requests
import tkinter.messagebox as messagebox
from tkinter import *

import time





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



def new_win():
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


        tehapi = 'C808AFD79C4F1A523682FF587DFC4481'
        tehuid = '76561198992221003'
        tehuri = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=' + tehapi + '&steamid=' + tehuid + '&relationship=friend'

        friendlist = requests.get(tehuri).json()['friendslist']['friends']

        steamidlist = []

        for i in range(len(friendlist)):
            steamidlist.append(friendlist[i]['steamid'])

        joinedsids = ','.join(steamidlist)

        def printFriendInfo(ids):
            useruri = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + tehapi + '&steamids=' + ids
            userget = requests.get(useruri).json()['response']
            for i in range(len(userget['players'])):
                # print(userget['players'][i])

                sname = str(userget['players'][i]['personaname'])
                text=sname
                text.replace(" ", "")
                print(text)
                txt = tkinter.Text(root, font="Times10")

                txt.pack()
                txt.insert('end', text)

                messagebox.showinfo('Vrienden' , sname )



        def printOnlineFriends(ids):
            useruri = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + tehapi + '&steamids=' + ids
            userget = requests.get(useruri).json()['response']

            onlineDict = {}
            global maxnamelen
            maxnamelen = 0
            for i in range(len(userget['players'])):
                tonli = userget['players'][i]['personastate']
                if tonli == 1:
                    if 'gameextrainfo' in userget['players'][i]:
                        sname = userget['players'][i]['personaname']
                        onlineDict.update({sname: sgame})
                        if len(sname) > maxnamelen:
                            maxnamelen = int(len(sname))

                else:

                    continue

            sortDict = sorted(onlineDict.items(), key=lambda z: z[1])
            for i in sorted(onlineDict.keys()):

                tspaces = ""
                lennamediff = (maxnamelen - len(i)) + 2
                for x in range(lennamediff):
                    tspaces += ' '
                print(i + tspaces, "speelt nu " + onlineDict[i])
                print(i + tspaces)
                if i + tspaces + onlineDict[i] == ' ':
                    text = ('al je vrienden zijn offline')
                else:
                    text = (i + tspaces, "speelt nu " + onlineDict[i])


        printOnlineFriends(joinedsids)
        printFriendInfo(joinedsids)
    def modus():
        json_filename = 'steam.json'
        with open(json_filename, 'r') as inside:
             data = json.load(inside)



        # Using list comprehension
        # Get values of particular key in list of dictionaries
        res = [ sub['appid'] for sub in data ]

        # printing result
        def median(res):
            res.sort() # lst word gesorteerd
            lengte = len(res)
            if len(res) % 2 == 0: # kijken of de lijst even is zo ja , dan moeten we 2 medianen gebruiken
                first_median = res[lengte // 2] # Eerste median
                second_median = res[lengte // 2 - 1] # Tweede median
                mediaan = (first_median + second_median) / 2 # hier heb je het gemiddelde van de mediaanen
            else:
                mediaan = res[lengte // 2] #dit is wanneer een lijst oneven is, dan is het gewoon gedeelt door 2
            return float(mediaan)
        messagebox.showinfo('Mediaan' , 'De mediaan van appid is '+ str(median(res)) )


    def x1():
        hoofdframe.pack_forget()
        lezenframe.pack()
        imgLabel.pack_forget()
        json_filename = 'steam.json'
        with open(json_filename, 'r') as inside:
            data = json.load(inside)
        text = json.dumps(sorted(data, key=lambda k: int(k['average_playtime']), reverse = True), indent=2)
        txt = tk.Text(root, font="Times32")
        root.title('Steam')
        txt.pack()
        txt.insert('end', text)

    def x2():

        tehapi = 'C808AFD79C4F1A523682FF587DFC4481'
        tehuid = '76561198992221003'
        tehuri = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=' + tehapi + '&steamid=' + tehuid + '&relationship=friend'

        friendlist = requests.get(tehuri).json()['friendslist']['friends']

        steamidlist = []

        for i in range(len(friendlist)):
            steamidlist.append(friendlist[i]['steamid'])

        joinedsids = ','.join(steamidlist)


        def printOnlineFriends(ids):
            useruri = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + tehapi + '&steamids=' + ids
            userget = requests.get(useruri).json()['response']


            onlineDict = {}
            global maxnamelen
            maxnamelen = 0
            for i in range(len(userget['players'])):
                tonli = userget['players'][i]['personastate']
                if tonli == 1:
                    if 'gameextrainfo' in userget['players'][i]:
                        sname = userget['players'][i]['personaname']
                        sgame = userget['players'][i]['gameextrainfo']
                        onlineDict.update({sname: sgame})
                        if len(sname) > maxnamelen:
                            maxnamelen = int(len(sname))

                        continue
            if maxnamelen == 0:
                messagebox.showinfo('Vrienden', 'Er zijn geen vrienden online')

            sortDict = sorted(onlineDict.items(), key=lambda z: z[1])
            for i in sorted(onlineDict.keys()):

                tspaces = ""
                lennamediff = (maxnamelen - len(i)) + 2
                for x in range(lennamediff):
                    tspaces += ' '

                print(i + tspaces, "speelt nu " + onlineDict[i])
                print(i + tspaces)

                if i + tspaces + onlineDict[i]:
                    text = (i + tspaces, "speelt nu " + onlineDict[i])
                    hoofdframe.pack_forget()
                    lezenframe.pack()
                    imgLabel.pack_forget()

                    txt = tkinter.Text(root, font="Times32")

                    txt.pack()
                    txt.insert('end', text)




        printOnlineFriends(joinedsids)


    def x3():
        messagebox.showinfo("Mijn planning", "Red Button clicked")
    def x6():
        webbrowser.open('https://docdro.id/SILq3fp', new=2)
    def zoeken():
        hoofdframe.pack_forget()
        lezenframe.pack()
        imgLabel.pack_forget()

        def inzenden():
            x = int(e_name.get())

            json_filename = 'steam.json'
            with open(json_filename, 'r') as inside:
                data = json.load(inside)
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

            txt = tk.Text(root, font="Times32")
            root.title('Steam')
            txt.pack()
            txt.insert('end', text)
        naam = Label(root, text = "Voer de appid in.", font=('bold', 10) )
        naam.place(x=20, y=20)
        e_name = Entry()
        e_name.place(x=150,y=20)
        inzenden=Button(root, text='zoeken', font=('italic', 10), fg='white', bg=
        "Black",command=inzenden)
        inzenden.place(x=150, y=40)
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


    style = ttk.Style()
    style.theme_create('appstyle', parent='alt',
                       settings={
                           'TLabelframe': {
                               'configure': {
                                   'background': '#1b2838'
                               }
                           },
                           'TLabelframe.Label': {
                               'configure': {
                                    'background': '#1b2838'
                               }
                           }
                       }
                       )
    style.theme_use('appstyle')
    root.title('Steam')
    root.configure(bg='#1b2838')
    hoofdframe = ttk.LabelFrame(root)
    hoofdframe.pack(ipadx=550,
        ipady=50,
        expand=False,
        side=BOTTOM)

    photo = PhotoImage(file = "./img/steam_banner.png")
    imgLabel = Label(root, image=photo)
    imgLabel.pack(side=TOP, pady=10)


    pic = PhotoImage(file="./img/discord2.png")


    lezenn = Button(hoofdframe, text='Alle games', font=('italic', 12), fg='white', bg=
    "Black",command=lezen)
    lezenn.grid(row=5, column=4, pady=50)

    inzenden = Button(hoofdframe, text='Mijn vrienden', font=('italic', 10), fg='white', bg=
    "Black",command=fun )
    inzenden.grid(row=7, column=2, pady=10, padx= 46)

    modus = Button(hoofdframe, text='Mediaan van appid', font=('italic', 10), fg='white', bg=
    "Black",command=modus  )
    modus.grid(row=9, column=2)



    x1 = Button(hoofdframe, text='Meest gespeeld game', font=('italic', 10), fg='white', bg=
    "Black",command=x1)
    x1.grid(row=7, column=3, pady=10, padx= 46)

    x2 = Button(hoofdframe, text='Online Vrienden', font=('italic', 10), fg='white', bg=
    "Black",command=x2)
    x2.grid(row=7, column=4, pady=10, padx= 46)

    x3 = Button(hoofdframe, text='Mijn planning', font=('italic', 10), fg='white', bg=
    "Black",command=x3)
    x3.grid(row=7, column=5, pady=10, padx= 46)

    x5 = Button(hoofdframe, text='Aanbevolen games', font=('italic', 10), fg='white', bg=
    "Black",command=x5)
    x5.grid(row=7, column=6, pady=10, padx= 46)


    btn2 = Button(hoofdframe, image=pic, command=vragen, height=50, width=69)
    btn2.grid(row=9, column=4, pady=10, padx= 46)


    x6 = Button(hoofdframe, text='Stakeholder', font=('italic', 10), fg='white', bg=
    "Black", command=x6)
    x6.grid(row=9, column=5)


    x6 = Button(hoofdframe, text='Customer Journey', font=('italic', 10), fg='white', bg=
    "Black", command=x6)
    x6.grid(row=9, column=6)

    x7 = Button(hoofdframe, text='Zoeken naar een game', font=('italic', 10), fg='white', bg=
    "Black", command=zoeken)
    x7.grid(row=9, column=3)

    root.geometry("980x600+300+50")

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


