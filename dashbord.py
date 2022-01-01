from tkinter import *

root = Tk()
root.geometry("800x600")

photo = PhotoImage(file="steam banner.png")
imgLabel = Label(root, image=photo)
imgLabel.pack(side=TOP)

label = Label(root, text='This is a label')
label.pack(ipadx=5, ipady=10, side=LEFT)

mainloop()