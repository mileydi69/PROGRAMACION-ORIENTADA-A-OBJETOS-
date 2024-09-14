import tkinter as tk
from tkinter import messagebox
# Función para actualizar la etiqueta con el texto ingresado
def mostrar_texto():
    messagebox.showinfo("mensaje", "mi nombre, leydi susana")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica con tkinter")
ventana.geometry("200x200")


# Crear un botón que llama a la función mostrar_texto
boton = tk.Button(ventana, text="Mostrar Texto", command=mostrar_texto)
boton.pack(pady=10)


# Ejecutar el bucle principal de eventos
ventana.mainloop()