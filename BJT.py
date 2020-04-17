from tkinter import *

window = Tk()
window.title("Circuit 4 - BJT")
cir4 = PhotoImage(file="BJT.PNG")
cir = Label(window, image=cir4)
cir.pack(padx=1, pady=1, side=LEFT)


LabVcc = Label(window , text="Vcc", font=("Arial", 10))
LabVcc.pack(padx=1, pady=1)
txtVcc = Entry(window,width=10)
txtVcc.pack(padx=5, pady=1)

LabR_b = Label(window , text="R_b(ohm)", font=("Arial", 10))
LabR_b.pack(padx=1, pady=1)
txtR_b = Entry(window,width=10)
txtR_b.pack(padx=5, pady=1)

LabR_c = Label(window , text="R_c(ohm)", font=("Arial", 10))
LabR_c.pack(padx=1, pady=1)
txtR_c = Entry(window,width=10)
txtR_c.pack(padx=5, pady=1)

LabB = Label(window , text="B", font=("Arial", 10))
LabB.pack(padx=1, pady=1)
txtB = Entry(window,width=10)
txtB.pack(padx=5, pady=1)

Labr_o = Label(window , text="r_o(ohm)", font=("Arial", 10))
Labr_o.pack(padx=1, pady=1)
txtr_o = Entry(window,width=10)
txtr_o.pack(padx=5, pady=1)

def clicked():
    Vcc = int(txtVcc.get())
    R_b = int(txtR_b.get())
    R_c = int(txtR_c.get())
    B = int(txtB.get())
    r_o = int(txtr_o.get())

    I_B = (Vcc-0.7)/R_b
    I_C = I_B*B
    Vce = Vcc - (I_C*R_c)

    I_E = I_B*(B + 1)
    rE = 0.026 / I_E
    Zi = (R_b*B*rE)/(R_b+ B*rE)
    Zo = (R_c*r_o)/(R_c+ r_o)
    Av = (-Zo)/rE

    LabresI_B.configure(text= I_B)
    LabI_B.configure(text="I_B(A)=")
    LabresI_C.configure(text= I_C)
    LabI_C.configure(text="  I_C(A)=")
    LabresVce.configure(text= Vce)
    LabVce.configure(text="  Vce=")
    LabresZi.configure(text= Zi)
    LabZi.configure(text="  Zi(ohm)=")
    LabresZo.configure(text= Zo)
    LabZo.configure(text="  Zo(ohm)=")
    LabresAv.configure(text= Av)
    LabAv.configure(text="  Av=")
btn = Button(window, text="calculate", bg="black", fg="white", command=clicked)
btn.pack(padx=1, pady=10)

LabI_B = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabI_B.pack(padx=1, pady=1)
LabresI_B = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabresI_B.pack(padx=1, pady=1)

LabI_C = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabI_C.pack(padx=1, pady=1)
LabresI_C = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabresI_C.pack(padx=1, pady=1)

LabVce = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabVce.pack(padx=1, pady=1)
LabresVce = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabresVce.pack(padx=1, pady=1)

LabZi = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabZi.pack(padx=1, pady=1)
LabresZi = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabresZi.pack(padx=1, pady=1)

LabZo = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabZo.pack(padx=1, pady=1)
LabresZo = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabresZo.pack(padx=1, pady=1)

LabAv = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabAv.pack(padx=1, pady=1)
LabresAv = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabresAv.pack(padx=1, pady=1)


window.mainloop()
