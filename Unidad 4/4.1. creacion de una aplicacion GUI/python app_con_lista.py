import tkinter as tk
from tkinter import messagebox

def agregar_item():
    try:
# Añade el número del resultado ingresado en el campo de texto a la lista.
        numero = float(entrada.get())
        resultado = numero * 3
# Corrige la asignación de resultado
# Muestra el resultado en la lista de texto
        lista_texto.insert(tk.END, f"El triple de {numero} es {resultado}\n")
    except ValueError:
        messagebox.showerror("Error", "El valor especificado es incorrecto")

def limpiar_lista():
    """Limpia todos los elementos de la lista y el campo de entrada."""
    lista_texto.delete(1.0, tk.END)
# Borra el contenido del widget Text
    entrada.delete(0, tk.END)
# Borra el contenido del campo de entrada

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Software de Cálculo del Triple")
ventana.geometry("300x300")

# Crear un campo de texto para la entrada de números
entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=10)

# Crear un botón "Agregar" que llama a la función agregar_item
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_item)
boton_agregar.pack(pady=5)

# Crear un botón "Limpiar" que llama a la función limpiar_lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Crear un widget Text para mostrar los elementos agregados
lista_texto = tk.Text(ventana, width=50, height=10)
lista_texto.pack(pady=10)

# Ejecutar el bucle principal de eventos
ventana.mainloop()
