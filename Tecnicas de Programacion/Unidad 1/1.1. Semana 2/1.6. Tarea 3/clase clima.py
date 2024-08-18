class Clima:
    def __init__(self,calor,frio):
        self.calor = calor
        self.frio = frio


class Lluvia(Clima):
    def __init__(self,calor,frio):
        super().__init__(calor,frio)
        self.nombre = "Lluvia"

class Soleado(Clima):

    def __init__(self,calor,frio):
        super().__init__(calor,frio)
        self.nombre = "Soleado"


    def atributos(self):
        print(self.nombre,self.calor,self.frio)
        print('Lluvia:',self.frio)

        print('Soleado:', self.calor )
