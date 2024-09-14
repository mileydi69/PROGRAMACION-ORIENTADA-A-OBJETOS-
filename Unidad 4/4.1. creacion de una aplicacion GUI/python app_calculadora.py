import tkinter as tk

def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

def calcular(*args):
    try:
        expresion = entrada.get().strip()
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
        log.config(text = f"Operación: {expresion}, Resultado: {resultado}")
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")
        log.config(text = "Error")

def limpiar():
    entrada.delete(0, tk.END)
    log.config(text = "limpia")

def salir():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

# Centrar la ventana en la pantalla
ancho_ventana = 300
alto_ventana = 400
posicion_derecha = int(ventana.winfo_screenwidth() / 2 - ancho_ventana / 2)
posicion_abajo = int(ventana.winfo_screenheight() / 2 - alto_ventana / 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_derecha}+{posicion_abajo}")

# Crear un menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Limpiar", command=limpiar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)# Crear un campo de entrada
entrada = tk.Entry(ventana, font=("Calibri", 10), justify="right")
entrada.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
entrada.bind("<Return>", lambda event: calcular())
entrada.bind("<Escape>", lambda event: limpiar())

# Crear un label para visualizar las operaciones en formato de log
log = tk.Label(ventana, text="crea un label", font=("Calibri", 10))
log.grid(row=2, column=1, columnspan=4, padx=10, pady=5)

# Crear los botones de los números
numeros = "789456123"
for i, num in enumerate(numeros):
    tk.Button(ventana, text=num, font=("Calibri", 11),
              command=lambda numero=num: agregar_caracter(numero)).grid(row=(i//3)+3, column=(i%3), padx=7, pady=7)

# Botón para el punto decimal
tk.Button(ventana, text=".", font=("Calibri", 11), command=lambda: agregar_caracter(".")).grid(row=6, column=0, padx=7, pady=7)

# Botón para el cálculo
tk.Button(ventana, text="Calcular", font=("Calibri", 11), command=calcular).grid(row=6, column=1, columnspan=3, padx=7, pady=7)

# Crear los botones de las operaciones
operadores = ["+", "-", "*", "/"]
for i, operador in enumerate(operadores):
    tk.Button(ventana, text=operador, font=("Calibri", 12),
              command=lambda op=operador: agregar_caracter(op)).grid(row=i+3, column=3, padx=7, pady=7)



# Ejecutar el bucle de eventos
ventana.mainloop()




