from tkinter import *

root = Tk()
root.title("Hello World")
root.resizable(1,1)
root.iconbitmap("@hola.xbm")


# Creating a frame
root.config(cursor="pirate", bg="blue", bd=25, relief="sunken")
frame = Frame(root, width=480, height=320)
frame.pack(fill="both", expand=1)
frame.config(cursor="pirate", bg="lightblue", bd=25, relief="sunken")

root.mainloop()
