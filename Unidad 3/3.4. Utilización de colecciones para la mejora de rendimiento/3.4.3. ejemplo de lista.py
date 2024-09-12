class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}: ${self.precio}"

class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("El carrito está vacío.")
        else:
            print("Productos en el carrito:")
            for producto in self.productos:
                print(producto)

    def calcular_total(self):
        return sum(producto.precio for producto in self.productos)

# Ejemplo de uso
carrito = CarritoDeCompras()
carrito.agregar_producto(Producto("peras", 1.00))
carrito.agregar_producto(Producto("galletas", 2.25))
carrito.agregar_producto(Producto("yogurt", 4.50))

carrito.mostrar_productos()
print(f"Total: ${carrito.calcular_total()}")
