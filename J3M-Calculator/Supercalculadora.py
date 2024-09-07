from tkinter import Tk, PhotoImage, StringVar, W, N , E ,S, ttk
from tkinter.ttk import *
from tkinter import simpledialog
from fractions import Fraction
import numpy as np
from random import randint
import sympy as sp
import tkinter as tk
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from math import *
from tkinter import simpledialog, Tk
from numpy import *
import customtkinter
from sympy import symbols, integrate,simplify,pretty
from tkinter.messagebox import askyesno


potencia = {
    '^': '**'
    
}
def calculadora():
    def ingresarValores(tecla):
        if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.' or tecla == '**':
            entrada2.set(entrada2.get() + tecla)
            
        if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-' or tecla == 'Mod' or tecla == 'Div':
            if tecla == '*':
                entrada1.set(entrada2.get() + '*')
            elif tecla == '/':
                entrada1.set(entrada2.get() + '/')
            elif tecla == '+':
                entrada1.set(entrada2.get() + '+')
            elif tecla == '-':
                entrada1.set(entrada2.get() + '-')
            elif tecla == '**':
                entrada1.set(entrada2.get() + '**' ) 
            elif tecla == 'Mod':
                entrada1.set(entrada2.get() + '%')
            elif tecla == 'Div':
                entrada1.set(entrada2.get() + '//')
            entrada2.set('')
        if tecla == "=":
            entrada1.set(entrada1.get() + entrada2.get())
            resultado = eval(entrada1.get())
            entrada2.set(resultado)


    def euler():
        entrada1.set('')
        resultado = math.e
        entrada2.set(resultado)
    def redon():
        entrada1.set('')
        resultado = round(float(entrada2.get()))
        entrada2.set(resultado)
    def raiz_cuadrada():
        entrada1.set('')
        resultado = math.sqrt(float(entrada2.get()))
        entrada2.set(resultado)    
    def pi():

        entrada1.set('')
        resultado = math.pi
        entrada2.set(resultado)
    def log10n():
        entrada1.set('')
        resultado = log10(float(entrada2.get()))
        entrada2.set(resultado)

    def numero_aureo():
        entrada1.set('')
        resultado  = (1 + math.sqrt(5)) / 2
        entrada2.set(resultado)
    def sen():
        entrada1.set('')
        resultado = sin(((float(entrada2.get())) * math.pi)/180)
        if resultado < 1e-15 and resultado > 0 or resultado < 0 and resultado > -1e-10:
            resultado = 0.0

        entrada2.set(resultado)
    def coss():
        entrada1.set('')
        resultado = cos((((float(entrada2.get())) * math.pi)/180))
        if abs(resultado) < 1e-15:
            resultado = 0.0
        entrada2.set(resultado)
    def tann():
        entrada1.set('')
        resultado = tan(((float(entrada2.get())) * math.pi)/180)
        if abs(resultado) > 1e15:
            resultado = 'Indefinido'
        elif resultado < 1e-15 and resultado > 0 or resultado < 0 and resultado > -1e-10:
            resultado = 0.0

        entrada2.set(resultado)
    def cotan():
        entrada1.set('')
        
        resultado = 1/(tan(((float(entrada2.get())) * math.pi)/180))

        if abs(resultado) < 1e-15:
            resultado = 0.0
        elif abs(resultado) >= 2*math.pi:
            resultado = 'Indefinido'
        entrada2.set(resultado)
    def sec():
        
        entrada1.set('')
        resultado = 1/(cos(((float(entrada2.get())) * math.pi)/180))
        if abs(resultado) < 1e-15:
            resultado = 0.0
        elif abs(resultado) > 1e15:
            resultado = 'Indefinido'
        entrada2.set(resultado)
    def csc():
        
        entrada1.set('')
        resultado = 1/(sin(((float(entrada2.get())) * math.pi)/180))
        if abs(resultado) < 1e-15:
            resultado = 0.0
        elif abs(resultado) > 1e15:
            resultado = 'Indefinido'
        entrada2.set(resultado)
        
    def asen():
        entrada1.set('') 
        valor_ingresado = float(entrada2.get())  
        resultado = degrees(arcsin(valor_ingresado)) 
        if valor_ingresado >= -1 and valor_ingresado <= 1: 
            if abs(resultado) < 1e-15:
                resultado = 0.0
        elif abs(resultado) > 1e15:
            resultado = 'Indefinido'
        else:
            resultado = 'Fuera de rango' 

        entrada2.set(resultado) 
    
    def acos():


        valor_ingresado = float(entrada2.get())

    
        if valor_ingresado >= -1 and valor_ingresado <= 1:
            resultado_radianes = arccos(valor_ingresado)
            resultado_grados = degrees(resultado_radianes)
        else:
            resultado_grados = 'Fuera de rango'

        entrada2.set(resultado_grados) 

    def absoluto():
        entrada1.set('')
        resultado = abs(float(entrada2.get()))
        entrada2.set(resultado)
    def borrar():
        inicio = 0
        final = len(entrada2.get())

        entrada2.set(entrada2.get()[inicio:final - 1])
    def borrartodo():
        entrada1.set('')
        entrada2.set('')
    def aleatorio():
        numero1 = simpledialog.askinteger("Número 1", "Ingrese el primer número:")
        numero2 = simpledialog.askinteger("Número 2", "Ingrese el segundo número:")
        
    
        if numero1 is not None and numero2 is not None:
            
            numero_aleatorio = randint(numero1, numero2)
            
            
            ventana_resultado = tk.Toplevel(root)
            ventana_resultado.geometry('+100+200')
            ventana_resultado.minsize(width=300 ,height= 100)
            ventana_resultado.maxsize(width=300 ,height= 100)
            etiqueta_resultado = tk.Label(ventana_resultado, text=f"Número aleatorio entre {numero1} y {numero2}: {numero_aleatorio}")
            etiqueta_resultado.grid(row=2)
            etiqueta_resultado.pack()
    
    

    root1 = tk.Toplevel()

    root1.title("Calculadora")
    root1.geometry("500x500")
    root1.columnconfigure(0, weight=1)
    root1.rowconfigure(0, weight=1)

   

    root = ttk.Frame(root1, style="mainframe.TFrame")
    root.grid(column=0, row=0, sticky=(W, N, E ,S))
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)
    root.columnconfigure(6, weight=1)



    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=1)

   


    entrada1 = StringVar()
    label_entrada1 = ttk.Label(root, textvariable=entrada1, anchor= "e", font="80",foreground="#000000")
    label_entrada1.grid(row=0, column=0, columnspan=8, sticky=(W,N,E,S))

    entrada2 = StringVar()
    label_entrada2 = ttk.Label(root, textvariable=entrada2, anchor= "e", font="100",foreground="#000000")
    label_entrada2.grid(row=1, column=0, columnspan=8, sticky=(W,N,E,S))

    

    button0 = customtkinter.CTkButton(root, text="0", command=lambda: ingresarValores('0'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button1 = customtkinter.CTkButton(root, text="1", command=lambda: ingresarValores('1'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button2 = customtkinter.CTkButton(root, text="2", command=lambda: ingresarValores('2'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button3 = customtkinter.CTkButton(root, text="3", command=lambda: ingresarValores('3'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button4 = customtkinter.CTkButton(root, text="4", command=lambda: ingresarValores('4'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button5 = customtkinter.CTkButton(root, text="5", command=lambda: ingresarValores('5'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button6 = customtkinter.CTkButton(root, text="6", command=lambda: ingresarValores('6'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button7 = customtkinter.CTkButton(root, text="7", command=lambda: ingresarValores('7'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button8 = customtkinter.CTkButton(root, text="8", command=lambda: ingresarValores('8'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button9 = customtkinter.CTkButton(root, text="9", command=lambda: ingresarValores('9'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_aleatorio = customtkinter.CTkButton(root, text='Al',command=lambda: aleatorio(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_borrar = customtkinter.CTkButton(root, text=chr(9003), command=lambda: borrar(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_borrar_todo = customtkinter.CTkButton(root, text="C", command=lambda:borrartodo(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_parentesis1 = customtkinter.CTkButton(root, text="(", command=lambda: ingresarValores('('),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_parentesis2 = customtkinter.CTkButton(root, text=")", command=lambda: ingresarValores(')'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_punto = customtkinter.CTkButton(root, text=".", command=lambda: ingresarValores('.'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_pi = customtkinter.CTkButton(root, text='π', command=lambda: pi(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_aureo = customtkinter.CTkButton(root, text= 'φ', command=lambda: numero_aureo(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_division = customtkinter.CTkButton(root, text=chr(247), command=lambda: ingresarValores('/'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_multiplicacion = customtkinter.CTkButton(root, text="x", command=lambda: ingresarValores('*'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_resta = customtkinter.CTkButton(root, text="-", command=lambda: ingresarValores('-'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_suma = customtkinter.CTkButton(root, text="+", command=lambda: ingresarValores('+'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_sen = customtkinter.CTkButton(root, text= 'sen(θ)', command=lambda: sen(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_igual = customtkinter.CTkButton(root, text="=", command=lambda: ingresarValores("="),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_raiz_cuadrada = customtkinter.CTkButton(root, text="√", command=lambda:raiz_cuadrada(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_cos = customtkinter.CTkButton(root, text= 'cos(θ)', command=lambda: coss(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_tan = customtkinter.CTkButton(root, text= 'tan(θ)', command=lambda: tann(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_cot = customtkinter.CTkButton(root, text= 'ctan(θ)',command=lambda: cotan(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_sec = customtkinter.CTkButton(root, text= 'sec(θ)', command=lambda: sec(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_csc = customtkinter.CTkButton(root, text= 'csc(θ)', command=lambda: csc(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_arcsen = customtkinter.CTkButton(root, text= 'arsen(θ)', command=lambda: asen(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_arccos = customtkinter.CTkButton(root, text= 'arccos(θ)', command=lambda: acos(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_abs = customtkinter.CTkButton(root, text= '|x|', command=lambda: absoluto(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_potencia = customtkinter.CTkButton(root, text= '^' , command=lambda:ingresarValores('**'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_logaritmo10 = customtkinter.CTkButton(root, text= 'Log10', command=lambda:log10n(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_redon = customtkinter.CTkButton(root, text='Redon', command=lambda:redon(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_mod = customtkinter.CTkButton(root, text='Mod', command=lambda: ingresarValores('Mod',fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF"),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_div = customtkinter.CTkButton(root, text='Div', command=lambda:ingresarValores('Div'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_euler = customtkinter.CTkButton(root, text="e", command=lambda: euler(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")

    button_potencia.grid(column=4, row = 3, sticky=(W,N,E,S))
    button_parentesis1.grid(column=0, row=2,sticky=(W,N,E,S))
    button_parentesis2.grid(column=1, row=2,sticky=(W,N,E,S))
    button_borrar_todo.grid(column=2, row=2,sticky=(W,N,E,S))
    button_borrar.grid(column=3, row=2,sticky=(W,N,E,S))
    button_pi.grid(column=3 ,  row=7, sticky=(W,N,E,S) )
    button_aureo.grid(column=4, row= 7, sticky=(W,N,E,S))
    button7.grid(column=0, row=3,sticky=(W,N,E,S))
    button8.grid(column=1, row=3,sticky=(W,N,E,S))
    button9.grid(column=2, row=3,sticky=(W,N,E,S))
    button_division.grid(column=3, row=3,sticky=(W,N,E,S))
    button_cos.grid (column= 6, row= 2, sticky=(W,N,E,S))
    button_tan.grid  (column= 6, row= 5, sticky=(W,N,E,S))
    button_cot.grid  (column=5 , row= 3, sticky=(W,N,E,S))
    button_sec.grid (column= 6, row= 3, sticky=(W,N,E,S))
    button_csc.grid (column= 6 , row= 6, sticky=(W,N,E,S))
    button_arcsen.grid  (column= 5, row= 4, sticky=(W,N,E,S))
    button_arccos.grid  (column=6 , row= 4, sticky=(W,N,E,S))
    button_sen.grid(column=5, row=2, sticky=(W,N,E,S))
    button4.grid(column=0, row=4,sticky=(W,N,E,S))
    button5.grid(column=1, row=4,sticky=(W,N,E,S))
    button6.grid(column=2, row=4,sticky=(W,N,E,S))
    button_multiplicacion.grid(column=3, row=4,sticky=(W,N,E,S))
    button_abs.grid(column= 4, row= 4 , sticky=(W,N,E,S))
    button1.grid(column=0, row=5,sticky=(W,N,E,S))
    button1.grid(column=0, row=5,sticky=(W,N,E,S))
    button2.grid(column=1, row=5,sticky=(W,N,E,S))
    button3.grid(column=2, row=5,sticky=(W,N,E,S))
    button_suma.grid(column=3, row=5,sticky=(W,N,E,S))
    button_aleatorio.grid(column=4, row = 5, sticky=(W,N,E,S))
    button0.grid(column=0, row=6, columnspan=2,sticky=(W,N,E,S))
    button_punto.grid(column=2, row=6,sticky=(W,N,E,S))
    button_resta.grid(column=3, row=6,sticky=(W,N,E,S))
    button_logaritmo10.grid(column=4, row=6, sticky=(W,N,E,S))
    button_igual.grid(column=0, row=7, columnspan=2, sticky=(W,N,E,S))
    button_raiz_cuadrada.grid(column=4, row=2,sticky=(W,N,E,S))
    button_redon.grid(column= 5, row=5, sticky=(W,N,E,S))
    button_mod.grid(column=5, row=6, sticky=(W,N,E,S))
    button_div.grid(column=5, row=7, sticky=(W,N,E,S))
    button_euler.grid(column=2, row=7, sticky=(W,N,E,S))
    for child in root.winfo_children():
        child.grid_configure(ipady=10, padx=1, pady=1)
    
    root1.resizable(0,0)

def inte_indefinidas():
    ventana1 = tk.Toplevel()
    ventana1.title("Integrales Definidas")
    ventana1.config(bg="#FFFFFF")
    ventana1.geometry("500x500")
    frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
    frame.pack(pady=20, padx= 20, fill= "both", expand= True) 

    x = symbols('x')
    funcion=customtkinter.CTkEntry(frame,border_color="#f0f0f0",fg_color="#ffffff",text_color="#000000")
    
    funcion.place(x=150,y=139)

    dx_c=customtkinter.CTkLabel(frame,text=f"dx ",font=("Arial",30),text_color="#000000")
    
    dx_c.place(x=300,y=139)
    
    titulo=customtkinter.CTkLabel(master=frame,text="∫", font=("Arial",60),text_color="#000000")
    
    titulo.place(x=125,y=120)

    titulo1=customtkinter.CTkLabel(master=frame,text="Calcule su Integral Definida",font=("Arial",28),text_color="#000000")
    titulo1.pack()

    resultado=None

    def calcular():

        nonlocal resultado  
        if resultado:
                resultado.destroy()

        funcion1=funcion.get()

         
        try:
            integral_indefinida1 = integrate(funcion1, x)
            integral_indefinida_simplificada = simplify(integral_indefinida1)
            resultado_texto = pretty(integral_indefinida_simplificada, use_unicode=True)
            resultado = customtkinter.CTkLabel(frame, text=f"El resultado de su integral es:\n {resultado_texto}", text_color="#000000", font=("Arial", 25))
            
            resultado.place(x=60, y=260)
        except Exception as e:
            resultado = customtkinter.CTkLabel(frame, text=f"Error: {str(e)}", text_color="#FF0000", font=("Arial", 25))
            
            resultado.place(x=60, y=260)

    integrar = customtkinter.CTkButton(frame, text="Integrar la Funcion", command=calcular, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
    
    integrar.place(x=160, y=200)
    

def integrales_definidas():
    ventana1 = tk.Toplevel()
    ventana1.title("Integrales Definidas")
    ventana1.config(bg="#FFFFFF")
    ventana1.geometry("500x400")
    frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
    frame.pack(pady=20, padx= 20, fill= "both", expand= True)  

    lim_supe=customtkinter.CTkEntry(master=frame,width=30,height=20,border_color="#f0f0f0",fg_color="#ffffff",text_color="#000000")
    
    lim_supe.place(x=110,y=120)

    lim_inf=customtkinter.CTkEntry(master=frame,width=30,height=20,border_color="#f0f0f0",fg_color="#ffffff",text_color="#000000")
    
    lim_inf.place(x=110,y=170)
    
    funcion=customtkinter.CTkEntry(frame,border_color="#f0f0f0",fg_color="#ffffff",text_color="#000000")
    
    funcion.place(x=140,y=139)

    dx_c=customtkinter.CTkLabel(frame,text=f"dx ",font=("Arial",30),text_color="#000000")
    
    dx_c.place(x=290,y=139)


    titulo=customtkinter.CTkLabel(master=frame,text="∫", font=("Arial",60),text_color="#000000")
    
    titulo.place(x=90,y=130)

    titulo1=customtkinter.CTkLabel(master=frame,text="Calcule su Integral Definida",font=("Arial",28),text_color="#000000")
    titulo1.pack()

    x = symbols('x')

    resultado=None

    def calculado():

        nonlocal resultado  
        if resultado:
                resultado.destroy() 

        funcion1=funcion.get()
        lim_inf1=lim_inf.get()
        lim_supe1=lim_supe.get()

        lim_inf2=Fraction(lim_inf1)
        lim_supe2=Fraction(lim_supe1)
        
        integral_definida1 = integrate(funcion1, (x, lim_inf2, lim_supe2))
        integral_definida2=pretty(integral_definida1)

        resultado=customtkinter.CTkLabel(frame,text=f"El resultado de su integral es:\n {integral_definida2}",text_color="#000000",font=("Arial",25))
        
        resultado.place(x=60,y=260)

    integrar=customtkinter.CTkButton(frame,text="Integrar la Funcion",command=calculado,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    integrar.place(x=160,y=200)

    

    
def integrales():
    ventana1 = tk.Toplevel()
    ventana1.title("Escoja su tipo de integral")
    ventana1.config(bg="#FFFFFF")
    ventana1.geometry("350x250")
    frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
    frame.pack(pady=20, padx= 20, fill= "both", expand= True)        
    etiqueta2 = tk.Label(frame, text = "Escoja su tipo de integral")
    etiqueta2.pack(padx=10, pady=5)
    boton1 = customtkinter.CTkButton(frame, text="INTEGRAL INDEFINIDA", command=inte_indefinidas,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton1.pack(padx=10, pady=10)
    boton2 = customtkinter.CTkButton(frame, text="INTEGRAL DEFINIDA", command=integrales_definidas,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton2.pack(padx=10, pady=10)
def derivar():
        ventana1 = tk.Toplevel()
        ventana1.title("Escoja su tipo de derivada")
        ventana1.config(bg="#FFFFFF")
        ventana1.geometry("350x250")
        frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)        
        etiqueta2 = tk.Label(frame, text = "Escoja su tipo de Derivada")
        etiqueta2.pack(padx=10, pady=5)
        
        
        def deri_implicita():
            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado")
            ventana_resultado.configure(bg="#FFFFFF")
            ventana_resultado.geometry("600x440")
            frame1 = customtkinter.CTkFrame(master=ventana_resultado, fg_color="#f0f0f0")
            frame1.pack(pady=20, padx=20, fill="both", expand=True)

            x, y = sp.symbols('x y')
            eqn_original = customtkinter.CTkEntry(master=frame1, bg_color="#FFFFFF")
            
            eqn_original.place(x=80, y=80)

            eqn_label = customtkinter.CTkLabel(frame1, text="<- Ingrese la ecuación implícita", text_color="black", font=("Arial", 20))
            
            eqn_label.place(x=275, y=80)

            titulo = customtkinter.CTkLabel(master=frame1, text="Calcula la Derivada Implícita", text_color="black", font=("Doble struck", 28))
            
            titulo.place(x=105, y=10)

            etiqueta_resultado = None

            def calcular():
                nonlocal etiqueta_resultado  
                if etiqueta_resultado:
                    etiqueta_resultado.destroy()  

                eqn = eqn_original.get()

                if eqn:
                    try:
                        eq = sp.sympify(eqn)
                        derivada_implicita = sp.diff(eq, x) / sp.diff(eq, y)
                        derivada_implicita = -derivada_implicita  
                        etiqueta_resultado = tk.Label(ventana_resultado, text=f"La derivada implícita de la ecuación {eqn} es: \n{derivada_implicita}", fg="black", font=("Doble struck", 15))
                        
                        etiqueta_resultado.place(x=100, y=240)
                    except (sp.SympifyError, ValueError) as e:
                        etiqueta_resultado = customtkinter.CTkLabel(frame1, text=f"Error: {e}", text_color="black")
                        
                        etiqueta_resultado.place(x=20, y=200)
                else:
                    etiqueta_resultado = customtkinter.CTkLabel(frame1, text="Por favor, ingrese una ecuación válida.", text_color="black")
                    
                    etiqueta_resultado.place(x=20, y=200)

            boton_calcular = customtkinter.CTkButton(master=frame1, text="Calcular Derivada Implícita", command=calcular, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
            
            boton_calcular.place(y=180, x=200)
        def deri_ordensupe():
            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado")
            ventana_resultado.configure(bg="#FFFFFF")
            ventana_resultado.geometry("670x440")
            frame1 = customtkinter.CTkFrame(master=ventana_resultado, fg_color="#f0f0f0")
            frame1.pack(pady=20, padx=20, fill="both", expand=True)

            x = sp.Symbol('x')

            funcion_original = customtkinter.CTkEntry(master=frame1, bg_color="#FFFFFF")
            
            funcion_original.place(x=80, y=80)

            numero_deri = customtkinter.CTkEntry(master=frame1, bg_color="#ffffff")
            
            numero_deri.place(x=80, y=130)

            orden_supe = customtkinter.CTkLabel(frame1, text="<-Ingrese el orden", text_color="black", font=("Arial", 20))
            
            orden_supe.place(x=300, y=130)

            funcion_deri = customtkinter.CTkLabel(frame1, text="<-Ingrese la funcion a derivar", text_color="black", font=("Arial", 20))
            
            funcion_deri.place(x=300, y=80)

            titulo = customtkinter.CTkLabel(master=frame1, text="Calcula la Derivada de Orden Superior", text_color="black", font=("Doble struck", 28))
            
            titulo.place(x=55, y=10)

            etiqueta_resultado = None

            def calcular_derivada():
                nonlocal etiqueta_resultado  
                if etiqueta_resultado:
                    etiqueta_resultado.destroy()  

                funcion = funcion_original.get()
                orden_str = numero_deri.get()

                if funcion and orden_str:
                    try:
                        orden = int(orden_str)
                        derivada = sp.diff(sp.sympify(funcion), x, orden)
                        etiqueta_resultado = tk.Label(ventana_resultado, text=f"La derivada de orden {orden} de la función {funcion} es: \n{derivada}", fg="black", font=("Doble struck", 15))
                        
                        etiqueta_resultado.place(x=70, y=280)
                    except (sp.SympifyError, ValueError) as e:
                        etiqueta_resultado = customtkinter.CTkLabel(frame1, text=f"Verifique la manera en la que escribio la funcion", text_color="black")
                        
                        etiqueta_resultado.place(x=70, y=280)
                else:
                    etiqueta_resultado = customtkinter.CTkLabel(frame1, text="Por favor, ingresa una función y un orden válido.", text_color="black")
                    
                    etiqueta_resultado.place(x=70, y=280)

            boton_calcular = customtkinter.CTkButton(master=frame1, text="Calcular Derivada", command=calcular_derivada, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
            
            boton_calcular.place(y=180, x=200)

        boton1 = customtkinter.CTkButton(frame, text="Derivada Implicita", command=deri_implicita,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        boton1.pack(padx=10, pady=10)
        boton2 = customtkinter.CTkButton(frame, text="Derivada de Orden Superior", command=deri_ordensupe,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        boton2.pack(padx=10, pady=10)
def sistemas_de_ecuaciones():
    
    ventana2 = tk.Toplevel()
    ventana2.title("Sistemas de ecuaciones lineales")
    ventana2.config(bg="#ffffff")
    frame=customtkinter.CTkFrame(master=ventana2,fg_color="#f0f0f0")
    frame.pack(pady=20, padx= 20, fill= "both", expand= True)
    
    ventana2.minsize(width=300, height=260)
    ventana2.maxsize(width=300, height=350)
    
    etiqueta2 = customtkinter.CTkLabel(frame, text = "𝙴𝚂𝙲𝙾𝙹𝙰 𝙻𝙰 𝙾𝙿𝙴𝚁𝙰𝙲𝙸𝙾𝙽 𝙰 𝚁𝙴𝙰𝙻𝙸𝚉𝙰𝚁", font=("Doble struck",17),text_color="black" )
    etiqueta2.pack(padx=10, pady=5)
    
    
    def matriz():
        def create_matrix_entries():
            def solve_matrix():
                matrix = []
                for i in range(rows):
                    row = []
                    for j in range(cols):
                        try:
                            value = Fraction(entries[i][j].get())
                        except ValueError:
                            error_label.configure(ext="Ingrese numeros")
                            return
                        row.append(value)
                    matrix.append(row)

                vector = []
                for i in range(rows):
                    try:
                        value = Fraction(result_entries[i].get())
                    except ValueError:
                        error_label.configure(text="Ingrese numeros")
                        return
                    vector.append(value)

                
                A = np.array(matrix, dtype=object)
                b = np.array(vector,dtype=object)


                
                
                try:
                    x = np.linalg.solve(A.astype(float), b.astype(float))
                    x_fracciones = [f"{Fraction(num).limit_denominator()}" for num in x]
                    x_resultado = "  ~  ".join(x_fracciones)
                    
                    
                    

                    ventana_resultado = tk.Toplevel()
                    ventana_resultado.title("Resultado")
                    ventana_resultado.config(bg="#ffffff")
                    frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
                    frame.pack(pady=20, padx= 20, fill= "both", expand= True)
                    etiqueta_resultado = customtkinter.CTkLabel(frame, text=f"La solución del sistema de ecuaciones es:\n{x_resultado}",text_color="#000000")
                    etiqueta_resultado.pack(padx=20, pady=20)

                except np.linalg.LinAlgError:
                    ventana_error = tk.Toplevel()
                    ventana_error.title("Error")
                    ventana_error.config(bg="#ffffff")
                    frame=customtkinter.CTkFrame(master=ventana_error,fg_color="#f0f0f0")
                    frame.pack(pady=20, padx= 20, fill= "both", expand= True)
                    etiqueta_error = customtkinter.CTkLabel(frame, text="Su ecuacion no tiene solucion o tiene infinitas soluciones",text_color="#000000")
                    etiqueta_error.pack(padx=20, pady=20)
                    



                
            def inversa():
                matrix = []
                for i in range(rows):
                    row = []
                    for j in range(cols):
                        try:
                            value = Fraction(entries[i][j].get())
                        except ValueError:
                            error_label.configure(text="Ingrese numeros")
                            
                            return
                        row.append(value)
                    matrix.append(row)

                
                A = np.array(matrix, dtype=float64)

                if A.shape[0] != A.shape[1]:
                    ventana_error = tk.Toplevel()
                    ventana_error.title("Error")
                    ventana_error.config(bg="#ffffff")
                    frame=customtkinter.CTkFrame(master=ventana_error,fg_color="#f0f0f0")
                    frame.pack(pady=20, padx= 20, fill= "both", expand= True)
                    
                    etiqueta_error = tk.Label(frame, text="La matriz no es cuadrada, por lo que no tiene inversa.")
                    etiqueta_error.pack(padx=20, pady=20)
                    return

                    
                if np.linalg.det(A) == 0:
                    ventana_error = tk.Toplevel()
                    ventana_error.title("Error")
                    ventana_error.config(bg="#ffffff")
                    frame=customtkinter.CTkFrame(master=ventana_error,fg_color="#f0f0f0")
                    frame.pack(pady=20, padx= 20, fill= "both", expand= True)
                        
                    etiqueta_error = tk.Label(frame, text="La matriz es singular y no tiene inversa.")
                    etiqueta_error.pack(padx=20, pady=20)
                    return                
                
                inversa= (np.linalg.inv(A.astype(float)))
                inversa_fracciones = [[Fraction(num).limit_denominator() for num in row] for row in inversa]
                inversa_resultado = "\n".join(["\t".join(map(str, row)) for row in inversa_fracciones])

                ventana_resultado = tk.Toplevel()
                ventana_resultado.title("Resultado")
                ventana_resultado.config(bg="#ffffff")
                frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
                frame.pack(pady=20, padx= 20, fill= "both", expand= True)
                etiqueta_resultado = customtkinter.CTkLabel(frame, text=f"La matriz inversa es: \n{inversa_resultado}",text_color="#000000")
                etiqueta_resultado.pack(padx=20, pady=20)

            def transpuesta():
                matrix = []
                for i in range(rows):
                    row = []
                    for j in range(cols):
                        try:
                            value = Fraction(entries[i][j].get())
                        except ValueError:
                            error_label.configure(text="Ingrese numeros")
                                
                            return
                        row.append(value)
                    matrix.append(row)

                A = np.array(matrix, dtype=object)

                matriz_transpuesta = np.transpose(A.astype(float))

        
                matriz_cadenas = [[Fraction(num).limit_denominator() for num in row] for row in matriz_transpuesta]
                cadena_matriz = "\n".join(["\t".join(map(str, row)) for row in matriz_cadenas])     
          

                    
                ventana_resultado = tk.Toplevel()
                ventana_resultado.title("Resultado")
                ventana_resultado.config(bg="#ffffff")
                frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
                frame.pack(pady=20, padx= 20, fill= "both", expand= True)
                etiqueta_resultado = tk.Label(frame, text=f"La Transpuesta de su Matrix es: \n {cadena_matriz}")
                etiqueta_resultado.pack(padx=20, pady=20)
            
            def determinante():
                matrix = []
                for i in range(rows):
                    row = []
                    for j in range(cols):
                        try:
                            value = Fraction(entries[i][j].get())
                        except ValueError:
                            error_label.configure(text="Ingrese numeros")
                                
                            return
                        row.append(value)
                    matrix.append(row)

                A = np.array(matrix, dtype=object)

                matriz = np.array(A)
        
                determinante = np.linalg.det(matriz.astype(float))
                det = Fraction(determinante).limit_denominator()

                ventana_resultado = tk.Toplevel()
                ventana_resultado.title("Resultado")
                ventana_resultado.config(bg="#ffffff")
                frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
                frame.pack(pady=20, padx= 20, fill= "both", expand= True)
                etiqueta_resultado = tk.Label(frame, text=f"El determinante de la matriz ingresada es: \n {det}")
                etiqueta_resultado.pack(padx=20, pady=20)

            global rows, cols, entries, result_entries, solve_button, vector_label, boton_inversa, boton_transpuesta, boton_determinante, entry,result_entry
            try:
                new_rows = int(rows_entry.get())
                new_cols = int(cols_entry.get())
            except ValueError:
                error_label.configure(text="Ingrese bien los datos")
                return

            error_label.configure(text="")

           
            if 'entries' in globals() and 'solve_button' in globals() and 'vector_label' in globals() and 'boton_inversa' in globals() and 'boton_determinante' in globals() and "boton_transpuesta"in globals():
                if root.winfo_exists():
                    for row in entries:
                        for entry in row:
                            entry.destroy()
                    for entry in result_entries:
                        entry.destroy()                      
                    solve_button.destroy()
                    vector_label.destroy()
                    boton_inversa.destroy()
                    boton_determinante.destroy()
                    boton_transpuesta.destroy()




            rows, cols = new_rows, new_cols

            entries = []
            result_entries = []

            for r in range(rows):
                row_entries = []
                for c in range(cols):
                    entry = customtkinter.CTkEntry(matrix_frame, width=60, height=30, border_color="#f0f0f0")
                    entry.grid(row=r, column=c, padx=10, pady=5)
                    row_entries.append(entry)
                entries.append(row_entries)

                vector_label = customtkinter.CTkLabel(matrix_frame, text="|", text_color="#000000")
                vector_label.grid(row=r, column=cols, padx=10, pady=5)

                result_entry = customtkinter.CTkEntry(matrix_frame, width=90, height=30, border_color="#f0f0f0")
                result_entry.grid(row=r, column=cols + 1, padx=10, pady=5)
                result_entries.append(result_entry)


            solve_button = customtkinter.CTkButton(dim_frame, text="Resolver Matrix", command=solve_matrix,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            solve_button.grid(row=0, columnspan=cols+1,padx=5,column=cols+1 )
            
            boton_inversa=customtkinter.CTkButton(dim_frame, text="Resolver inversa", command=inversa,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_inversa.grid(row=1, columnspan=cols+1,padx=20,column=cols+1 )
            
            boton_transpuesta=customtkinter.CTkButton(dim_frame, text="Resolver Transpuesta", command=transpuesta,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_transpuesta.grid(row=2, columnspan=cols+1,padx=20,column=cols+1 )

            boton_determinante= customtkinter.CTkButton(dim_frame, text="Resolver Determinante", command=determinante,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_determinante.grid(row=3, columnspan=cols+1,padx=20,column=cols+1 )
            
            
            
            

        # Crear la ventana principal
        root = tk.Toplevel()
        root.title("Sistemas de ecuaciones")
        root.config(bg="#ffffff")
        

        # Crear el marco para la entrada de dimensiones
        dim_frame = customtkinter.CTkFrame(root,fg_color="#f0f0f0")
        dim_frame.pack(pady=20, padx= 20, fill= "both", expand= True)

        rows_label = customtkinter.CTkLabel(dim_frame, text="Numero de columnas: ",text_color="#000000")
        rows_label.grid(row=0, column=0, padx=5, pady=5)
        rows_entry = customtkinter.CTkEntry(dim_frame,border_color="#f0f0f0")
        rows_entry.grid(row=0, column=1, padx=5, pady=5)

        cols_label = customtkinter.CTkLabel(dim_frame, text="Numero de filas: ",text_color="#000000")
        cols_label.grid(row=1, column=0, padx=5, pady=5)
        cols_entry =customtkinter.CTkEntry(dim_frame,border_color="#f0f0f0")
        cols_entry.grid(row=1, column=1, padx=5, pady=5)

        generate_button = customtkinter.CTkButton(dim_frame, text="Generar Matriz", command=create_matrix_entries,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        generate_button.grid(row=2, columnspan=2, pady=10)

        error_label = customtkinter.CTkLabel(dim_frame, text="", text_color="#000000")
        error_label.grid(row=3, columnspan=2, pady=5)

        # Crear el marco para la matriz de entradas
        matrix_frame =customtkinter.CTkFrame(root,fg_color="#f0f0f0")
        matrix_frame.pack(pady=20, padx= 20, fill= "both", expand= True)


    def operaciones_matrices():
        ventana2 = tk.Toplevel()
        ventana2.title("Sistemas de ecuaciones lineales")
        ventana2.config(bg="#ffffff")
        frame=customtkinter.CTkFrame(master=ventana2,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
        
        ventana2.minsize(width=300, height=260)
        ventana2.maxsize(width=300, height=350)
        
        etiqueta2 = customtkinter.CTkLabel(frame, text = "𝙴𝚂𝙲𝙾𝙹𝙰 𝙻𝙰 𝙾𝙿𝙴𝚁𝙰𝙲𝙸𝙾𝙽 𝙰 𝚁𝙴𝙰𝙻𝙸𝚉𝙰𝚁", font=("Doble struck",17),text_color="black" )
        etiqueta2.pack(padx=10, pady=5)

        def suma_matrices():
            r = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la primera matriz: "))
            c = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la primera matriz: "))

            m = []
            for i in range(c):
                l = []
                for j in range(r):
                    v = Fraction(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    l.append(v)
                m.append(l)
        
            a = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la segunda matriz: "))
            b = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la segunda matriz: "))

            q = []
            for i in range(b):
                s = []
                for j in range(a):
                    k = Fraction(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    s.append(k)
                q.append(s)

             
            suma = []
            for i in range(len(m)):
                fila_suma = []
                for j in range(len(m[0])):
                    fila_suma.append(m[i][j] + q[i][j])
                suma.append(fila_suma)
                
                texto = ""
                for fila in suma:
                    fila_texto = "   ".join(map(lambda x: str(Fraction(x).limit_denominator()), fila))  # Convertir elementos de la fila a cadenas y unirlos con comas
                    texto += f"{fila_texto}\n" 

            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado")
            ventana_resultado.config(bg="#ffffff")
            frame=customtkinter.CTkFrame(ventana_resultado,fg_color="#f0f0f0")
            frame.pack(pady=20, padx= 20, fill= "both", expand= True)
            etiqueta_resultado = tk.Label(frame, text=f"El resultado entre su operacion entre matrices es:\n {(texto)}")
            etiqueta_resultado.pack(padx=20, pady=20)


        def resta_marices():
            r = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la primera matriz: "))
            c = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la primera matriz: "))

            m = []
            for i in range(c):
                l = []
                for j in range(r):
                    v = float(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    l.append(v)
                m.append(l)
        
            a = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la segunda matriz: "))
            b = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la segunda matriz: "))

            q = []
            for i in range(b):
                s = []
                for j in range(a):
                    k = Fraction(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    s.append(k)
                q.append(s)

             
            suma = []
            for i in range(len(m)):
                fila_suma = []
                for j in range(len(m[0])):
                    fila_suma.append(m[i][j] - q[i][j])
                suma.append(fila_suma)
                
                texto = ""
                for fila in suma:
                    fila_texto = "   ".join(map(lambda x: str(Fraction(x).limit_denominator()), fila))  
                    texto += f"{fila_texto}\n" 

            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado")
            ventana_resultado.config(bg="#ffffff")
            frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
            frame.pack(pady=20, padx= 20, fill= "both", expand= True)
            etiqueta_resultado = tk.Label(frame, text=f"El resultado de su operacion entre matrices es:\n {(texto)}")
            etiqueta_resultado.pack(padx=20, pady=20)

        def multi_matrices():
            r = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la primera matriz: "))
            c = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la primera matriz: "))

            m = []
            for i in range(c):
                l = []
                for j in range(r):
                    v = Fraction(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    l.append(v)
                m.append(l)
        
            a = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la segunda matriz: "))
            b = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la segunda matriz: "))

            q = []
            for i in range(b):
                s = []
                for j in range(a):
                    k = Fraction(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    s.append(k)
                q.append(s)

             
            multiplicacion = []
            for i in range(len(m)):
                fila_multiplicacion = []
                for j in range(len(q[0])):
                    suma = 0
                    for k in range(len(q)):
                        suma += m[i][k] * q[k][j]
                    fila_multiplicacion.append(suma)
                multiplicacion.append(fila_multiplicacion)
            
            texto = ""
            for fila in multiplicacion:
                fila_texto = "   ".join(map(lambda x: str(Fraction(x).limit_denominator()), fila))  
                texto += f"{fila_texto}\n" 

            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado")
            ventana_resultado.config(bg="#ffffff")
            frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
            frame.pack(pady=20, padx= 20, fill= "both", expand= True)
            etiqueta_resultado = tk.Label(frame, text=f"El resultado de la operacion de la matrices es:\n {(texto)}")
            etiqueta_resultado.pack(padx=20, pady=20)

        
        def escalar_matriz():
            a = Fraction(simpledialog.askstring("Ingrese numero", "Ingrese el escalar"))
            r = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la matriz: "))
            c = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la matriz: "))

            q = []
            for i in range(c):
                s = []
                for j in range(r):
                    k = Fraction(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    s.append(k)
                q.append(s)

            resultado = []
            for fila in q:
                fila_resultado = [elemento * a for elemento in fila]
                resultado.append(fila_resultado)


                texto = ""
                for fila in resultado:
                    fila_texto = "   ".join(map(lambda x: str(Fraction(x).limit_denominator()), fila))  
                    texto += f"{fila_texto}\n"   

            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado")
            ventana_resultado.config(bg="#ffffff")
            frame1=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
            frame1.pack(pady=20, padx= 20, fill= "both", expand= True)
            etiqueta_resultado = tk.Label(frame1, text=f"El resultado de la operacion con matices es:\n {"\n"}{(texto)}")
            etiqueta_resultado.pack(padx=20, pady=20)

    
        boton0=customtkinter.CTkButton(master=frame,text="Suma",command=suma_matrices,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        boton0.pack(padx=20, pady=10)
        boton20=customtkinter.CTkButton(master=frame, text="Resta",command=resta_marices,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        boton20.pack(padx=20, pady=10)
        boton10=customtkinter.CTkButton(master=frame, text="Multiplicacion",command=multi_matrices,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        boton10.pack(padx=20, pady=10)
        boton30=customtkinter.CTkButton(master= frame, text="Por escalar",command=escalar_matriz,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        boton30.pack(padx=20, pady=10)
    

    
    boton1 =customtkinter.CTkButton(frame, text="Calculos de matrices", command= matriz,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton1.pack(padx=10, pady=10)
        

    boton=customtkinter.CTkButton(frame,text="Operaciones entre matrices",command=operaciones_matrices,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton.pack(padx=10, pady=10)


def grafica():
    ventana1=tk.Toplevel()
    ventana1.title("Graficador de funciones")
    ventana1.config(bg="#ffffff")
    ventana1.geometry("500x200")
    frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
    frame.pack(pady=20, padx= 20, fill= "both", expand= True)
    
    def grafica3d():
        
        def plot_function_3d():
            
            function_text = function_entry.get()

            
            ax.clear()
            
            x_min = float(x_min_entry.get())
            x_max = float(x_max_entry.get())
            y_min = float(y_min_entry.get())
            y_max = float(y_max_entry.get())

            x = np.linspace(x_min, x_max, 1000)
            y = np.linspace(y_min, y_max, 1000)
            x, y = np.meshgrid(x, y)
            
            try:
                z = eval(function_text)
                
                ax.plot_surface(x, y, z, cmap='viridis')
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_zlabel('z')
                ax.set_title('Gráfico 3D de la función: ' + function_text)
                ax.grid(True)
                
                
                canvas.draw()
                
            except Exception as e:
                
                error_label.config(text="Error: " + str(e))

        def clear_plot():
            
            ax.clear()
            
            canvas.draw()

        
        root = tk.Toplevel()
        root.title("Graficador de funciones 3D")
        root.geometry("800x600")

        
        function_label = customtkinter.CTkLabel(root, text="Ingrese la función:", text_color="black", font=("Arial", 16))
        function_label.pack()
        function_entry = tk.Entry(root, width=50)
        function_entry.pack()

        
        domain_frame = tk.Frame(root)
        domain_frame.pack()
        x_min_label = tk.Label(domain_frame, text="x mínimo:")
        x_min_label.grid(row=0, column=0)
        x_min_entry = tk.Entry(domain_frame)
        x_min_entry.grid(row=0, column=1)
        x_max_label = tk.Label(domain_frame, text="x máximo:")
        x_max_label.grid(row=0, column=2)
        x_max_entry = tk.Entry(domain_frame)
        x_max_entry.grid(row=0, column=3)
        
        y_min_label = tk.Label(domain_frame, text="y mínimo:")
        y_min_label.grid(row=1, column=0)
        y_min_entry = tk.Entry(domain_frame)
        y_min_entry.grid(row=1, column=1)
        y_max_label = tk.Label(domain_frame, text="y máximo:")
        y_max_label.grid(row=1, column=2)
        y_max_entry = tk.Entry(domain_frame)
        y_max_entry.grid(row=1, column=3)

        
        plot_button = customtkinter.CTkButton(root, text="Graficar", command=plot_function_3d, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        plot_button.pack(pady=5)
        clear_button = customtkinter.CTkButton(root, text="Borrar", command=clear_plot, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        clear_button.pack(pady=5)

        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack()

        
        error_label = tk.Label(root, fg="red")
        error_label.pack()

        
    def graficadefuncion():
        
        def plot_function():
            
            function_text = function_entry.get()

            
            
            
            x_min = float(x_min_entry.get())
            x_max = float(x_max_entry.get())
            x = np.linspace(x_min, x_max, 4000000)
            try:
                y = eval(function_text)
                
                plt.plot(x, y)
                plt.xlabel('x')
                plt.ylabel('f(x)')
                plt.title('Gráfico de la función: ' + function_text)
                plt.grid(True)
                plt.axhline(0, color='black', linewidth=0.5)
                plt.axvline(0, color='black', linewidth=0.5)
                plt.xlim(x_min, x_max)
                plt.tight_layout()
                
                
                canvas.draw()
                
            except Exception as e:
                
                error_label.config(text="Error: " + str(e))

        def clear_plot():
            
            ax.clear()
            
            canvas.draw()

    
        
        root = tk.Toplevel()
    
        root.title("Graficador de funciones")
        
        
        
        function_label = customtkinter.CTkLabel(root, text="Ingrese la función:",text_color="black",font=("Arial",16))
        function_label.pack()
        function_entry = tk.Entry(root, width=50)
        function_entry.pack()

        
        domain_frame = tk.Frame(root)           
        domain_frame.pack()
        x_min_label = tk.Label(domain_frame, text="x mínimo:")
        x_min_label.grid(row=0, column=0)
        x_min_entry = tk.Entry(domain_frame,textvariable="1")
        x_min_entry.grid(row=0, column=1)
        x_max_label = tk.Label(domain_frame, text="x máximo:")
        x_max_label.grid(row=0, column=2) 
        x_max_entry = tk.Entry(domain_frame)
        x_max_entry.grid(row=0, column=3)

       
        plot_button = customtkinter.CTkButton(root, text="Graficar", command=plot_function,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        plot_button.pack(pady=5)
        clear_button = customtkinter.CTkButton(root, text="Borrar", command=clear_plot,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        clear_button.pack(pady=5)


        
        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack()

       
        error_label = tk.Label(root, fg="red")
        error_label.pack()
        
        

    label=customtkinter.CTkLabel(frame,text="Elige tu forma de grafica",text_color="black",font=("Arial",25))
    label.pack()
    boton0=customtkinter.CTkButton(frame,command=grafica3d,text="Grafica 3D",fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
    boton0.pack(padx=20,pady=20)
    boton10=customtkinter.CTkButton(frame,command=graficadefuncion,text="Grafica 2D",fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
    boton10.pack(padx=20,pady=20)
    
    
def operacion_con_complejos():

    def operaciones():


        frame_calculos1.pack_forget()
        
        frame_calculos.pack(pady=10, padx= 15, fill= "both", expand= True) 

        
        a.geometry("500x600")
        
        entry_real = customtkinter.CTkEntry(frame_calculos, border_color="#f0f0f0")
        entry_real.place(x=50, y=75)

        entry_comple = customtkinter.CTkEntry(frame_calculos, border_color="#f0f0f0")
        entry_comple.place(x=255, y=75)

        primer_num = customtkinter.CTkLabel(frame_calculos, text="Primer numero", text_color="#000000",font=("Arial", 22))                
        primer_num.place(x=25, y=10)

        label_real = customtkinter.CTkLabel(frame_calculos, text="Parte Real", text_color="#000000", font=("Arial", 17))    
        label_real.place(x=55, y=48)

        label_comple = customtkinter.CTkLabel(frame_calculos, text="Parte Imaginaria", text_color="#000000",font=("Arial", 17))                                           
        label_comple.place(x=260, y=48)

        segundo_num = customtkinter.CTkLabel(frame_calculos, text="Segundo numero", text_color="#000000",  font=("Arial", 22))
        segundo_num.place(x=25, y=130)

        label_real2 = customtkinter.CTkLabel(frame_calculos, text="Parte Real", text_color="#000000",font=("Arial", 17))
        label_real2.place(x=55, y=168)

        label_comple2 = customtkinter.CTkLabel(frame_calculos, text="Parte Imaginaria", text_color="#000000",font=("Arial", 17))       
        label_comple2.place(x=260, y=168)

        entry_real2 = customtkinter.CTkEntry(frame_calculos, border_color="#f0f0f0")
        entry_real2.place(x=55, y=195)

        entry_comple2 = customtkinter.CTkEntry(frame_calculos, border_color="#f0f0f0")
        entry_comple2.place(x=255, y=195)

        def calcular_suma(operacion):


            a = entry_real.get()
            k = Fraction(a)
            b = entry_comple.get()
            j = Fraction(b)
            c = entry_real2.get()
            h = Fraction(c)
            d = entry_comple2.get()
            g = Fraction(d)
            m = k + j * 1j
            n = h + g * 1j
            if operacion == "suma":
                result = np.sum(m + n)
            elif operacion == "resta":
                result = np.sum(m - n)
            elif operacion == "multiplicacion":
                result = np.multiply(m, n)
            elif operacion == "division":
                result = np.divide(m, n)
            parte_real = Fraction(result.real).limit_denominator()
            parte_imaginaria = Fraction(result.imag).limit_denominator()
            resultado = f"{parte_real} +{parte_imaginaria}i" if parte_imaginaria > 0 else f"{parte_real} {parte_imaginaria}i"
            label_result = customtkinter.CTkLabel(frame_calculos, text=f"El resultado de su Operacion es : \n {resultado}", text_color="#000000", font=("Arial", 20))
            label_result.place(x=80, y=360)

        boton_calcular=customtkinter.CTkButton(frame_calculos,text="Calcular Suma",fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF",command=lambda:calcular_suma("suma"),width=100)
        boton_calcular.place(x=25,y=280)
        boton_calcular1=customtkinter.CTkButton(frame_calculos,text="Calcular Resta",fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF",command=lambda:calcular_suma("resta"),width=100)
        boton_calcular1.place(x=165,y=280)
        boton_calcular2=customtkinter.CTkButton(frame_calculos,text="Calcular Multiplicacion",fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF",command=lambda:calcular_suma("multiplicacion"),width=80)
        boton_calcular2.place(x=300,y=280)
        boton_calcular3=customtkinter.CTkButton(frame_calculos,text="Calcular Division",fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF",command=lambda:calcular_suma("division"),width=100)
        boton_calcular3.place(x=160,y=320)


    def convercion():

            
        frame_calculos.pack_forget()
        
        frame_calculos1.pack(pady=10, padx= 15, fill= "both", expand= True)

        a.geometry("500x570")

        def polar():
            
            label=customtkinter.CTkLabel(master=frame_calculos1,text="Representacion polar- > r ( cosθ + sinθ i )",text_color="#000000",font=("Arial",20))
            label.place(x=50,y=105)

            r=customtkinter.CTkLabel(master=frame_calculos1,text="R =",text_color="#000000",font=("Arial",18))
            r.place(x=90,y=145) 

            entry_r=customtkinter.CTkEntry(master=frame_calculos1,border_color="#f0f0f0",width=40)
            entry_r.place(x=120, y=145)

            theta=customtkinter.CTkLabel(master=frame_calculos1,text="θ =",text_color="#000000",font=("Arial",18)) 
            theta.place(x=270,y=145)

            entry_theta=customtkinter.CTkEntry(master=frame_calculos1,border_color="#f0f0f0",width=40)
            entry_theta.place(x=300, y=145)

            label_forma=customtkinter.CTkLabel(frame_calculos1,text="¿A que forma quiere convertirlo?",text_color="#000000",font=("Arial",20))
            label_forma.place(x=70, y=200)
            
            
            def polar_binomica():
                   
                k=entry_r.get()
                g=Fraction(k)
                l=entry_theta.get()
                d=Fraction(l)
                g=float(g)
                d=float(d)
                q=("{:.2f}".format(g*cos(d)))
                w=("{:.2f}".format(g*sin(d)))
                a= (Fraction(q).limit_denominator())
                b= Fraction(w).limit_denominator()

                resultado = f"{(a)} {b}i" if b<0 else f"{a} +{b}i" 
                
                etiqueta_resultado = customtkinter.CTkLabel(frame_calculos1, text=f"El resultado es : \n {(resultado)}",font=("Arial",19),text_color="#000000")
                etiqueta_resultado.place(x=145, y=310)

            def polar_cartesiana():

                
                
                k=entry_r.get()
                g=Fraction(k)
                l=entry_theta.get()
                d=Fraction(l)
                g=float(g)
                d=float(d)
                q=("{:.2f}".format(g*cos(d)))
                w=("{:.2f}".format(g*sin(d)))
                a= (Fraction(q).limit_denominator())
                b= Fraction(w).limit_denominator()

                resultado = f"({(a)} , {b}i)" if b<0 else f"({a} , +{b}i)" 
                
                etiqueta_resultado = customtkinter.CTkLabel(frame_calculos1, text=f"El resultado es : \n {(resultado)}",font=("Arial",19),text_color="#000000") 
                etiqueta_resultado.place(x=145, y=310)

            def polar_exponcial():
                k=entry_r.get()
                g=Fraction(k)
                l=entry_theta.get()
                d=Fraction(l)


                resultado = f"{g}e^{d}i"
                
                etiqueta_resultado = customtkinter.CTkLabel(frame_calculos1, text=f"El resultado es : \n {(resultado)}",font=("Arial",19),text_color="#000000")
                etiqueta_resultado.place(x=160, y=310)

            
    

            boton_polar_binomica=customtkinter.CTkButton(frame_calculos1,text="Forma Binomica",command=polar_binomica,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_polar_binomica.place(x=15,y=240)

            boton_polar_exponencial=customtkinter.CTkButton(frame_calculos1,text="Forma Exponencial",command=polar_exponcial,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_polar_exponencial.place(x=165,y=240)

            boton_polar_carteciana=customtkinter.CTkButton(frame_calculos1,text="Forma Cartesiana",command=polar_cartesiana,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_polar_carteciana.place(x=315,y=240)

        def binomica():
            label=customtkinter.CTkLabel(master=frame_calculos1,text="Representacion Binomica- > a + bi",text_color="#000000",font=("Arial",20))
            label.place(x=50,y=105)

            a=customtkinter.CTkLabel(master=frame_calculos1,text="a =",text_color="#000000",font=("Arial",18))
            a.place(x=90,y=145) 

            entry_a=customtkinter.CTkEntry(master=frame_calculos1,border_color="#f0f0f0",width=40)
            entry_a.place(x=120, y=145)

            b=customtkinter.CTkLabel(master=frame_calculos1,text="b =",text_color="#000000",font=("Arial",18))
            b.place(x=270,y=145) 

            entry_b=customtkinter.CTkEntry(master=frame_calculos1,border_color="#f0f0f0",width=40)
            entry_b.place(x=300, y=145)

            label_forma=customtkinter.CTkLabel(frame_calculos1,text="¿A que forma quiere convertirlo?",text_color="#000000",font=("Arial",20))
            label_forma.place(x=70, y=200)

            def binomica_polar():
                k=entry_a.get()
                g=Fraction(k)
                l=entry_b.get()
                d=Fraction(l)

                r = Fraction("{:.2f}".format(math.sqrt((g**2)+(d**2))))
                theta = Fraction("{:.2f}".format(math.degrees(math.atan(d/g))))

                resultado = f"{r}(cos({theta}) + sin({theta})i)"
                
                etiqueta_resultado = customtkinter.CTkLabel(frame_calculos1, text=f"El resultado es : \n {(resultado)}",font=("Arial",19),text_color="#000000")
                etiqueta_resultado.place(x=40, y=310)

            def binomica_exponencial():
                k=entry_a.get()
                g=Fraction(k)
                l=entry_b.get()
                d=Fraction(l)

                r = Fraction("{:.2f}".format(math.sqrt((g**2)+(d**2))))
                theta = Fraction("{:.2f}".format(math.degrees(math.atan(d/g))))

                resultado = f"{r}e^{theta}i"
                
                etiqueta_resultado = customtkinter.CTkLabel(frame_calculos1, text=f"El resultado es : \n {(resultado)}",font=("Arial",19),text_color="#000000")
                etiqueta_resultado.place(x=140, y=310)

            def binomica_cartesiana():
                k=entry_a.get()
                g=Fraction(k)
                l=entry_b.get()
                d=Fraction(l)



                resultado = f"{g} +{l}i" if d>0 else f"{g}  {l}i"
                
                etiqueta_resultado = customtkinter.CTkLabel(frame_calculos1, text=f"El resultado es : \n {(resultado)}",font=("Arial",19),text_color="#000000")
                etiqueta_resultado.place(x=160, y=310)


            boton_polar_binomica=customtkinter.CTkButton(frame_calculos1,text="Forma Polar",command=binomica_polar,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_polar_binomica.place(x=15,y=240)

            boton_polar_exponencial=customtkinter.CTkButton(frame_calculos1,text="Forma Exponencial",command=binomica_exponencial,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_polar_exponencial.place(x=165,y=240)

            boton_polar_carteciana=customtkinter.CTkButton(frame_calculos1,text="Forma Cartesiana",command=binomica_cartesiana,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_polar_carteciana.place(x=315,y=240)

        def cartesiana():
            label=customtkinter.CTkLabel(master=frame_calculos1,text="Representacion Cartesiana- > a , bi",text_color="#000000",font=("Arial",20))
            label.place(x=50,y=105)

            a=customtkinter.CTkLabel(master=frame_calculos1,text="a =",text_color="#000000",font=("Arial",18))
            a.place(x=90,y=145) 

            entry_a=customtkinter.CTkEntry(master=frame_calculos1,border_color="#f0f0f0",width=40)
            entry_a.place(x=120, y=145)

            b=customtkinter.CTkLabel(master=frame_calculos1,text="b =",text_color="#000000",font=("Arial",18))
            b.place(x=270,y=145) 

            entry_b=customtkinter.CTkEntry(master=frame_calculos1,border_color="#f0f0f0",width=40)
            entry_b.place(x=300, y=145)

            label_forma=customtkinter.CTkLabel(frame_calculos1,text="¿A que forma quiere convertirlo?",text_color="#000000",font=("Arial",20))
            label_forma.place(x=70, y=200)

            def cartesiana_binomica():
                k=entry_a.get()
                g=Fraction(k)
                l=entry_b.get()
                d=Fraction(l)

                resultado = f"{g}  +{l}i" if d>0 else f"{g}  {l}i"
                etiqueta_resultado = customtkinter.CTkLabel(frame_calculos1, text=f"El resultado es : \n {(resultado)}",font=("Arial",19),text_color="#000000")
                etiqueta_resultado.place(x=160, y=310)

            def cartesiana_polar():
                k=entry_a.get()
                g=Fraction(k)
                l=entry_b.get()
                d=Fraction(l)

                r = Fraction("{:.2f}".format(math.sqrt((g**2)+(d**2))))
                theta = Fraction("{:.2f}".format(math.degrees(math.atan(d/g))))

                resultado = f"{r}(cos({theta}) + sin({theta})i)"
                
                etiqueta_resultado = customtkinter.CTkLabel(frame_calculos1, text=f"El resultado es : \n {(resultado)}",font=("Arial",19),text_color="#000000")
                etiqueta_resultado.place(x=40, y=310)
            
            def cartesiana_exponencial():
                k=entry_a.get()
                g=Fraction(k)
                l=entry_b.get()
                d=Fraction(l)

                r = Fraction("{:.2f}".format(math.sqrt((g**2)+(d**2))))
                theta = Fraction("{:.2f}".format(math.degrees(math.atan(d/g))))

                resultado = f"{r}e^{theta}i"
                
                etiqueta_resultado = customtkinter.CTkLabel(frame_calculos1, text=f"El resultado es : \n {(resultado)}",font=("Arial",19),text_color="#000000")
                etiqueta_resultado.place(x=140, y=310)

            boton_polar_binomica=customtkinter.CTkButton(frame_calculos1,text="Forma Polar",command=cartesiana_polar,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_polar_binomica.place(x=15,y=240)

            boton_polar_exponencial=customtkinter.CTkButton(frame_calculos1,text="Forma Exponencial",command=cartesiana_exponencial,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_polar_exponencial.place(x=165,y=240)

            boton_polar_carteciana=customtkinter.CTkButton(frame_calculos1,text="Forma Binomica",command=cartesiana_binomica,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_polar_carteciana.place(x=315,y=240)

        def exponencial():
            label=customtkinter.CTkLabel(master=frame_calculos1,text="Representacion polar- > re^θi",text_color="#000000",font=("Arial",20))
            label.place(x=50,y=105)

            r=customtkinter.CTkLabel(master=frame_calculos1,text="R =",text_color="#000000",font=("Arial",18))
            r.place(x=90,y=145) 

            entry_r=customtkinter.CTkEntry(master=frame_calculos1,border_color="#f0f0f0",width=40)
            entry_r.place(x=120, y=145)

            theta=customtkinter.CTkLabel(master=frame_calculos1,text="θ =",text_color="#000000",font=("Arial",18))
            theta.place(x=270,y=145) 

            entry_theta=customtkinter.CTkEntry(master=frame_calculos1,border_color="#f0f0f0",width=40)
            entry_theta.place(x=300, y=145)

            label_forma=customtkinter.CTkLabel(frame_calculos1,text="¿A que forma quiere convertirlo?",text_color="#000000",font=("Arial",20))
            label_forma.place(x=70, y=200)

            def exponencial_polar():

                k=entry_r.get()
                g=Fraction(k)
                l=entry_theta.get()
                d=Fraction(l)

                resultado =f"{g}(cos({d}) + sin({d})i)"
                etiqueta_resultado = customtkinter.CTkLabel(frame_calculos1, text=f"El resultado es : \n {(resultado)}",font=("Arial",19),text_color="#000000")
                etiqueta_resultado.place(x=140, y=310)

            def exponencial_binomica():
                k=entry_r.get()
                g=Fraction(k)
                l=entry_theta.get()
                d=Fraction(l)
                g=float(g)
                d=float(d)

                a= Fraction("{:.2f}".format(g*cos(d)))
                b= Fraction("{:.2f}".format(g*sin(d)))

                resultado = f"{a} +{b}i"if b>0 else f"{a} {b}"
                etiqueta_resultado = customtkinter.CTkLabel(frame_calculos1, text=f"El resultado es : \n {(resultado)}",font=("Arial",19),text_color="#000000")     
                etiqueta_resultado.place(x=140, y=310)

            def exponencial_cartesiana():
                k=entry_r.get()
                g=Fraction(k)
                l=entry_theta.get()
                d=Fraction(l)
                g=float(g)
                d=float(d)

                a= Fraction("{:.2f}".format(g*cos(d)))
                b= Fraction("{:.2f}".format(g*sin(d)))

                resultado = f"{a} , {b}i"if b>0 else f"{a} , {b}"
                etiqueta_resultado = customtkinter.CTkLabel(frame_calculos1, text=f"El resultado es : \n {(resultado)}",font=("Arial",19),text_color="#000000")
                etiqueta_resultado.place(x=140, y=310)

            boton_polar_binomica=customtkinter.CTkButton(frame_calculos1,text="Forma Polar",command=exponencial_polar,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_polar_binomica.place(x=15,y=240)
            boton_polar_exponencial=customtkinter.CTkButton(frame_calculos1,text="Forma Cartesiana",command=exponencial_cartesiana,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_polar_exponencial.place(x=165,y=240)
            boton_polar_carteciana=customtkinter.CTkButton(frame_calculos1,text="Forma Binomica",command=exponencial_binomica,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
            boton_polar_carteciana.place(x=315,y=240)



        primer_num = customtkinter.CTkLabel(frame_calculos1, text="Eliga la forma en la que esta representado su numero", text_color="#000000",font=("Arial", 18))                                           
        primer_num.place(x=25, y=10)
        boton_polar=customtkinter.CTkButton(master=frame_calculos1,text="Forma polar",command=polar,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF",width=100)
        boton_polar.place(x=10,y=50)
        boton_binomica=customtkinter.CTkButton(master=frame_calculos1,text="Forma Binomica",command=binomica,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF",width=100)
        boton_binomica.place(x=115,y=50)
        boton_cartesiana=customtkinter.CTkButton(master=frame_calculos1,text="Forma Cartesiana",command=cartesiana,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF",width=100)
        boton_cartesiana.place(x=225,y=50)
        boton_exponencial=customtkinter.CTkButton(master=frame_calculos1,text="Forma Exponencial",command=exponencial,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF",width=100) 
        boton_exponencial.place(x=345,y=50)


    a= tk.Tk()
    a.config(bg="#ffffff")
    a.geometry("500x200")
    frame=customtkinter.CTkFrame(master=a,fg_color="#f0f0f0", height=0)
    frame.pack(pady=5, padx= 15, fill= "both", expand= True, )
    label_cal=customtkinter.CTkLabel(master= frame, text="Elige el tipo de Calculo", font=("Arial",27),text_color="#000000")
    label_cal.place(x=90,y=10)
    boton_op=customtkinter.CTkButton(master=frame,text="Operaciones",command=operaciones,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton_op.place(x=240, y= 55)
    boton_conver=customtkinter.CTkButton(master=frame,text="Conversiones",command=convercion,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton_conver.place(x=70, y=55 )

    frame_calculos1=customtkinter.CTkFrame(master=a,fg_color="#f0f0f0", height= 350)
    frame_calculos=customtkinter.CTkFrame(master=a,fg_color="#f0f0f0", height= 350)

    a.resizable(0,0)


ventana =Tk()
ventana.title("J³M Calculator")
ventana.geometry("577x319")
ventana.configure(bg = "#FFFFFF")
frame=customtkinter.CTkFrame(master=ventana,fg_color="#f0f0f0")
frame.pack(pady=20, padx= 20, fill= "both", expand= True)

principal=customtkinter.CTkLabel(master=frame, text="𝙹³𝙼 𝙲𝙰𝙻𝙲𝚄𝙻𝙰𝚃𝙾𝚁", font=("Doble struck",34),text_color="black" )
principal.pack( pady= 12, padx= 10)

boton1=customtkinter.CTkButton(master=frame, text="Calculadora", command = calculadora, fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
boton1.place(x=370, y=95,)

boton2=customtkinter.CTkButton(master=frame, text="Matrices", command= sistemas_de_ecuaciones,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
boton2.place(x=370, y=165,)

boton3=customtkinter.CTkButton(master=frame, text="Integrales", command= integrales,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF" )
boton3.place(x=370, y=200,)

boton4=customtkinter.CTkButton(master=frame, text="Derivadas", command=derivar,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
boton4.place(x=370, y=130,)

boton5=customtkinter.CTkButton(master=frame, text="Operaciones con Complejos", command= operacion_con_complejos,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
boton5.place(x=340, y=235,)

boton6=customtkinter.CTkButton(master=frame, text="Graficar", command= grafica,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
boton6.place(x=370, y=60,)

i = PhotoImage(file="imagen.png")
i.configure( )
l = tk.Label(frame, image=i)
l.place(relx=0.09, rely=0.45,relheight=.45,relwidth=.45)

ventana.resizable(0,0)
def confirmar():
                ans = askyesno(title="Salir", message= '¿Deseas salir?')
                if ans:
                    ventana.destroy()

ventana.protocol('WM_DELETE_WINDOW', confirmar)
a= PhotoImage (file="ae.ico")
ventana.iconphoto(True,a)
ventana.mainloop()