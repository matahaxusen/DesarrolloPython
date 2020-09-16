from tkinter import *

root = Tk()

miFrame = Frame(root)
miFrame.pack()

#-----------------SECCION VARIABLES-----------------------------------

operacion = ""
resultado = 0

#funcion suma
def suma(num):
    global operacion
    global resultado

    resultado += float(num)
    operacion="suma"
    numeroPantalla.set(resultado)

def resta(num):
    global operacion
    global resultado

    resultado = resultado - float(num)
    operacion = "resta"
    numeroPantalla.set(resultado)


#-----------------PANTALLA--------------------------------------

numeroPantalla=StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=5, pady=5,columnspan=4)
pantalla.config(background="black", fg="#03f943",justify="right")


#-----------------PULSACIONES TECLADO-------------------------------

def NumeroPulsado(num):

    global operacion
    if operacion=="suma":
        numeroPantalla.set(num)
        operacion=""
    elif operacion=="resta":
        numeroPantalla.set(num)
        operacion="resta"
    else:
        numeroPantalla.set(numeroPantalla.get()+num)

#---------------EL RESULTADO----------------------------------------

def elResultado():

    global resultado

    if operacion == "suma":
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
        resultado = 0;
        operacion = ""
    elif operacion == "resta":
        numeroPantalla.set(resultado - int(numeroPantalla.get()))
        resultado = 0;
        operacion = ""
    else:
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
        resultado = 0;
        operacion = ""

#-----------------FILA 1--------------------------------------------

button7 = Button(miFrame, text="7",width=3, command=lambda:NumeroPulsado("7"))
button7.grid(row=2,column=1)
button8 = Button(miFrame, text="8",width=3, command=lambda:NumeroPulsado("8"))
button8.grid(row=2,column=2)
button9 = Button(miFrame, text="9",width=3, command=lambda:NumeroPulsado("9"))
button9.grid(row=2,column=3)
buttonDiv = Button(miFrame, text="/",width=3)
buttonDiv.grid(row=2,column=4)

#-----------------FILA 2--------------------------------------------

button4 = Button(miFrame, text="4",width=3, command=lambda:NumeroPulsado("4"))
button4.grid(row=3,column=1)
button5 = Button(miFrame, text="5",width=3, command=lambda:NumeroPulsado("5"))
button5.grid(row=3,column=2)
button6 = Button(miFrame, text="6",width=3, command=lambda:NumeroPulsado("6"))
button6.grid(row=3,column=3)
buttonMul = Button(miFrame, text="X",width=3)
buttonMul.grid(row=3,column=4)

#-----------------FILA 3--------------------------------------------

button1 = Button(miFrame, text="1",width=3, command=lambda:NumeroPulsado("1"))
button1.grid(row=4,column=1)
button2 = Button(miFrame, text="2",width=3, command=lambda:NumeroPulsado("2"))
button2.grid(row=4,column=2)
button3 = Button(miFrame, text="3",width=3, command=lambda:NumeroPulsado("3"))
button3.grid(row=4,column=3)
buttonRes = Button(miFrame, text="-",width=3, command=lambda:resta(int(numeroPantalla.get())* -1))
buttonRes.grid(row=4,column=4)

#-----------------FILA 4--------------------------------------------

button0 = Button(miFrame, text="0",width=3, command=lambda:NumeroPulsado("0"))
button0.grid(row=5,column=1)
buttonComa = Button(miFrame, text=".",width=3, command=lambda:NumeroPulsado("."))
buttonComa.grid(row=5,column=2)
buttonIgual = Button(miFrame, text="=",width=3, command=lambda:elResultado())
buttonIgual.grid(row=5,column=3)
buttonSum = Button(miFrame, text="+",width=3, command=lambda:suma(numeroPantalla.get()))
buttonSum.grid(row=5,column=4)


root.mainloop()
