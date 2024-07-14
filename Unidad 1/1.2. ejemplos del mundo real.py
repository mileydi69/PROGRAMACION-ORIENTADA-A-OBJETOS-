class Frutas:
   def __init__(self, cantidad):
        self.cantidad = cantidad


   def comprar(self,cantidad):
       self.cantidad += cantidad

   def eliminar(self,cantidad):
       self.cantidad -= cantidad
   def __str__(self):
       return f"ls cantidad de frutas: {self.cantidad}"

#intanciar cada objeto
fruta1 = Frutas(5)
fruta1.comprar(1)
fruta1.eliminar(5)

print(fruta1)


class Naturaleza:
    def __init__(self,raiz, plantas, hojas,flores, petalos):
        self.raiz = raiz
        self.plantas = plantas
        self.hojas = hojas
        self.flores = flores
        self.petalos = petalos
class Arbol(Naturaleza):
    def __init__(self,raiz, hojas):
        super().__init__(raiz)
        self.nombre = 'Arbol'



class Flores(Naturaleza):


    def __init__(self, plantas,petalos):
        super().__init__(petalos)
        self.nombre = 'Flores'






