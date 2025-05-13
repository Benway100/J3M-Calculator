from reescribir import *
class Calculadora(Botones):
    def __init__(self,inter):
        self.root1 = Toplevel(inter)
        self.root1.title("Calculadora")
        self.root1.geometry("500x500")
        self.root1.columnconfigure(0, weight=1)
        self.root1.rowconfigure(0, weight=1)
        self.root1.config(bg="#ffffff")

        self.root = ctk.CTkFrame(self.root1, fg_color="#f0f0f0")
        self.root.pack(pady=7, padx=15, fill="both", expand=True)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.columnconfigure(5, weight=1)
        self.root.columnconfigure(6, weight=1)

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=1)
        self.root.rowconfigure(8, weight=1)
        
        self.entrada1 = StringVar()
        self.label_entrada1 = ttk.Label(self.root, textvariable=self.entrada1, anchor= "e", font="80",foreground="#000000")
        self.label_entrada1.grid(row=0, column=0, columnspan=8, sticky=(W,N,E,S))

        self.entrada2 = StringVar()
        self.label_entrada2 = ttk.Label(self.root, textvariable=self.entrada2, anchor= "e", font="100",foreground="#000000")
        self.label_entrada2.grid(row=1, column=0, columnspan=8, sticky=(W,N,E,S))
        self.botones_calcu()
        
    def botones_calcu(self):
        button0 = ctk.CTkButton(self.root, text="0", command=lambda: self.ingresarValores('0'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button1 = ctk.CTkButton(self.root, text="1", command=lambda: self.ingresarValores('1'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button2 = ctk.CTkButton(self.root, text="2", command=lambda: self.ingresarValores('2'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button3 = ctk.CTkButton(self.root, text="3", command=lambda: self.ingresarValores('3'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button4 = ctk.CTkButton(self.root, text="4", command=lambda: self.ingresarValores('4'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button5 = ctk.CTkButton(self.root, text="5", command=lambda: self.ingresarValores('5'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button6 = ctk.CTkButton(self.root, text="6", command=lambda: self.ingresarValores('6'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button7 = ctk.CTkButton(self.root, text="7", command=lambda: self.ingresarValores('7'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button8 = ctk.CTkButton(self.root, text="8", command=lambda: self.ingresarValores('8'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button9 = ctk.CTkButton(self.root, text="9", command=lambda: self.ingresarValores('9'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_aleatorio = ctk.CTkButton(self.root, text='Al',command=lambda: self.aleatorio(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_borrar = ctk.CTkButton(self.root, text=chr(9003), command=lambda: self.borrar(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_borrar_todo = ctk.CTkButton(self.root, text="C", command=lambda:self.borrartodo(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_parentesis1 = ctk.CTkButton(self.root, text="(", command=lambda: self.ingresarValores('('),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_parentesis2 = ctk.CTkButton(self.root, text=")", command=lambda: self.ingresarValores(')'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_punto = ctk.CTkButton(self.root, text=".", command=lambda: self.ingresarValores('.'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_pi = ctk.CTkButton(self.root, text='π', command=lambda: pi(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_aureo = ctk.CTkButton(self.root, text= 'φ', command=lambda: self.numero_aureo(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_division = ctk.CTkButton(self.root, text=chr(247), command=lambda: self.ingresarValores('/'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_multiplicacion = ctk.CTkButton(self.root, text="x", command=lambda: self.ingresarValores('*'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_resta = ctk.CTkButton(self.root, text="-", command=lambda: self.ingresarValores('-'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_suma = ctk.CTkButton(self.root, text="+", command=lambda: self.ingresarValores('+'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_sen = ctk.CTkButton(self.root, text= 'sen(θ)', command=lambda: self.sen(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_igual = ctk.CTkButton(self.root, text="=", command=lambda: self.ingresarValores("="),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_raiz_cuadrada = ctk.CTkButton(self.root, text="√", command=lambda:self.raiz_cuadrada(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_cos = ctk.CTkButton(self.root, text= 'cos(θ)', command=lambda: self.coss(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_tan = ctk.CTkButton(self.root, text= 'tan(θ)', command=lambda: self.tann(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_cot = ctk.CTkButton(self.root, text= 'ctan(θ)',command=lambda: self.cotan(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_sec = ctk.CTkButton(self.root, text= 'sec(θ)', command=lambda: self.sec(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_csc = ctk.CTkButton(self.root, text= 'csc(θ)', command=lambda: self.csc(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_arcsen = ctk.CTkButton(self.root, text= 'arsen(θ)', command=lambda: self.asen(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_arccos = ctk.CTkButton(self.root, text= 'arccos(θ)', command=lambda: acos(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_abs = ctk.CTkButton(self.root, text= '|x|', command=lambda: self.absoluto(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_potencia = ctk.CTkButton(self.root, text= '^' , command=lambda:self.ingresarValores('**'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_logaritmo10 = ctk.CTkButton(self.root, text= 'Log10', command=lambda:self.log10n(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_redon = ctk.CTkButton(self.root, text='Redon', command=lambda:self.redon(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_mod = ctk.CTkButton(self.root, text='Mod', command=lambda: self.ingresarValores('Mod',fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF"),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_div = ctk.CTkButton(self.root, text='Div', command=lambda:self.ingresarValores('Div'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        button_euler = ctk.CTkButton(self.root, text="e", command=lambda: self.euler(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")

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
        
                
        for child in self.root.winfo_children():
            child.grid_configure(ipady=10, padx=1, pady=1)
        
        self.root1.resizable(0,0)
            
    def ingresarValores(self,tecla):
        if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.' or tecla == '**':
            self.entrada2.set(self.entrada2.get() + tecla)
        if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-' or tecla == 'Mod' or tecla == 'Div':
            if tecla == '*':
                self.entrada1.set(self.entrada2.get() + '*')
            elif tecla == '/':
                self.entrada1.set(self.entrada2.get() + '/')
            elif tecla == '+':
                self.entrada1.set(self.entrada2.get() + '+')
            elif tecla == '-':
                self.entrada1.set(self.entrada2.get() + '-')
            elif tecla == '**':
                self.entrada1.set(self.entrada2.get() + '**' ) 
            elif tecla == 'Mod':
                self.entrada1.set(self.entrada2.get() + '%')
            elif tecla == 'Div':
                self.entrada1.set(self.entrada2.get() + '//')
            self.entrada2.set('')
        if tecla == "=":
            self.entrada1.set(self.entrada1.get() + self.entrada2.get())
            resultado = eval(self.entrada1.get())
            self.entrada2.set(resultado)


    def euler(self):
        self.entrada1.set('')
        resultado = math.e
        self.entrada2.set(resultado)
    def redon(self):
        self.entrada1.set('')
        resultado = round(float(self.entrada2.get()))
        self.entrada2.set(resultado)
    def raiz_cuadrada(self):
        self.entrada1.set('')
        resultado = math.sqrt(float(self.entrada2.get()))
        self.entrada2.set(resultado)    
    def pi(self):

        self.entrada1.set('')
        resultado = math.pi
        self.entrada2.set(resultado)
    def log10n(self):
        self.entrada1.set('')
        resultado = log10(float(self.entrada2.get()))
        self.entrada2.set(resultado)

    def numero_aureo(self):
        self.entrada1.set('')
        resultado  = (1 + math.sqrt(5)) / 2
        self.entrada2.set(resultado)
    def sen(self):
        self.entrada1.set('')
        resultado = sin(((float(self.entrada2.get())) * math.pi)/180)
        if resultado < 1e-15 and resultado > 0 or resultado < 0 and resultado > -1e-10:
            resultado = 0.0

        self.entrada2.set(resultado)
    def coss(self):
        self.entrada1.set('')
        resultado = cos((((float(self.entrada2.get())) * math.pi)/180))
        if abs(resultado) < 1e-15:
            resultado = 0.0
        self.entrada2.set(resultado)
    def tann(self):
        self.entrada1.set('')
        resultado = tan(((float(self.entrada2.get())) * math.pi)/180)
        if abs(resultado) > 1e15:
            resultado = 'Indefinido'
        elif resultado < 1e-15 and resultado > 0 or resultado < 0 and resultado > -1e-10:
            resultado = 0.0
        self.entrada2.set(resultado)
        
    def cotan(self):
        self.entrada1.set('')
        
        resultado = 1/(tan(((float(self.entrada2.get())) * math.pi)/180))

        if abs(resultado) < 1e-15:
            resultado = 0.0
        elif abs(resultado) >= 2*math.pi:
            resultado = 'Indefinido'
        self.entrada2.set(resultado)
        
    def sec(self):
        self.entrada1.set('')
        resultado = 1/(cos(((float(self.entrada2.get())) * math.pi)/180))
        if abs(resultado) < 1e-15:
            resultado = 0.0
        elif abs(resultado) > 1e15:
            resultado = 'Indefinido'
        self.entrada2.set(resultado)
    def csc(self):
        
        self.entrada1.set('')
        resultado = 1/(sin(((float(self.entrada2.get())) * math.pi)/180))
        if abs(resultado) < 1e-15:
            resultado = 0.0
        elif abs(resultado) > 1e15:
            resultado = 'Indefinido'
        self.entrada2.set(resultado)
        
    def asen(self):
        self.entrada1.set('') 
        valor_ingresado = float(self.entrada2.get())  
        resultado = degrees(arcsin(valor_ingresado)) 
        if valor_ingresado >= -1 and valor_ingresado <= 1: 
            if abs(resultado) < 1e-15:
                resultado = 0.0
        elif abs(resultado) > 1e15:
            resultado = 'Indefinido'
        else:
            resultado = 'Fuera de rango' 

        self.entrada2.set(resultado) 
    
    def acos(self):
        valor_ingresado = float(self.entrada2.get())
    
        if valor_ingresado >= -1 and valor_ingresado <= 1:
            resultado_radianes = arccos(valor_ingresado)
            resultado_grados = degrees(resultado_radianes)
        else:
            resultado_grados = 'Fuera de rango'

        self.entrada2.set(resultado_grados) 

    def absoluto(self):
        self.entrada1.set('')
        resultado = abs(float(self.entrada2.get()))
        self.entrada2.set(resultado)
    def borrar(self):
        inicio = 0
        final = len(self.entrada2.get())

        self.entrada2.set(self.entrada2.get()[inicio:final - 1])
    def borrartodo(self):
        self.entrada1.set('')
        self.entrada2.set('')
    def aleatorio(self):
        numero1 = simpledialog.askinteger("Número 1", "Ingrese el primer número:")
        numero2 = simpledialog.askinteger("Número 2", "Ingrese el segundo número:")
        
    
        if numero1 is not None and numero2 is not None:
            
            numero_aleatorio = random.randint(numero1, numero2)
            
            ventana_resultado = Toplevel(self.root)
            ventana_resultado.geometry('+100+200')
            ventana_resultado.minsize(width=300 ,height= 100)
            ventana_resultado.maxsize(width=300 ,height= 100)
            etiqueta_resultado = tk.Label(ventana_resultado, text=f"Número aleatorio entre {numero1} y {numero2}: {numero_aleatorio}")
            etiqueta_resultado.grid(row=2)
            etiqueta_resultado.pack()
    
    
