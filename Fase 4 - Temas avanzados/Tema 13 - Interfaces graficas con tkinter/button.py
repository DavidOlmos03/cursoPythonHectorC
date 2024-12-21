from tkinter import  *

# Functions 
def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()

def restar():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()

def multiplicar():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()

def dividir():
    r.set(float(n1.get()) / float(n2.get()))
    borrar()

def borrar():
    n1.set("")
    n2.set("")

# Aplication 
root = Tk()
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

lista = [n1, n2, r]

for i in range(3):
    if i != 2:
        Label(root, text=f"Number {i+1}").pack()
    else:
         Label(root, text="Result", state="disabled").pack()

    Entry(root, justify="center", textvariable = lista[i]).pack()


Label(root, text=" ").pack()
Button(root, text="sumar", command=sumar).pack(side="left")

Button(root, text="restar", command=restar).pack(side="left")

Button(root, text="multiplicar", command=multiplicar).pack(side="left")

Button(root, text="dividir", command=dividir).pack(side="left")

root.mainloop()
