import os
def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Programacion Orientada a Objetos/Tecnicas de Programacion/1.Unidad 1/Semana 2.py',
        '2': '1.1. Abstraccion/ abstraccion.py',
        '3': '1.2. Encapsulacion/encapsulacion.py',
        '4': '1.3. Herencia/herencia.py',
        '5': '1.4. Polimorfismo/polimorfismo.py',
        '6': '1.5. Semana 3/programacion Orientada a Objetos/programacion tradicional.py',
        '7': '1.6. Semana 4/ejemplos del mundo real.py',
        '8': '1.7. Semana 5/calcular el area de un perimetro.py',
        '9': 'Programacion Orientada a Objetos/Tecnicas de Programacion/2.Unidad 2.py',
        '10': '2.1. Semana 6/objeto, clase herencia, polimorfismo.py',
        '11': '2.2. Semana 7/ implementacion de conductores y destructores.py',

         
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()