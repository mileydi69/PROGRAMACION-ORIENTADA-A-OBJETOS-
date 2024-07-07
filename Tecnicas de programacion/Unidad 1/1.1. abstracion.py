# Definición de la clase abstracta Figura
class Figura('ABC'):
    def __init__(self, color):
        self.color = color


    def area(self):



    def perimetro(self):



# Clase concreta Rectangulo que hereda de Figura
class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


# Clase concreta Circulo que hereda de Figura
class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.radio


# Uso de las clases
rectangulo = Rectangulo("azul", 5, 10)
circulo = Circulo("rojo", 7)

print("Área del rectángulo:", rectangulo.area())  # Salida: Área del rectángulo: 50
print("Perímetro del rectángulo:", rectangulo.perimetro())  # Salida: Perímetro del rectángulo: 30
print("Área del círculo:", circulo.area())  # Salida: Área del círculo: 153.86
print("Perímetro del círculo:", circulo.perimetro())  # Salida: Perímetro del círculo: 43.96