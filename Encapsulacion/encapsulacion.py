class electrodomestico('de toda clase'):
 def __init__(self,nombres, codigo, motor, inteligencia, vida, color):
     super().__init__(nombres, codigo, motor, inteligencia, vida)
     self.color = color

def cambiar_codigos(self):
    opcion = int(input('elige un codigo:(1) lavadora lg cambio 6. (2) microhondas oster cambio 3. '))
    if opcion == 1:
        self.codigo = 6
    elif opcion == 2:
        self.codigo = 8
    else:
        print("opcion no valida")
 def atributos(self):
     super().__atributos()
     print('codigo:', self.codigo)
def cambio(self, codigo)