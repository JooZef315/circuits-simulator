from tkinter import *
from sympy import *

window = Tk()

window.title("Circuit 1 - Mesh")
cir1 = PhotoImage(file="mesh-digram.png")
cir = Label(window, image=cir1)
cir.pack(padx=1, pady=1, side=LEFT)


i1 ,i2 ,i3 = symbols('i1 ,i2 ,i3')

LabR1 = Label(window , text="R1", font=("Arial", 10))
LabR1.pack(padx=1, pady=1)
txtR1 = Entry(window,width=10)
txtR1.pack(padx=5, pady=1)

LabR2 = Label(window , text="R2", font=("Arial", 10))
LabR2.pack(padx=5, pady=1)
txtR2 = Entry(window,width=10)
txtR2.pack(padx=5, pady=1)

LabR3 = Label(window , text="R3", font=("Arial", 10))
LabR3.pack(padx=5, pady=1)
txtR3 = Entry(window,width=10)
txtR3.pack(padx=5, pady=1)

LabR13 = Label(window , text="R13", font=("Arial", 10))
LabR13.pack(padx=5, pady=1)
txtR13 = Entry(window,width=10)
txtR13.pack(padx=5, pady=1)

LabR23 = Label(window , text="R23", font=("Arial", 10))
LabR23.pack(padx=1, pady=1)
txtR23 = Entry(window,width=10)
txtR23.pack(padx=5, pady=1)

LabV1 = Label(window , text="V1", font=("Arial", 10))
LabV1.pack(padx=1, pady=1)
txtV1 = Entry(window,width=10)
txtV1.pack(padx=5, pady=1)

LabV12 = Label(window , text="V12", font=("Arial", 10))
LabV12.pack(padx=1, pady=1)
txtV12 = Entry(window,width=10)
txtV12.pack(padx=5, pady=1)

LabV2 = Label(window , text="V2", font=("Arial", 10))
LabV2.pack(padx=1, pady=1)
txtV2 = Entry(window,width=10)
txtV2.pack(padx=5, pady=1)


def clicked():
    R1 = int(txtR1.get())
    R13 = int(txtR13.get())
    R2 = int(txtR2.get())
    R23 = int(txtR23.get())
    R3 = int(txtR3.get())
    V1 = int(txtV1.get())
    V12 = int(txtV1.get())
    V2 = int(txtV2.get())

    mesh1= Eq(i1*(R1+R13) - i3*R13, (V1-V12))
    mesh2= Eq(i2*(R2+R23) - i3*R23, (V2+V12))
    mesh3= Eq(-i1*R13 - i2*R23 + i3*(R3+R13+R23),0)

    res = solve((mesh1,mesh2, mesh3), (i1 , i2 , i3))


    Labresi1.configure(text= res[i1])
    Labi1.configure(text="i1=")
    Labresi2.configure(text= res[i2])
    Labi2.configure(text="  i2=")
    Labresi3.configure(text= res[i3])
    Labi3.configure(text="  i3=")
btn = Button(window, text="calculate", bg="black", fg="white", command=clicked)
btn.pack(padx=1, pady=10)

Labi1 = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
Labi1.pack(padx=1, pady=1, side=LEFT)
Labresi1 = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
Labresi1.pack(padx=1, pady=1, side=LEFT)

Labi2 = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
Labi2.pack(padx=1, pady=1, side=LEFT)
Labresi2 = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
Labresi2.pack(padx=1, pady=1, side=LEFT)

Labi3 = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
Labi3.pack(padx=1, pady=1, side=LEFT)
Labresi3 = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
Labresi3.pack(padx=1, pady=1, side=LEFT)

window.mainloop()
