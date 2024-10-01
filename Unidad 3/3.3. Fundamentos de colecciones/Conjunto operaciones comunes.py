# Creación de un conjunto
frutas = {"durazno", "frambuesa", "toronja"}

# Agregar un elemento
frutas.add("sandia")

# Eliminar un elemento
frutas.remove("frambuesa")  # Usar discard("frambuesa") para evitar errores si no existe

# Operaciones de conjunto
vegetales = {"pepino", "calabaza", "toronja"}
union = frutas | vegetales
interseccion = frutas & vegetales
diferencia = frutas - vegetales

print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia:", diferencia)


