import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo '{ruta_script}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra este script
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Tecnicas de Programacion/Unidad 1/1.1. Semana 2/1.2. Abstraccion/abstraccion.py',
        '2': 'Tecnicas de Programacion/Unidad 1/1.1. Semana 2/1.3. Encapsulacion/encapsulacion.py',
        '3': 'Tecnicas de Programacion/Unidad 1/1.1. Semana 2/1.4. Herencia/herencia.py',
        '4': 'Tecnicas de Programacion/Unidad 1/1.1. Semana 2/1.5. Polimorfismo/polimorfismo.py',
        '5': 'Tecnicas de Programacion/Unidad 1/1.1. Semana 2/1.6. Tarea 3/clase clima.py',
        '6': 'Tecnicas de Programacion/Unidad 1/1.1. Semana 2/1.6.1. Tarea 3/programacion tradicional.py',
        '7': 'Tecnicas de Programacion/Unidad 1/1.1. Semana 2/1.7. Tarea 4/ejemplos del mundo real.py',
        '8': 'Tecnicas de Programacion/Unidad 1/1.1. Semana 2/1.8. Tarea 5/calcular el area de un perimetro.py',
        '9': 'Tecnicas de Programacion/Unidad 2/2.1. Semana 6/objeto clase herencia polimorfismo.py',
        '10': 'Unidad 2/2.2. Semana 7/implementacion de constructores y destructores.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key, value in opciones.items():
            print(f"{key} - {value}")
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
