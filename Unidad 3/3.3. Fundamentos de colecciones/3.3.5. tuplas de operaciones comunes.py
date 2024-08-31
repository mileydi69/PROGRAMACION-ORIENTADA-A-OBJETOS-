# Creación de una tupla
mi_tupla = (2, "tres", 4.0)

# Acceso a un elemento
print(mi_tupla[2])  # Imprime "tres"

# Desempaquetado de una tupla
e, f, g = mi_tupla
print(e, f, g)  # Imprime 2 tres 4.0

# Concatenación de tuplas
nueva_tupla = mi_tupla + (6, 7)
print(nueva_tupla)  # Imprime (2, 'tres', 4.0, 6, 7)