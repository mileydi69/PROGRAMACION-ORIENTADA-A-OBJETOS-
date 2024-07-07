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