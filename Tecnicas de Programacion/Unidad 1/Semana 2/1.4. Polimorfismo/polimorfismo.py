class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu!"


# sonido genérico de un animal
def hacer_sonido_animal(animal):
    return animal.hacer_sonido()


# instancias de diferentes animales
perro = Perro("Bobby")
gato = Gato("Pelusa")
vaca = Vaca("Margarita")

# Llamar a la función que hace sonido
print(f"{perro.nombre}: {hacer_sonido_animal(perro)}")  # Salida: Bobby: Guau!
print(f"{gato.nombre}: {hacer_sonido_animal(gato)}")  # Salida: Pelusa: Miau!
print(f"{vaca.nombre}: {hacer_sonido_animal(vaca)}")  # Salida: Margarita: Muu!