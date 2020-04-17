from tkinter import *
import matplotlib.pyplot as plt
import math

window = Tk()
window.title("Circuit 5 - op-amp")
cir5 = PhotoImage(file="op-amp2.PNG")
cir = Label(window, image=cir5)
cir.pack(padx=1, pady=1, side=LEFT)

LabVi = Label(window , text="Vi", font=("Arial", 10))
LabVi.pack(padx=1, pady=1)
txtVi = Entry(window,width=10)
txtVi.pack(padx=5, pady=1)

LabRg = Label(window , text="Rg(ohm)", font=("Arial", 10))
LabRg.pack(padx=1, pady=1)
txtRg = Entry(window,width=10)
txtRg.pack(padx=5, pady=1)

LabRf = Label(window , text="Rf(ohm)", font=("Arial", 10))
LabRf.pack(padx=1, pady=1)
txtRf = Entry(window,width=10)
txtRf.pack(padx=5, pady=1)

LabR1 = Label(window , text="R1(ohm)", font=("Arial", 10))
LabR1.pack(padx=1, pady=1)
txtR1 = Entry(window,width=10)
txtR1.pack(padx=5, pady=1)

LabC1 = Label(window , text="C1", font=("Arial", 10))
LabC1.pack(padx=1, pady=1)
txtC1 = Entry(window,width=10)
txtC1.pack(padx=5, pady=1)


def clicked1():
    Vi = int(txtVi.get())
    Rg = int(txtRg.get())
    Rf = int(txtRf.get())

    Vo = Vi*(1 + (Rf / Rg))
    A = (1 + (Rf / Rg))*100

    LabresVo.configure(text= Vo)
    LabVo.configure(text="  Vo=")
    LabresA.configure(text= A)
    LabA.configure(text="  A(gain)=")

btn1 = Button(window, text="calculate", bg="black", fg="white", command=clicked1)
btn1.pack(padx=1, pady=10)

def clicked2():
    f = range(0,1000)
    Vi = int(txtVi.get())
    Rg = int(txtRg.get())
    Rf = int(txtRf.get())
    R1 = int(txtR1.get())
    C1 = float(txtC1.get())

    fc = 1 / (2*math.pi*R1*C1)
    A = 1 + (Rf / Rg)
    Av = []
    Amax = []
    for i in f:
        Av.append(A / math.sqrt( 1 + math.pow((i/fc),2)))
    for i in f:
        Amax.append(20*math.log10(Av[i]))
    plt.style.use('ggplot')
    plt.semilogx(f, Amax,label='frequency response')
    plt.plot([fc,fc],[0,20*math.log10(Av[int(fc)])],label='fc')
    plt.grid(True, which="both")
    plt.xlabel('frequency')
    plt.ylabel('gain (dB)')
    plt.title('op-amp filter frequency response')
    plt.legend()
    plt.show()
btn2 = Button(window, text="frequency response", bg="black", fg="white", command=clicked2)
btn2.pack(padx=1, pady=10)

LabVo = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabVo.pack(padx=1, pady=1, side=LEFT )
LabresVo = Label(window , text=" ", font=("Arial Bold", 15), fg="red")
LabresVo.pack(padx=1, pady=1, side=LEFT)

LabA = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabA.pack(padx=1, pady=1, side=LEFT)
LabresA = Label(window , text=" ", font=("Arial Bold", 15), fg="blue")
LabresA.pack(padx=1, pady=1, side=LEFT)

window.mainloop()
