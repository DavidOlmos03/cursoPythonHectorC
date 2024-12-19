from tkinter import *

root = Tk()

# First input
label = Label(root, text="Name: ")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="normal")

# Second input
label2 = Label(root, text="Password: ")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1,padx=5, pady=5)
entry2.config(justify="center", show="*")

root.mainloop()

