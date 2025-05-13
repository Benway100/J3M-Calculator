import tkinter as tk
import customtkinter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from mpl_toolkits.mplot3d import Axes3D

class GraficadorFunciones:
    def __init__(self, master):
        self.master = master
        self.master.title("Graficador de funciones")
        self.master.config(bg="#ffffff")
        self.master.geometry("500x200")
        
        self.frame = customtkinter.CTkFrame(master=self.master, fg_color="#f0f0f0")
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(self.frame, text="Elige tu forma de gráfica", text_color="black", font=("Arial", 25))
        self.label.pack()

        self.boton_3d = customtkinter.CTkButton(self.frame, text="Gráfica 3D", command=self.grafica3d, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        self.boton_3d.pack(padx=20, pady=20)

        self.boton_2d = customtkinter.CTkButton(self.frame, text="Gráfica 2D", command=self.grafica2d, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        self.boton_2d.pack(padx=20, pady=20)

    def grafica3d(self):
        Graficador3D(tk.Toplevel(self.master))

    def grafica2d(self):
        Graficador2D(tk.Toplevel(self.master))

class Graficador3D:
    def __init__(self, master):
        self.master = master
        self.master.title("Graficador de funciones 3D")
        self.master.geometry("800x600")
        
        self.create_widgets()

    def create_widgets(self):
        # Entrada de función
        self.function_label = customtkinter.CTkLabel(self.master, text="Ingrese la función:", text_color="black", font=("Arial", 16))
        self.function_label.pack()
        self.function_entry = tk.Entry(self.master, width=50)
        self.function_entry.pack()

        # Entrada de dominio
        self.domain_frame = tk.Frame(self.master)
        self.domain_frame.pack()
        
        self.x_min_label = tk.Label(self.domain_frame, text="x mínimo:")
        self.x_min_label.grid(row=0, column=0)
        self.x_min_entry = tk.Entry(self.domain_frame)
        self.x_min_entry.grid(row=0, column=1)

        self.x_max_label = tk.Label(self.domain_frame, text="x máximo:")
        self.x_max_label.grid(row=0, column=2)
        self.x_max_entry = tk.Entry(self.domain_frame)
        self.x_max_entry.grid(row=0, column=3)

        self.y_min_label = tk.Label(self.domain_frame, text="y mínimo:")
        self.y_min_label.grid(row=1, column=0)
        self.y_min_entry = tk.Entry(self.domain_frame)
        self.y_min_entry.grid(row=1, column=1)

        self.y_max_label = tk.Label(self.domain_frame, text="y máximo:")
        self.y_max_label.grid(row=1, column=2)
        self.y_max_entry = tk.Entry(self.domain_frame)
        self.y_max_entry.grid(row=1, column=3)

        # Botones
        self.plot_button = customtkinter.CTkButton(self.master, text="Graficar", command=self.plot_function_3d, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        self.plot_button.pack(pady=5)
        
        self.clear_button = customtkinter.CTkButton(self.master, text="Borrar", command=self.clear_plot, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        self.clear_button.pack(pady=5)

        # Área de la gráfica
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Barra de herramientas
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.master)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack()

        # Mensaje de error
        self.error_label = tk.Label(self.master, fg="red")
        self.error_label.pack()

    def plot_function_3d(self):
        function_text = self.function_entry.get()
        x_min = float(self.x_min_entry.get())
        x_max = float(self.x_max_entry.get())
        y_min = float(self.y_min_entry.get())
        y_max = float(self.y_max_entry.get())

        x = np.linspace(x_min, x_max, 1000)
        y = np.linspace(y_min, y_max, 1000)
        x, y = np.meshgrid(x, y)

        try:
            z = eval(function_text)
            self.ax.clear()
            self.ax.plot_surface(x, y, z, cmap='viridis')
            self.ax.set_xlabel('x')
            self.ax.set_ylabel('y')
            self.ax.set_zlabel('z')
            self.ax.set_title('Gráfico 3D de la función: ' + function_text)
            self.canvas.draw()
        except Exception as e:
            self.error_label.config(text="Error: " + str(e))

    def clear_plot(self):
        self.ax.clear()
        self.canvas.draw()

class Graficador2D:
    def __init__(self, master):
        self.master = master
        self.master.title("Graficador de funciones 2D")
        
        self.create_widgets()

    def create_widgets(self):
        # Entrada de función
        self.function_label = customtkinter.CTkLabel(self.master, text="Ingrese la función:", text_color="black", font=("Arial", 16))
        self.function_label.pack()
        self.function_entry = tk.Entry(self.master, width=50)
        self.function_entry.pack()

        # Entrada de dominio
        self.domain_frame = tk.Frame(self.master)
        self.domain_frame.pack()

        self.x_min_label = tk.Label(self.domain_frame, text="x mínimo:")
        self.x_min_label.grid(row=0, column=0)
        self.x_min_entry = tk.Entry(self.domain_frame)
        self.x_min_entry.grid(row=0, column=1)

        self.x_max_label = tk.Label(self.domain_frame, text="x máximo:")
        self.x_max_label.grid(row=0, column=2)
        self.x_max_entry = tk.Entry(self.domain_frame)
        self.x_max_entry.grid(row=0, column=3)

        # Botones
        self.plot_button = customtkinter.CTkButton(self.master, text="Graficar", command=self.plot_function_2d, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        self.plot_button.pack(pady=5)

        self.clear_button = customtkinter.CTkButton(self.master, text="Borrar", command=self.clear_plot, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        self.clear_button.pack(pady=5)

        # Área de la gráfica
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        # Barra de herramientas
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.master)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack()

        # Mensaje de error
        self.error_label = tk.Label(self.master, fg="red")
        self.error_label.pack()

    def plot_function_2d(self):
        function_text = self.function_entry.get()
        x_min = float(self.x_min_entry.get())
        x_max = float(self.x_max_entry.get())
        x = np.linspace(x_min, x_max, 1000)

        try:
            y = eval(function_text)
            self.ax.clear()
            self.ax.plot(x, y)
            self.ax.set_xlabel('x')
            self.ax.set_ylabel('f(x)')
            self.ax.set_title('Gráfico de la función: ' + function_text)
            self.ax.grid(True)
            self.ax.axhline(0, color='black', linewidth=0.5)
            self.ax.axvline(0, color='black', linewidth=0.5)
            self.canvas.draw()
        except Exception as e:
            self.error_label.config(text="Error: " + str(e))

    def clear_plot(self):
        self.ax.clear()
        self.canvas.draw()

# Inicializar la ventana principal
root = tk.Tk()
app = GraficadorFunciones(root)
root.mainloop()
