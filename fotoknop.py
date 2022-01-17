from tkinter import *
import webbrowser



def label2():
    webbrowser.open('https://discord.gg/ptBRjBHM', new=2)


window = Tk()
window.title('PYTROOPS')
window.geometry("600x600")
window.configure(background = "grey")
pic = PhotoImage(file = "discord2.png")


btn2 = Button(window , image = pic , command = label2, height= 50, width=69).grid(row =10 , column = 10)

window.mainloop()