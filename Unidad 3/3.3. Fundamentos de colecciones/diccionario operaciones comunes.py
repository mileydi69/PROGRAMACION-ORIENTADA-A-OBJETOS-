# Creación de un diccionario con información de un libro
#libro = {
#    "titulo": "la culpa fue de la vaca",
#    "autor": "Jaime Lopera Gutiérrez y Marta Inés Bernal Trujillo",
#    "publicado": 2015
#}

libro = dict()
libro["titulo"] = "la culpa fue de la vaca"
libro["autor"] = "Jaime Lopera Gutiérrez y Marta Inés Bernal Trujillo"
libro["publicado"] = 2015

# Acceso a un valor
print(libro["titulo"])  # Salida: la culpa fue de la vaca

# Modificación de un valor
libro["publicado"] = 2015

# Agregar un nuevo par clave-valor
libro["genero"] = "Fábula"
print(f'Genero agregado: {libro["genero"]}')

# Eliminación de un par clave-valor
#del libro["genero"]
print(f'Genero eliminado: {libro.pop("genero")}')

# Uso de .items() para iterar sobre el diccionario
for clave, valor in libro.items():
    print(f"{clave}: {valor}")