import json
import os

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


def __init__(self, archivo='inventario.txt'):
    self.archivo = archivo
    self.inventario = self.cargar_inventario()


def cargar_inventario(self):
    """Carga el inventario desde un archivo. Si el archivo no existe, crea uno nuevo."""
    if not os.path.exists(self.archivo):
        print("El archivo de inventario no existe. Se creará un nuevo archivo.")
        return {}

    try:
        with open(self.archivo, 'r') as f:
            inventario = json.load(f)
        print("Inventario cargado exitosamente.")
        return inventario
    except FileNotFoundError:
        print("El archivo no se encontró. Se creará uno nuevo.")
        return {}
    except json.JSONDecodeError:
        print("El archivo está corrupto o no es un JSON válido. Se creará uno nuevo.")
        return {}
    except PermissionError:
        print("Permiso denegado para leer el archivo.")
        return {}
    except Exception as e:
        print(f"Se produjo un error al cargar el inventario: {e}")
        return {}

def guardar_inventario(self):
    """Guarda el inventario en un archivo."""
    try:
        with open(self.archivo, 'w') as f:
            json.dump(self.inventario, f, indent=4)
        print("Inventario guardado exitosamente.")
    except PermissionError:
        print("Permiso denegado para escribir en el archivo.")
    except IOError as e:
        print(f"Error al guardar el archivo: {e}")
    except Exception as e:
        print(f"Se produjo un error al guardar el inventario: {e}")

        def main():
            inventario = Inventario()

            while True:
                print("\nMenú de Gestión de Inventarios:")
                print("1. Agregar producto")
                print("2. Actualizar producto")
                print("3. Eliminar producto")
                print("4. Salir")

                opcion = input("Elija una opción: ")

                if opcion == '1':
                    id_producto = input("Ingrese ID del producto: ")
                    nombre = input("Ingrese nombre del producto: ")
                    cantidad = int(input("Ingrese cantidad: "))
                    precio = float(input("Ingrese precio: "))
                    inventario.agregar_producto(id_producto, nombre, cantidad, precio)

                elif opcion == '2':
                    id_producto = input("Ingrese ID del producto a actualizar: ")
                    nombre = input("Ingrese nuevo nombre (dejar en blanco si no desea cambiar): ")
                    cantidad = input("Ingrese nueva cantidad (dejar en blanco si no desea cambiar): ")
                    precio = input("Ingrese nuevo precio (dejar en blanco si no desea cambiar): ")

                    cantidad = int(cantidad) if cantidad else None
                    precio = float(precio) if precio else None

                    inventario.actualizar_producto(id_producto, nombre if nombre else None, cantidad, precio)

                elif opcion == '3':
                    id_producto = input("Ingrese ID del producto a eliminar: ")
                    inventario.eliminar_producto(id_producto)

                elif opcion == '4':
                    print("Saliendo...")
                    break

                else:
                    print("Opción no válida. Inténtelo de nuevo.")

        if __name__ == "__main__":
            main()















