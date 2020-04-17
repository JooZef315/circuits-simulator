from tkinter import *
from sympy import *
from tkinter import messagebox

window = Tk()
window.title("Circuit 3 - RCgrid")
cir3 = PhotoImage(file="RCgrid.PNG")
cir = Label(window, image=cir3)
cir.pack(padx=1, pady=1, side=LEFT)

t, V = symbols('t, V')
V1, V2, V3 = symbols('V1 V2 V3')

LabVo = Label(window , text="Vo", font=("Arial", 10))
LabVo.pack(padx=1, pady=1)
txtVo = Entry(window,width=10)
txtVo.pack(padx=5, pady=1)

Labw = Label(window , text="frequency (w)", font=("Arial", 10))
Labw.pack(padx=1, pady=1)
txtw = Entry(window,width=10)
txtw.pack(padx=5, pady=1)

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

LabR4 = Label(window , text="R4", font=("Arial", 10))
LabR4.pack(padx=1, pady=1)
txtR4 = Entry(window,width=10)
txtR4.pack(padx=5, pady=1)

LabR5 = Label(window , text="R5", font=("Arial", 10))
LabR5.pack(padx=1, pady=1)
txtR5 = Entry(window,width=10)
txtR5.pack(padx=5, pady=1)

LabR6 = Label(window , text="R6", font=("Arial", 10))
LabR6.pack(padx=1, pady=1)
txtR6 = Entry(window,width=10)
txtR6.pack(padx=5, pady=1)

LabC1 = Label(window , text="C1", font=("Arial", 10))
LabC1.pack(padx=1, pady=1)
txtC1 = Entry(window,width=10)
txtC1.pack(padx=5, pady=1)

LabC2 = Label(window , text="C2", font=("Arial", 10))
LabC2.pack(padx=1, pady=1)
txtC2 = Entry(window,width=10)
txtC2.pack(padx=5, pady=1)

def clicked():

    Vo = int(txtVo.get())
    w = int(txtw.get())
    V = Vo*exp(1j*w*t)
    R1 = int(txtR1.get())
    R2 = int(txtR2.get())
    R3 = int(txtR3.get())
    R4 = int(txtR4.get())
    R5 = int(txtR5.get())
    R6 = int(txtR6.get())
    C1 = int(txtC1.get())
    C2 = int(txtC2.get())

    if (txtC1.get() == "0" and txtC2.get() == "0") :
        V1_eq = Eq((V/(R1+R4))*R1 - V1, 0)
        V2_eq = Eq((V/(R2+R5))*R2 - V2, 0)
        V3_eq = Eq((V/(R3+R6))*R3 - V3, 0)

        res1 = solve(V1_eq, V1)
        res2 = solve(V2_eq, V2)
        res3 = solve(V3_eq, V3)

        LabresV1.configure(text= res1)
        LabV1.configure(text="V1=")
        LabresV2.configure(text= res2)
        LabV2.configure(text="  V2=")
        LabresV3.configure(text= res3)
        LabV3.configure(text="  V3=")

    elif (txtR4.get() == "0" or txtR5.get() == "0" or txtR6.get() == "0"):
        messagebox.showerror('showerror', 'R4, R5 ,R6 Can not be zeros')

    elif (txtC1.get() == "0" and txtC2.get() != "0") :
        V1_eq = Eq((V/(R1+R4))*R1 - V1, 0)
        V2_eq = Eq((V2-V)/R2 + (V2/R5) + (V2-V3)/(1/(1j*w*C2)), 0)
        V3_eq = Eq((V3-V)/R3 + (V3-V2)/(1/(1j*w*C2)) + (V3/R6), 0)

        res1 = solve(V1_eq, V1)
        res = solve((V2_eq,V3_eq), (V2, V3) )

        LabresV1.configure(text= res1)
        LabV1.configure(text="V1=")
        LabresV2.configure(text= res[V2])
        LabV2.configure(text="  V2=")
        LabresV3.configure(text= res[V3])
        LabV3.configure(text="  V3=")

    elif (txtC1.get() != "0" and txtC2.get() == "0") :
        V1_eq = Eq((V1-V)/R1 + (V1-V2)/(1/(1j*w*C1)) + (V1/R4), 0)
        V2_eq = Eq((V2-V)/R2 + (V2/R5) + (V2-V1)/(1/(1j*w*C1)), 0)
        V3_eq = Eq((V/(R3+R6))*R3 - V3, 0)

        res3 = solve(V3_eq, V3)
        res = solve(( V1_eq,V2_eq), (V1, V2) )

        LabresV1.configure(text= res[V1])
        LabV1.configure(text="V1=")
        LabresV2.configure(text= res[V2])
        LabV2.configure(text="  V2=")
        LabresV3.configure(text= res3)
        LabV3.configure(text="  V3=")

    else:
        V1_eq = Eq((V1-V)/R1 + (V1-V2)/(1/(1j*w*C1)) + (V1/R4), 0)
        V2_eq = Eq((V2-V)/R2 + (V2-V1)/(1/(1j*w*C1)) + (V2/R5) + (V2-V3)/(1/(1j*w*C2)), 0)
        V3_eq = Eq((V3-V)/R3 + (V3-V2)/(1/(1j*w*C2)) + (V3/R6), 0)

        res = solve(( V1_eq,V2_eq,V3_eq), (V1, V2, V3) )

        LabresV1.configure(text= res[V1])
        LabV1.configure(text="V1=")
        LabresV2.configure(text= res[V2])
        LabV2.configure(text="  V2=")
        LabresV3.configure(text= res[V3])
        LabV3.configure(text="  V3=")

btn = Button(window, text="calculate", bg="black", fg="white", command=clicked)
btn.pack(padx=1, pady=10)

LabV1 = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabV1.pack(padx=1, pady=1)
LabresV1 = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabresV1.pack(padx=1, pady=1)

LabV2 = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabV2.pack(padx=1, pady=1)
LabresV2 = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabresV2.pack(padx=1, pady=1)


LabV3 = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabV3.pack(padx=1, pady=1)
LabresV3 = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabresV3.pack(padx=1, pady=1)

window.mainloop()
