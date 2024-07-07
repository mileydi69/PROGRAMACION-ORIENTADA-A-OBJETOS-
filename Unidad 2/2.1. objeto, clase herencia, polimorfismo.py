# Definición de la clase base Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

    def saludar(self):
        return f"Hola, soy {self.nombre}"


# Definición de la clase derivada Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Curso: {self.curso}"

    def estudiar(self):
        return f"{self.nombre} está estudiando en el curso {self.curso}"


# Ejemplo de encapsulamiento
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Saldo es un atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Se han depositado {cantidad} unidades."
        else:
            return "La cantidad a depositar debe ser mayor que cero."

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self.__saldo}"


# Ejemplo de polimorfismo
def mostrar_detalle(objeto):
    if isinstance(objeto, Persona):
        print(objeto.saludar())
    elif isinstance(objeto, Estudiante):
        print(objeto.estudiar())
    else:
        print("Objeto no reconocido.")


# Uso de las clases y funciones definidas
if __name__ == "__main__":
    # Creación de objetos de las clases
    persona1 = Persona("Juan", 30)
    estudiante1 = Estudiante("María", 25, "Python")

    # Herencia y polimorfismo
    print(persona1)  # Salida: Nombre: Juan, Edad: 30
    print(estudiante1)  # Salida: Nombre: María, Edad: 25, Curso: Python
    mostrar_detalle(persona1)  # Salida: Hola, soy Juan
    mostrar_detalle(estudiante1)  # Salida: María está estudiando en el curso Python

    # Encapsulamiento
    cuenta1 = CuentaBancaria("Carlos", 1000)
    print(cuenta1)  # Salida: Titular: Carlos, Saldo: 1000
    print(cuenta1.depositar(500))  # Salida: Se han depositado 500 unidades.
    # Intentando acceder al saldo directamente (generará un error porque es privado)
    # print(cuenta1.__saldo)
