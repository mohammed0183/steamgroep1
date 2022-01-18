from tkinter import *
import webbrowser



def label2():
    webbrowser.open('https://discord.gg/ptBRjBHM', new=2)


window = Tk()
window.title('PYTROOPS')
window.geometry("600x600")
hoofdframe = LabelFrame(window, text="Steam")
hoofdframe.pack(ipadx=500,
                ipady=50,
                expand=True,)

window.configure(background = "grey")
pic = PhotoImage(file = "discord2.png")


btn2 = Button(hoofdframe , image = pic , command = label2, height= 50, width=69)
btn2.pack(side=BOTTOM)

window.mainloop()