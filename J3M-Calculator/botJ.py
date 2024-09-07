import discord
from discord.ext import commands
import tkinter as tk
from threading import Thread

# Configuración del bot de Discord
intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Variables globales para acceder a elementos de Tkinter
tk_response_var = None

# Comando del bot para procesar y responder desde Tkinter
@bot.command()
async def saludo(ctx):
    response = "Hola, ¿cómo estás?"
    # Actualizar el Label en el hilo principal de Tkinter usando StringVar
    if tk_response_var:
        tk_response_var.set(response)
    await ctx.send(response)  # Opcional si aún quieres enviar algo a Discord

# Función para ejecutar comandos directamente
def execute_command(command_name):
    command = bot.get_command(command_name)
    if command:
        # Simulamos el contexto llamando al comando directamente
        ctx = type('Context', (object,), {'send': lambda s: None})
        bot.loop.create_task(command.invoke(ctx))

# Crear la interfaz de Tkinter
def run_gui():
    global tk_response_var

    # Función para tomar el texto del Entry y ejecutar el comando
    def send_command():
        command = entry.get()  # Obtiene el texto del campo de entrada
        entry.delete(0, tk.END)  # Limpia el campo de entrada
        if command:
            execute_command(command)  # Ejecuta el comando ingresado

    root = tk.Tk()
    root.title("Interfaz de Discord Bot")

    label = tk.Label(root, text="Escribe un comando:")
    label.pack()

    entry = tk.Entry(root, width=50)
    entry.pack()

    send_button = tk.Button(root, text="Enviar", command=send_command)
    send_button.pack()

    # Usar StringVar para enlazar el texto del Label
    tk_response_var = tk.StringVar()
    tk_response_var.set("Respuesta del bot aquí...")
    response_label = tk.Label(root, textvariable=tk_response_var)
    response_label.pack()

    root.mainloop()

# Inicia el bot en un hilo separado
if __name__ == "__main__":
    # Iniciar la interfaz de Tkinter en un hilo separado
    bot_thread = Thread(target=lambda: bot.run("MTI4MDM1NDAyMzIzNjQzNTk3OA.G0EDvH.tjsDPeXjFOzDuYD0OlOCuG_IyAI9kQbD4qB6c8"))
    bot_thread.start()

    # Ejecutar la GUI de Tkinter
    run_gui()
