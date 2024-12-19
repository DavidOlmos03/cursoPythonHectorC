from tkinter import *

root = Tk()
""""
# Dynamic variables
text = StringVar()
text.set("New text")

Label(root, text="Hello World!!").pack(anchor="nw")
label = Label(root, text="¡Other tag!")
label.pack(anchor="center")
Label(root, text="¡Última etiqueta!").pack(anchor="se")

label.config(bg="green", fg="blue", font=("Verdana",24))
label.config(textvariable=text)
"""

image = PhotoImage(file="imagen.gif")
Label(root, image=image, bd=0).pack()

root.mainloop()
