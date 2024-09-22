from librerias import *

class Botones:
    def configurar_botones(self):
        self.opciones_boton = {
            "fg_color": "#a3d9f3",
            "text_color": "black",
            "hover_color": "#FFFFFF",
            "border_color": "#f0f0f0"
        }
        
class op_inmaginarios(Botones):
    def __init__(self,inter):
        self.inter =Toplevel(inter)
        self.inter.config(bg="#ffffff")
        self.inter.geometry("500x200")
        self.frame=ctk.CTkFrame(master=self.inter,fg_color="#f0f0f0", height=0)
        self.frame.pack(pady=10, padx= 15, fill= "both", expand= True, )
        self.configurar_botones()
        self.entradas()
        self.inter.resizable(0,0)
        
    def entradas(self):    
        label_cal=ctk.CTkLabel(master= self.frame, text="Elige el tipo de Calculo", font=("Arial",27),text_color="#000000")
        label_cal.place(x=90,y=10)
        boton_op=ctk.CTkButton(master=self.frame,text="Operaciones",**self.opciones_boton)
        boton_op.place(x=240, y= 55)
        boton_conver=ctk.CTkButton(master=self.frame,text="Conversiones",command=self.opraciones,**self.opciones_boton)
        boton_conver.place(x=70, y=55 )

        self.frame_calculos1=ctk.CTkFrame(master=self.frame,fg_color="#f0f0f0", height= 350)
        self.frame_calculos=ctk.CTkFrame(master=self.frame,fg_color="#f0f0f0", height= 350)
        
    def opraciones(self):    
        self.frame_calculos1.pack_forget()
        self.frame_calculos.pack(pady=10, padx= 15, fill= "both", expand= True) 
        self.inter.geometry("500x600")
        
        entry_real = ctk.CTkEntry(self.frame_calculos, border_color="#f0f0f0")
        entry_real.place(x=50, y=75)
        entry_comple = ctk.CTkEntry(self.frame_calculos, border_color="#f0f0f0")
        entry_comple.place(x=255, y=75)
        primer_num = ctk.CTkLabel(self.frame_calculos, text="Primer numero", text_color="#000000",font=("Arial", 22))                
        primer_num.place(x=25, y=10)
        label_real = ctk.CTkLabel(self.frame_calculos, text="Parte Real", text_color="#000000", font=("Arial", 17))    
        label_real.place(x=55, y=48)
        label_comple = ctk.CTkLabel(self.frame_calculos, text="Parte Imaginaria", text_color="#000000",font=("Arial", 17))                                           
        label_comple.place(x=260, y=48)
        segundo_num = ctk.CTkLabel(self.frame_calculos, text="Segundo numero", text_color="#000000",  font=("Arial", 22))
        segundo_num.place(x=25, y=130)
        label_real2 = ctk.CTkLabel(self.frame_calculos, text="Parte Real", text_color="#000000",font=("Arial", 17))
        label_real2.place(x=55, y=168)
        label_comple2 = ctk.CTkLabel(self.frame_calculos, text="Parte Imaginaria", text_color="#000000",font=("Arial", 17))       
        label_comple2.place(x=260, y=168)
        entry_real2 = ctk.CTkEntry(self.frame_calculos, border_color="#f0f0f0")
        entry_real2.place(x=55, y=195)
        entry_comple2 = ctk.CTkEntry(self.frame_calculos, border_color="#f0f0f0")
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
            label_result = ctk.CTkLabel(self.frame_calculos, text=f"El resultado de su Operacion es : \n {resultado}", text_color="#000000", font=("Arial", 20))
            label_result.place(x=80, y=360)
       
        boton_calcular=ctk.CTkButton(self.frame_calculos,text="Calcular Suma",fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF",command=lambda:calcular_suma("suma"),width=100)
        boton_calcular.place(x=25,y=280)
        boton_calcular1=ctk.CTkButton(self.frame_calculos,text="Calcular Resta",fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF",command=lambda:calcular_suma("resta"),width=100)
        boton_calcular1.place(x=165,y=280)
        boton_calcular2=ctk.CTkButton(self.frame_calculos,text="Calcular Multiplicacion",fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF",command=lambda:calcular_suma("multiplicacion"),width=80)
        boton_calcular2.place(x=300,y=280)
        boton_calcular3=ctk.CTkButton(self.frame_calculos,text="Calcular Division",fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF",command=lambda:calcular_suma("division"),width=100)
        boton_calcular3.place(x=160,y=320)



            
class integrales(Botones):
    def __init__(self, inter1):
        self.inter = Toplevel(inter1)
        self.inter.config(bg="#ffffff")
        self.inter.geometry("500x400")  
        self.inter.minsize(500, 150) 
        self.frame0=ctk.CTkFrame(master=self.inter,fg_color="#f0f0f0")
        self.frame0.pack(pady=20, padx= 20, fill= "both", expand= True)
        self.configurar_botones()
        self.entradas()
        
    def entradas(self):
        self.lim_supe=ctk.CTkEntry(master=self.frame0,width=30,height=20,border_color="#f0f0f0",fg_color="#ffffff",text_color="#000000")
        self.lim_supe.place(x=120,y=110)

        self.lim_inf=ctk.CTkEntry(master=self.frame0,width=30,height=20,border_color="#f0f0f0",fg_color="#ffffff",text_color="#000000")
        self.lim_inf.place(x=120,y=160)
        
        self.funcion=ctk.CTkEntry(self.frame0,border_color="#f0f0f0",fg_color="#ffffff",text_color="#000000")
        self.funcion.place(x=150,y=129)

        dx_c=ctk.CTkLabel(self.frame0,text=f"dx ",font=("Arial",30),text_color="#000000")
        dx_c.place(x=300,y=129)
        titulo=ctk.CTkLabel(master=self.frame0,text="∫", font=("Arial",60),text_color="#000000")
        titulo.place(x=100,y=120)
        titulo1=ctk.CTkLabel(master=self.frame0,text="Calcule su Integral definida o indefinida",font=("Arial",25),text_color="#000000")
        titulo1.pack(pady=20) 
        
        integrar=ctk.CTkButton(self.frame0,text="Integrar la Funcion",command=self.calculado,**self.opciones_boton)
        integrar.place(x=160,y=200)
        
        self.resultado=None

    def calculado(self):
        x = symbols('x')
        funcion1=self.funcion.get()
        
        if self.resultado:
            self.resultado.destroy() 
            
        if self.lim_inf.get()=="" or self.lim_supe.get() == "":
            try:
                integral_indefinida1 = integrate(funcion1, x)
                integral_definida0 = f"{simplify(integral_indefinida1)} + C"
                self.integral_definida2=str(integral_definida0).replace('log', 'ln')
            except Exception as e:
                self.resultado = ctk.CTkLabel(self.frame0, text=f"Error: {str(e)}", text_color="#FF0000", font=("Arial", 25))
                self.resultado.place(x=60, y=260)

        else:  
            
            lim_inf1=self.lim_inf.get()
            lim_supe1=self.lim_supe.get()

            lim_inf2=Fraction(lim_inf1)
            lim_supe2=Fraction(lim_supe1)
            
            integral_definida1 = integrate(funcion1, (x, lim_inf2, lim_supe2))
            self.integral_definida2=str(integral_definida1).replace('log', 'ln')

        self.resultado=ctk.CTkLabel(self.frame0,text=f"El resultado de su integral es:\n {sp.pretty(self.integral_definida2)}",text_color="#000000",font=("Arial",25))
        self.resultado.place(x=60,y=260)

class Derivadas (Botones):
    def __init__(self, inter1):
        self.inter = Toplevel(inter1)
        self.inter.config(bg="#ffffff")
        self.inter.geometry("500x150")  
        self.inter.minsize(500, 150) 

        self.configurar_botones()

        self.frame = ctk.CTkFrame(master=self.inter, fg_color="#f0f0f0", height= 100, width=500)
        self.frame.grid(row=0, column=0, sticky="nsew", padx=15, pady=5,)        
        
        self.inter.grid_rowconfigure(1, weight=1) 
        self.inter.grid_rowconfigure(0, weight=5)  
        self.inter.grid_columnconfigure(0, weight=1)  

        self.label_cal = ctk.CTkLabel(master=self.frame, text="Elige el tipo de Calculo", font=("Arial", 27), text_color="#000000")
        self.label_cal.grid(row=0, column=1, columnspan=2, pady=10,padx=100, sticky="n") 
        self.boton_op = ctk.CTkButton(master=self.frame, text="Implicita", command=self.implicita, **self.opciones_boton)
        self.boton_op.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

        self.boton_conver = ctk.CTkButton(master=self.frame, text="Orden Superior",command=self.orde_supe, **self.opciones_boton)
        self.boton_conver.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.frame_calculos1 = ctk.CTkFrame(master=self.inter, fg_color="#f0f0f0", height=350)        
        self.frame_calculos = ctk.CTkFrame(master=self.inter, fg_color="#f0f0f0", height=350)
        
       

    def implicita(self):
        self.inter.grid_rowconfigure(0, weight=1) 
        self.inter.grid_rowconfigure(1, weight=5)
        self.frame_calculos1.grid_remove()  
        self.frame_calculos.grid(row=1, column=0, sticky="nsew", padx=15, pady=10) 
        self.inter.geometry("500x400")  

        x, y = sp.symbols('x y')
        eqn_original = ctk.CTkEntry(master=self.frame_calculos, bg_color="#FFFFFF")
        eqn_original.grid(row=3, column=0, columnspan=2, pady=10, padx=40, sticky="ew")

        eqn_label = ctk.CTkLabel(self.frame_calculos, text="Ingrese la ecuación implícita", text_color="black", font=("Arial", 20))
        eqn_label.grid(row=2, column=1, padx=100, sticky="w")

        titulo = ctk.CTkLabel(master=self.frame_calculos, text="Calcula la Derivada Implícita", text_color="black", font=("Doble struck", 28))
        titulo.grid(row=0, column=0, columnspan=2, pady=20)

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
                    derivada_implicita_str = str(derivada_implicita).replace('log', 'ln')
                    etiqueta_resultado = tk.Label(self.frame_calculos, text=f"La derivada implícita de la ecuación {eqn} es: \n{sp.simplify(derivada_implicita_str)}", fg="black", font=("Doble struck", 15))
                    etiqueta_resultado.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
                except (sp.SympifyError, ValueError) as e:
                    etiqueta_resultado = ctk.CTkLabel(self.frame_calculos, text=f"Error: {e}", text_color="black")
                    etiqueta_resultado.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
            else:
                etiqueta_resultado = ctk.CTkLabel(self.frame_calculos, text="Por favor, ingrese una ecuación válida.", text_color="black")
                etiqueta_resultado.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        boton_calcular = ctk.CTkButton(master=self.frame_calculos, text="Calcular Derivada Implícita", command=calcular, **self.opciones_boton)
        boton_calcular.grid(row=4, column=0, columnspan=2, pady=10)
    def orde_supe(self):
        self.inter.grid_rowconfigure(0, weight=1) 
        self.inter.grid_rowconfigure(1, weight=5)
        self.frame_calculos.grid_remove()  
        self.frame_calculos1.grid(row=1, column=0, sticky="nsew", padx=15, pady=10) 
        self.inter.geometry("500x400")
        x = sp.symbols('x')
        eqn_original = ctk.CTkEntry(master=self.frame_calculos1, bg_color="#FFFFFF")
        eqn_original.grid(row=3, column=0, columnspan=2, pady=10, padx=40, sticky="ew")

        eqn_label = ctk.CTkLabel(self.frame_calculos1, text="Ingrese la ecuación y el orden separado por coma", text_color="black", font=("Arial", 20))
        eqn_label.grid(row=2, column=1, padx=20, sticky="w",)

        titulo = ctk.CTkLabel(master=self.frame_calculos1, text="Calcula la Derivada ", text_color="black", font=("Doble struck", 28))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        etiqueta_resultado = None

        def calcular():
            nonlocal etiqueta_resultado
            if etiqueta_resultado:
                etiqueta_resultado.destroy()

            eqn = eqn_original.get()

            if eqn:
                try:
                    #
                    eqn_parts = eqn.split(',')
                    if len(eqn_parts) != 2:
                        raise ValueError("Por favor, ingrese una ecuación y un orden separado por una coma.")

                    
                    eq = eqn_parts[0].strip()
                    orden = int(eqn_parts[1].strip())      
                    
                    derivada = sp.diff(eq, x, orden)
                    derivada_str = str(derivada).replace('log', 'ln')

                    etiqueta_resultado = tk.Label(self.frame_calculos1, text=f"La derivada de orden {orden} de la ecuación {eqn_parts[0]} es: \n{(derivada_str)}", fg="black", font=("Doble struck", 15))
                    etiqueta_resultado.grid(row=6, column=0, columnspan=2, pady=10, padx=10)
                except (sp.SympifyError, ValueError) as e:
                    etiqueta_resultado = ctk.CTkLabel(self.frame_calculos1, text=f"Error: {e}", text_color="black")
                    etiqueta_resultado.grid(row=6, column=0, columnspan=2, pady=10, padx=10)
            else:
                etiqueta_resultado = ctk.CTkLabel(self.frame_calculos1, text="Por favor, ingrese una ecuación válida.", text_color="black")
                etiqueta_resultado.grid(row=6, column=0, columnspan=2, pady=10, padx=10)
        boton_calcular = ctk.CTkButton(master=self.frame_calculos1, text="Calcular Derivada", command=calcular, **self.opciones_boton)
        boton_calcular.grid(row=5, column=0, columnspan=2, pady=10)

        
class MatrixOperations(Botones):
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.config(bg="#ffffff")
        self.rows = None
        self.cols = None
        self.entries = None
        self.result_entries = None
        self.error_label = None
        self.dim_frame = ctk.CTkFrame(self.root, fg_color="#f0f0f0")
        self.dim_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.matrix_frame = ctk.CTkFrame(self.root, fg_color="#f0f0f0")
        self.configurar_botones()
        self.create_matrix_entries()

    def create_matrix_entries(self):
        def validate_entries():
            try:
                self.rows = int(rows_entry.get())
                self.cols = int(cols_entry.get())
                self.error_label.configure(text="")
                self.generate_matrix_entries()
            except ValueError:
                self.error_label.configure(text="Ingrese bien los datos")

        rows_label = ctk.CTkLabel(self.dim_frame, text="Número de filas: ", text_color="#000000")
        rows_label.grid(row=0, column=0, padx=5, pady=5)
        rows_entry = ctk.CTkEntry(self.dim_frame, border_color="#f0f0f0")
        rows_entry.grid(row=0, column=1, padx=5, pady=5)

        cols_label = ctk.CTkLabel(self.dim_frame, text="Número de columnas: ", text_color="#000000")
        cols_label.grid(row=1, column=0, padx=5, pady=5)
        cols_entry = ctk.CTkEntry(self.dim_frame, border_color="#f0f0f0")
        cols_entry.grid(row=1, column=1, padx=5, pady=5)

        generate_button = ctk.CTkButton(self.dim_frame, text="Generar Matriz", command=validate_entries, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        generate_button.grid(row=2, columnspan=2, pady=10)

        self.error_label = ctk.CTkLabel(self.dim_frame, text="", text_color="#000000")
        self.error_label.grid(row=3, columnspan=2, pady=5)

    def generate_matrix_entries(self):
        self.matrix_frame.pack(pady=20, padx=20, fill="both", expand=True)

        if self.entries:
            for row in self.entries:
                for entry in row:
                    entry.destroy()
            for entry in self.result_entries:
                entry.destroy()
                self.boton_determinante.destroy()
                self.boton_inversa.destroy()
                self.boton_transpuesta.destroy()
                self.solve_button.destroy()

        self.entries = []
        self.result_entries = []

        for r in range(self.rows):
            row_entries = []
            for c in range(self.cols):
                entry = ctk.CTkEntry(self.matrix_frame, width=60, height=30, border_color="#f0f0f0")
                entry.grid(row=r, column=c, padx=10, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

            vector_label = ctk.CTkLabel(self.matrix_frame, text="|", text_color="#000000")
            vector_label.grid(row=r, column=self.cols, padx=10, pady=5)

            result_entry = ctk.CTkEntry(self.matrix_frame, width=90, height=30, border_color="#f0f0f0")
            result_entry.grid(row=r, column=self.cols + 1, padx=10, pady=5)
            self.result_entries.append(result_entry)
            
        self.create_buttons()

    def create_buttons(self):
         
        self.solve_button = ctk.CTkButton(self.dim_frame, text="Resolver Matriz", command=self.solve_matrix, **self.opciones_boton)
        self.solve_button.grid(row=0, columnspan=self.cols + 1, padx=5, column=self.cols + 1)

        self.boton_inversa = ctk.CTkButton(self.dim_frame, text="Resolver Inversa", command=self.solve_inverse, **self.opciones_boton)
        self.boton_inversa.grid(row=1, columnspan=self.cols + 1, padx=20, column=self.cols + 1)

        self.boton_transpuesta = ctk.CTkButton(self.dim_frame, text="Resolver Transpuesta", command=self.solve_transpose, **self.opciones_boton)
        self.boton_transpuesta.grid(row=2, columnspan=self.cols + 1, padx=20, column=self.cols + 1)

        self.boton_determinante = ctk.CTkButton(self.dim_frame, text="Resolver Determinante", command=self.solve_determinant, **self.opciones_boton)
        self.boton_determinante.grid(row=3, columnspan=self.cols + 1, padx=20, column=self.cols + 1)
        

    def get_matrix(self):
        matrix = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                try:
                    value = Fraction(self.entries[i][j].get())
                except ValueError:
                    self.error_label.configure(text="Ingrese números válidos")
                    return None
                row.append(value)
            matrix.append(row)
        return matrix
    
    def get_vector(self):
        vector = []
        for i in range(self.rows):
            try:
                value = Fraction(self.result_entries[i].get())
            except ValueError:
                self.error_label.configure(text="Ingrese números válidos")
                return None
            vector.append(value)

        return vector

    def solve_matrix(self):
        matrix, vector = self.get_matrix(),self.get_vector()
        if not matrix or not vector:
            return

        A = np.array(matrix, dtype=object)
        b = np.array(vector, dtype=object)

        try:
            x = np.linalg.solve(A.astype(float), b.astype(float))
            x_fracciones = [f"{Fraction(num).limit_denominator()}" for num in x]
            x_resultado = "  ~  ".join(x_fracciones)

            self.show_result(f"La solución del sistema de ecuaciones es:\n{x_resultado}")
        except np.linalg.LinAlgError:
            self.show_error("El sistema de ecuaciones no tiene solución o tiene infinitas soluciones.")

    def solve_inverse(self):
        matrix= self.get_matrix()
        if not matrix:
            return

        A = np.array(matrix, dtype=float)

        if A.shape[0] != A.shape[1]:
            self.show_error("La matriz no es cuadrada, por lo que no tiene inversa.")
            return

        if np.linalg.det(A) == 0:
            self.show_error("La matriz es singular y no tiene inversa.")
            return

        inversa = np.linalg.inv(A)
        inversa_fracciones = [[Fraction(num).limit_denominator() for num in row] for row in inversa]
        inversa_resultado = "\n".join(["\t".join(map(str, row)) for row in inversa_fracciones])

        self.show_result(f"La matriz inversa es:\n{inversa_resultado}")

    def solve_transpose(self):
        matrix = self.get_matrix()
        if not matrix:
            return

        A = np.array(matrix, dtype=object)
        matriz_transpuesta = np.transpose(A.astype(float))

        matriz_cadenas = [[Fraction(num).limit_denominator() for num in row] for row in matriz_transpuesta]
        cadena_matriz = "\n".join(["\t".join(map(str, row)) for row in matriz_cadenas])

        self.show_result(f"La transpuesta de su matriz es:\n{cadena_matriz}")

    def solve_determinant(self):
        matrix= self.get_matrix()
        if not matrix:
            return

        A = np.array(matrix, dtype=object)
        determinante = np.linalg.det(A.astype(float))
        det = Fraction(determinante).limit_denominator()

        self.show_result(f"El determinante de la matriz ingresada es:\n{det}")

    def show_result(self, message):
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="#ffffff")
        frame = ctk.CTkFrame(master=ventana_resultado, fg_color="#f0f0f0")
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        etiqueta_resultado = ctk.CTkLabel(frame, text=message, text_color="#000000")
        etiqueta_resultado.pack(padx=20, pady=20)

    def show_error(self, message):
        ventana_error = Toplevel()
        ventana_error.title("Error")
        ventana_error.config(bg="#ffffff")
        frame = ctk.CTkFrame(master=ventana_error, fg_color="#f0f0f0")
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        etiqueta_error = ctk.CTkLabel(frame, text=message, text_color="#000000")
        etiqueta_error.pack(padx=20, pady=20)




