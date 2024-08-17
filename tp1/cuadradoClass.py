from rectanguloClass import Rectangulo

class Cuadrado(Rectangulo):

    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)

    def info(self):
        return super().info()

cuadrado = Cuadrado(7, 3)
print("Aca arranca la ejecucion:")
print(cuadrado.area())
cuadrado.info()