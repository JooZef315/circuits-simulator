from tkinter import *
from sympy import *

window = Tk()
window.title("Circuit 2 - nodel")
cir2 = PhotoImage(file="nodel-digram.png")
cir = Label(window, image=cir2)
cir.pack(padx=1, pady=1, side=LEFT)

V1, V2 ,I_R1 ,I_R2 ,I_R3 = symbols('V1, V2 ,I_R1 ,I_R2 ,I_R3')

LabVs = Label(window , text="Vs", font=("Arial", 10))
LabVs.pack(padx=1, pady=1)
txtVs = Entry(window,width=10)
txtVs.pack(padx=5, pady=1)

LabR1 = Label(window , text="R1", font=("Arial", 10))
LabR1.pack(padx=1, pady=1)
txtR1 = Entry(window,width=10)
txtR1.pack(padx=5, pady=1)

LabR2 = Label(window , text="R2", font=("Arial", 10))
LabR2.pack(padx=1, pady=1)
txtR2 = Entry(window,width=10)
txtR2.pack(padx=5, pady=1)

LabR3 = Label(window , text="R3", font=("Arial", 10))
LabR3.pack(padx=1, pady=1)
txtR3 = Entry(window,width=10)
txtR3.pack(padx=5, pady=1)

LabIo = Label(window , text="Io", font=("Arial", 10))
LabIo.pack(padx=1, pady=1)
txtIo = Entry(window,width=10)
txtIo.pack(padx=5, pady=1)

def clicked():

    Vs = int(txtVs.get())
    V1 = Vs
    R1 = int(txtR1.get())
    R2 = int(txtR2.get())
    R3 = int(txtR3.get())
    Io = int(txtIo.get())

    eqV2 = Eq((V2-V1)/R1 + V2/R2 + V2/R3 , Io)
    resV2 = solve(eqV2, V2)
    resI_R1 = solve((V1-resV2[0])/R1 - I_R1 , I_R1)
    resI_R2 = solve(resV2[0]/R2 - I_R2 , I_R2)
    resI_R3 = solve(resV2[0]/R3 - I_R3 , I_R3)

    LabresV2.configure(text= resV2)
    LabV2.configure(text="V2=")
    LabresI_R1.configure(text= resI_R1)
    LabI_R1.configure(text="  I_R1=")
    LabresI_R2.configure(text= resI_R2)
    LabI_R2.configure(text="  I_R2=")
    LabresI_R3.configure(text= resI_R3)
    LabI_R3.configure(text="  I_R3=")
btn = Button(window, text="calculate", bg="black", fg="white", command=clicked)
btn.pack(padx=1, pady=10)

LabV2 = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabV2.pack(padx=1, pady=1, side=LEFT)
LabresV2 = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabresV2.pack(padx=1, pady=1, side=LEFT)

LabI_R1 = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabI_R1.pack(padx=1, pady=1, side=LEFT)
LabresI_R1 = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabresI_R1.pack(padx=1, pady=1, side=LEFT)

LabI_R2 = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabI_R2.pack(padx=1, pady=1, side=LEFT)
LabresI_R2 = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabresI_R2.pack(padx=1, pady=1, side=LEFT)

LabI_R3 = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabI_R3.pack(padx=1, pady=1, side=LEFT)
LabresI_R3 = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabresI_R3.pack(padx=1, pady=1, side=LEFT)

window.mainloop()
