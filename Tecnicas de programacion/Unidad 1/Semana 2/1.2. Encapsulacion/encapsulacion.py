class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo privado
        self.__edad = edad  # atributo privado

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser mayor que cero.")

    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}")


# Uso de la clase Persona
persona1 = Persona("liliana", 30)
persona1.mostrar_informacion()  # Salida: Nombre: liliana, Edad: 30

# Intentando acceder directamente a los atributos privados
# Esto generará un error porque son privados y no accesibles directamente desde fuera de la clase
# print(persona1.__nombre)  # Genera un AttributoError

# Modificar atributos usando métodos públicos
persona1.set_nombre("Carlos")
persona1.set_edad(25)
persona1.mostrar_informacion()  # Salida: Nombre: Carlos, Edad: 25