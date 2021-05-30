from tkinter import *

root = Tk()
root.title("giải pt bậc 2")
txta = StringVar()
z = 0


def adding():
    x1 = 0
    a = float(E1.get())
    b = float(E2.get())
    c = float(E3.get())
    z = abs(b**2-4*a*c)
    x1 = (-b+z)/(2*a)
    x2 = (-b+z)/(2*a)
    txta.set(str(x1) + "hoặc" + str(x2))


L1 = Label(root, text="nhập giá trị A,B,C vào Ax^2 + Bx+C = 0")
L1.grid(row=0, column=0, columnspan=2)
LA = Label(root, text="A = ")
LA.grid(row=1, column=0)
LB = Label(root, text="B = ")
LB.grid(row=2, column=0)
LC = Label(root, text="C = ")
LC.grid(row=3, column=0)
E1 = Entry(root)
E1.grid(row=1, column=1)
E2 = Entry(root)
E2.grid(row=2, column=1)
E3 = Entry(root)
E3.grid(row=3, column=1)
L4 = Label(root, text="X = ")
L4.grid(row=5, column=0)
E4 = Entry(root, textvariable=txta)
E4.grid(row=5, column=1)
Button(root, text="Solve", command=lambda: adding()).grid(row=4, column=1)
mainloop()