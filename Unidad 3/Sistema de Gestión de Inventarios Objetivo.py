class Inventario:
    def __init__(self):
        # Diccionario para almacenar productos, clave: ID del producto, valor: detalles del producto
        self.productos = {}

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        """Añadir un producto al inventario."""
        if id_producto in self.productos:
            print(f"El producto con ID {id_producto} ya existe.")
        else:

            self.productos[id_producto] = {
                'nombre': nombre,
                'cantidad': cantidad,
                'precio': precio
            }
            print(f"Producto '{nombre}' añadido con éxito.")

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        """Actualizar los detalles de un producto existente."""
        if id_producto in self.productos:
            if nombre is not None:
                self.productos[id_producto]['nombre'] = nombre
            if cantidad is not None:
                self.productos[id_producto]['cantidad'] = cantidad
            if precio is not None:
                self.productos[id_producto]['precio'] = precio
            print(f"Producto con ID {id_producto} actualizado con éxito.")
        else:
            print(f"El producto con ID {id_producto} no existe.")

    def eliminar_producto(self, id_producto):
        """Eliminar un producto del inventario."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado con éxito.")
        else:
            print(f"El producto con ID {id_producto} no existe.")

    def buscar_producto(self, id_producto):
        """Buscar un producto por su ID."""
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            return f"ID: {id_producto}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}"
        else:
            return f"El producto con ID {id_producto} no existe."

    def listar_productos(self):
        """Listar todos los productos en el inventario."""
        if not self.productos:
            return "El inventario está vacío."
        productos_lista = []
        for id_producto, detalles in self.productos.items():
            productos_lista.append(f"ID: {id_producto}, Nombre: {detalles['nombre']}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}")
        return "\n".join(productos_lista)
# Crear una instancia del inventario
mi_inventario = Inventario()

# Añadir productos
mi_inventario.añadir_producto('001', 'Laptop', 10, 750.00)
mi_inventario.añadir_producto('002', 'Ratón', 50, 25.00)

# Buscar un producto
print(mi_inventario.buscar_producto('001'))

# Actualizar un producto
mi_inventario.actualizar_producto('001', cantidad=8, precio=700.00)

# Listar todos los productos
print(mi_inventario.listar_productos())

# Eliminar un producto
mi_inventario.eliminar_producto('002')

# Listar productos después de eliminar uno
print(mi_inventario.listar_productos())
