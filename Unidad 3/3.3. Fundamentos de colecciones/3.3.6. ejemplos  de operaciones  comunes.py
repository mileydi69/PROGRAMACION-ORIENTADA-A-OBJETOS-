
# Definicion de clase
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def set_id(self):
        return self.id

    def set_nombre(self):
        return self.nombre

    def set_cantidad(self):
        return self.cantidad

    def set_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

import json

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos

    def añadir_producto(self, producto):
        if producto.get_id() not in self.productos:
            self.productos[producto.get_id()] = producto
        else:
            print("El producto ya existe.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id: producto.__dict__ for id, producto in self.productos.items()}, f)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                self.productos = {id: Producto(id, **info) for id, info in datos.items()}
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará un nuevo inventario vacío.")

# Interfaz de usuario

def menu():
    print("\n--- Gestión de Inventario ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")
    return input("Selecciona una opción: ")

def main():
    inventario = Inventario()
    archivo = 'inventario.json'

    while True:
        opcion = menu()

        if opcion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            print("Producto añadido.")

        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
            print("Producto eliminado.")

        elif opcion == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
            print("Producto actualizado.")

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            inventario.guardar_inventario(archivo)
            print("Inventario guardado.")

        elif opcion == '7':
            inventario.cargar_inventario(archivo)
            print("Inventario cargado.")

        elif opcion == '8':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 8.")

if __name__ == "__main__":
    main()