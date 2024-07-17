# Definición de la clase base  Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


# Definición de una clase derivada  Carro que hereda de Vehiculo
class Carro(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Color: {self.color}")


# Definición de otra clase derivada  Motocicleta que hereda de Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Cilindrada: {self.cilindrada} cc")


# Uso de las clases
carro = Carro("Toyota", "Corolla", "Rojo")
motocicleta = Motocicleta("Honda", "CBR300R", 300)

print("Información del carro:")
carro.mostrar_informacion()  # Salida: Marca: Toyota, Modelo: Corolla, Color: Rojo

print("\nInformación de la motocicleta:")
motocicleta.mostrar_informacion()  # Salida: Marca: Honda, Modelo: CBR300R, Cilindrada: 300 cc