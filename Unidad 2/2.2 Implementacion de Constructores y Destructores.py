# Constructores
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def saludar(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}."

# Creación de instancias de Persona
persona1 = Persona("Pedro", 63, "Colombia")
persona2 = Persona("Carmen", 20, "Londres")

# Accediendo a los atributos y métodos de las instancias
print(persona1.saludar())  # Salida: Hola, soy Pedro, tengo 63 años y vivo en Colombia.
print(persona2.saludar())  # Salida: Hola, soy Carmen, tengo 20 años y vivo en Londres.


# Destructores
class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        try:
            self.file = open(self.nombre, 'w')
            print(f"Archivo '{self.nombre}' abierto correctamente.")
        except IOError as e:
            print(f"Error al abrir el archivo '{self.nombre}': {e}")
            raise

    def escribir(self, contenido):
        if hasattr(self, 'file'):
            self.file.write(contenido)
            print(f"Se ha escrito en el archivo '{self.nombre}': {contenido}")
        else:
            print(f"Error: Intentando escribir en un archivo cerrado.")

    def __del__(self):
        if hasattr(self, 'file'):
            self.file.close()
            print(f"Archivo '{self.nombre}' cerrado correctamente.")
        else:
            print(f"No se cerró ningún archivo para '{self.nombre}'.")

# Ejemplo de uso
try:
    archivo = Archivo("ejemplo.txt")
    archivo.escribir("Hola, mundo!")
    del archivo  # Forzamos la llamada al destructor
except Exception as e:
    print(f"Error: {e}")
