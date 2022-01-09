import tkinter as tk
import json

json_filename = 'steam.json'
with open(json_filename, 'r') as inside:
   data = json.load(inside)
text = json.dumps(data, indent=2)

root = tk.Tk()

txt = tk.Text(root, font="Times32")
root.title('Steam')
txt.pack()
txt.insert('end', text)

root.mainloop()