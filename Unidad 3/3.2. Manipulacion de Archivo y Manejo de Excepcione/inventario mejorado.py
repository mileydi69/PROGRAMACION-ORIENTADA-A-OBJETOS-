import json
import os
class Inventario:
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

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario y guarda los cambios en el archivo."""
        if id_producto in self.inventario:
            print(f"El producto con ID {id_producto} ya existe.")
        else:
            self.inventario[id_producto] = {
                "nombre": nombre,
                "cantidad": cantidad,
                "precio": precio
            }
            self.guardar_inventario()
            print(f"Producto {nombre} agregado exitosamente.")

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        """Actualiza un producto existente en el inventario y guarda los cambios en el archivo."""
        if id_producto not in self.inventario:
            print(f"El producto con ID {id_producto} no existe.")
        else:
            if nombre is not None:
                self.inventario[id_producto]["nombre"] = nombre
            if cantidad is not None:
                self.inventario[id_producto]["cantidad"] = cantidad
            if precio is not None:
                self.inventario[id_producto]["precio"] = precio
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} actualizado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario y guarda los cambios en el archivo."""
        if id_producto in self.inventario:
            del self.inventario[id_producto]
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} eliminado exitosamente.")
        else:
            print(f"El producto con ID {id_producto} no existe.")


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
