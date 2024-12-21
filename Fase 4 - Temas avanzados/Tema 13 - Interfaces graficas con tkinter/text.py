from tkinter import  *

root = Tk()

text = Text(root)
text.pack()
text.config(width=30, height=10, font=("Consolas", 12), padx=15, pady=15, selectbackground="blue")

root.mainloop()
