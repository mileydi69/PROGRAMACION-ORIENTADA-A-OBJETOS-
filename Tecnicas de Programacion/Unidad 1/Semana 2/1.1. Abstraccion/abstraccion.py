# Definición de la clase abstracta Figura

class Figura_ABC:

   def __init__(self, color):
        self.color = color


   def area(self, aprobar):

       print('')

   def perimetro(self, aprobar):
        return 2 * (self.largo + self.ancho)


# Clase concreta Rectangulo que hereda de Figura
class Rectangulo(Figura_ABC):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def area(self, aprobar):
        print('')
        return self.base * self.altura

    def perimetro(self, aprobar):
        return 2 * (self.base + self.altura)


# Clase concreta Circulo que hereda de Figura
class Circulo(Figura_ABC):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self, aprobar):
        return 3.14 * self.radio ** 2

    def perimetro(self, aprobar):
        return 2 * 3.14 * self.radio


# Uso de las clases
rectangulo = Rectangulo("azul", 5, 10)
circulo = Circulo("rojo", 7)

print("Área del rectángulo:", rectangulo.area('aprobar'))  # Salida: Área del rectángulo: 50
print("Perímetro del rectángulo:", rectangulo.perimetro('aprobar'))  # Salida: Perímetro del rectángulo: 30
print("Área del círculo:", circulo.area('aprobar'))  # Salida: Área del círculo: 153.86
print("Perímetro del círculo:", circulo.perimetro('aprobar'))  # Salida: Perímetro del círculo: 43.96