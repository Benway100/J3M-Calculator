from reescribir import *
from calculadora import Calculadora

class VentanaPrincipal(Botones):
    def __init__(self, interfaz):
        self.inter = interfaz
        self.inter.geometry("580x320")
        self.inter.title("J³M Calculator")
        self.inter.configure(bg="#FFFFFF")
        self.inter.resizable(0, 0)
        self.frame = ctk.CTkFrame(self.inter, fg_color="#f0f0f0")
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.configurar_botones()
        self.crear_botones()
        self.imagen()
        self.texto()
        self.icono()

    def crear_botones(self):
        ctk.CTkButton(self.frame,text="Calculadora", command=self.abrir_calcu,**self.opciones_boton).place(x=370, y=95)
        ctk.CTkButton(self.frame,text="Matrices", command=self.abrir_matrices, **self.opciones_boton).place(x=370, y=165)
        ctk.CTkButton(self.frame,text="Integrales",command=self.abrir_inte,**self.opciones_boton).place(x=370, y=200)
        ctk.CTkButton(self.frame,text="Derivadas",command=self.abrir_derivadas , **self.opciones_boton).place(x=370, y=130)
        ctk.CTkButton(self.frame,text="Operaciones con Complejos", command=self.abrir_imagi,**self.opciones_boton).place(x=340, y=235)
        ctk.CTkButton(self.frame,text="Graficar", command=self.abrir_grafi,**self.opciones_boton).place(x=370, y=60)

    def calculadora(self):
        Calculadora(self.inter)
    def abrir_matrices(self):
        MatrixOperations(self.inter)
    def abrir_derivadas(self):
        Derivadas(self.inter)
    def abrir_inte(self):
        integrales(self.inter)
    def abrir_imagi(self):
        op_inmaginarios(self.inter)
    def abrir_grafi(self):
        GraficadorFunciones(self.inter)
    def abrir_calcu(self):
        Calculadora(self.inter)
    def imagen(self):
        self.i = PhotoImage(file="imagen.png")
        ctk.CTkLabel(self.frame, image=self.i, text="", fg_color="#f0f0f0").place(relx=0.09, rely=0.45, relheight=0.45, relwidth=0.45)

    def texto(self):
        ctk.CTkLabel(self.frame, text="𝙹³𝙼 𝙲𝙰𝙻𝙲𝚄𝙻𝙰𝚃𝙾𝚁", font=("Doble struck", 34), text_color="black").pack(pady=12, padx=10)

    def icono(self):
        self.a = PhotoImage(file="ae.ico")
        self.inter.iconphoto(True, self.a)

if __name__ == "__main__":
    ob = VentanaPrincipal(Tk())
    ob.inter.mainloop()
