import tkinter as tk
from tkinter import messagebox
import pyfiglet

# Mostrar título ASCII en consola
ascii_title = pyfiglet.figlet_format("CURLY")
print(ascii_title)

# Función para procesar el comando
def procesar_comando():
    comando = entrada.get().strip().lower()
    if comando == "kurly":
        messagebox.showinfo("Haz sido Curlyado", "¡Felicidades! Has invocado a Curly.")
    else:
        messagebox.showwarning("Comando inválido", f"'{comando}' no es reconocido.")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("CURLY Interface")
ventana.geometry("300x150")

# Etiqueta
tk.Label(ventana, text="Escribe un comando:").pack(pady=10)

# Entrada de texto
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Botón
tk.Button(ventana, text="Ejecutar", command=procesar_comando).pack(pady=10)

# Iniciar interfaz
ventana.mainloop()
