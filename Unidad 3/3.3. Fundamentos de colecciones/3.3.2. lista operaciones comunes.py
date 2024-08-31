# Creación de una lista
frutas = ["mango", "pera", "melocoton"]

# Añadir un elemento
frutas.append("piña")

# Reemplazar el elemento en el índice 1 con "fresa"
# Primero eliminamos el elemento en el índice 1 ("piña")
frutas.pop(1)  # Esto elimina "piña"

# Ahora, añadir "fresa" en el índice 1
frutas.insert(1, "fresa")  # Inserta "fresa" en el índice 1

# Acceder a un elemento
print(frutas[0])  # Imprime "mango"
print(frutas[1])  # Imprime "fresa"

# Eliminar el elemento en el índice 1 ("fresa")
frutas.pop(1)  # Elimina "fresa"

# Imprimir la lista modificada
print(frutas)  # Imprime ['mango', 'melocoton', 'piña']







