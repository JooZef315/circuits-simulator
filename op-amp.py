from tkinter import *

window = Tk()
window.title("Circuit 5 - op-amp")
cir5 = PhotoImage(file="op-amp.PNG")
cir = Label(window, image=cir5)
cir.pack(padx=1, pady=1, side=LEFT)

LabVi = Label(window , text="Vi", font=("Arial", 10))
LabVi.pack(padx=1, pady=1)
txtVi = Entry(window,width=10)
txtVi.pack(padx=5, pady=1)

LabR1 = Label(window , text="R1(ohm)", font=("Arial", 10))
LabR1.pack(padx=1, pady=1)
txtR1 = Entry(window,width=10)
txtR1.pack(padx=5, pady=1)

LabRf = Label(window , text="Rf(ohm)", font=("Arial", 10))
LabRf.pack(padx=1, pady=1)
txtRf = Entry(window,width=10)
txtRf.pack(padx=5, pady=1)

def clicked():
    Vi = int(txtVi.get())
    R1 = int(txtR1.get())
    Rf = int(txtRf.get())

    Vo = (-Vi)*(Rf/R1)
    A = (-Vo/Vi)*100

    LabresVo.configure(text= Vo)
    LabVo.configure(text="  Vo=")
    LabresA.configure(text= A)
    LabA.configure(text="  A(gain)=")

btn = Button(window, text="calculate", bg="black", fg="white", command=clicked)
btn.pack(padx=1, pady=10)

LabVo = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabVo.pack(padx=1, pady=1, side=LEFT )
LabresVo = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabresVo.pack(padx=1, pady=1, side=LEFT)

LabA = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabA.pack(padx=1, pady=1, side=LEFT)
LabresA = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabresA.pack(padx=1, pady=1, side=LEFT)


window.mainloop()
