from tkinter import *
from tkinter import messagebox
from math import sqrt

raiz = Tk()
raiz.title("Calculator")
raiz.iconbitmap("Calculator.ico")
raiz.config(bg="#1B181C")
raiz.resizable(False, False)
raiz.attributes("-alpha", 0.9)
miFrame = Frame(raiz)
miFrame.config(bg="#1B181C")
miFrame.pack()
numeroPantalla = StringVar()
numeroPantalla2 = StringVar()
operacion = ""
resultado = ""
opIgual = ""
lista_Pantalla = []


def numeroPulsado(num):
    global operacion
    lista_Pantalla.append(num)
    numeroPantalla2.set(lista_Pantalla)
    if operacion != "":
        numeroPantalla.set(num)
        operacion = ""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)


def oper(num, op):
    global operacion
    global resultado
    global opIgual

    if resultado == "":
        resultado = num
        operacion = "full"
        opIgual = op
    else:
        if op == "/" and num == "0":
            messagebox.showerror("Error", "Cannot Divide by 0")
            numeroPantalla.set("")
        elif op == "√":
            resultado = sqrt(float(resultado))
            numeroPantalla.set(resultado)
            resultado = ""
            opIgual = ""
        else:
            resultado = eval(str(resultado) + op + num)
            operacion = "full"
            opIgual = op
            numeroPantalla.set(resultado)
    lista_Pantalla.append(opIgual)
    numeroPantalla2.set(lista_Pantalla)


def el_resultado():
    global resultado
    global opIgual
    if opIgual == "√":
        numeroPantalla.set(sqrt(float(resultado)))
        resultado = ""
        opIgual = ""
    else:
        try:
            numeroPantalla.set(eval(str(resultado) + opIgual + numeroPantalla.get()))
            resultado = ""
            opIgual = ""
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot Divide by 0")
            numeroPantalla.set("")


def clearOper():
    global resultado
    numeroPantalla.set("")
    resultado = ""
    lista_Pantalla.clear()
    numeroPantalla2.set("")


pantalla = Entry(miFrame,
                 bg="#1B181C",
                 fg="#FEFCFE",
                 justify="right",
                 textvariable=numeroPantalla,
                 font=("Helvetica", 17, "bold"), borderwidth=0, highlightthickness=0
                 ).grid(row=1, column=1, pady=5, columnspan=4)
pantalla2 = Entry(miFrame,
                  bg="#1B181C",
                  fg="#283240",
                  justify="right",
                  textvariable=numeroPantalla2,
                  font=("Helvetica", 17, "bold"), borderwidth=0, highlightthickness=0
                  ).grid(row=0, column=1, pady=5, columnspan=4)

boton7 = Button(miFrame,
                text="7",
                command=lambda: numeroPulsado("7"),
                width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=4, column=1, pady=2)
boton8 = Button(miFrame,
                text="8",
                command=lambda: numeroPulsado("8"),
                width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=4, column=2)
boton9 = Button(miFrame,
                text="9",
                command=lambda: numeroPulsado("9"),
                width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=4, column=3)
botonDiv = Button(miFrame,
                  text="/",
                  command=lambda: oper(numeroPantalla.get(), "/"),
                  width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#333333",
                  font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=4, column=4)

boton4 = Button(miFrame,
                text="4",
                command=lambda: numeroPulsado("4"),
                width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=5, column=1, pady=2)
boton5 = Button(miFrame,
                text="5",
                command=lambda: numeroPulsado("5"),
                width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=5, column=2)
boton6 = Button(miFrame,
                text="6",
                command=lambda: numeroPulsado("6"),
                width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=5, column=3)
botonMul = Button(miFrame,
                  text="*",
                  command=lambda: oper(numeroPantalla.get(), "*"),
                  width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#333333",
                  font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=5, column=4)

boton1 = Button(miFrame,
                text="1",
                command=lambda: numeroPulsado("1"),
                width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=6, column=1, pady=2)
boton2 = Button(miFrame,
                text="2",
                command=lambda: numeroPulsado("2"),
                width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=6, column=2)
boton3 = Button(miFrame,
                text="3",
                command=lambda: numeroPulsado("3"),
                width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=6, column=3)
botonRes = Button(miFrame,
                  text="-",
                  command=lambda: oper(numeroPantalla.get(), "-"),
                  width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#333333",
                  font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=6, column=4)

boton0 = Button(miFrame,
                text="0",
                command=lambda: numeroPulsado("0"),
                width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=7, column=2, pady=2)
botonPunt = Button(miFrame,
                   text=".",
                   command=lambda: numeroPulsado("."),
                   width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                   font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=7, column=1)
botonIgul = Button(miFrame,
                   text="=",
                   command=lambda: el_resultado(),
                   width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#333333",
                   font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=7, column=3)
botonSum = Button(miFrame,
                  text="+",
                  command=lambda: oper(numeroPantalla.get(), "+"),
                  width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#333333",
                  font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=7, column=4)
botonClear = Button(miFrame,
                    text="CE",
                    command=lambda: clearOper(),
                    width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#333333",
                    font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=8, column=4, pady=2)
botonexp = Button(miFrame,
                  text="^",
                  command=lambda: oper(numeroPantalla.get(), "**"),
                  width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#333333",
                  font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=8, column=3)
botonraiz = Button(miFrame,
                   text="√",
                   command=lambda: oper(numeroPantalla.get(), "√"),
                   width=3, bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#333333",
                   font=("Helvetica", 20, "bold"), borderwidth=0).grid(row=8, column=2)
raiz.mainloop()
