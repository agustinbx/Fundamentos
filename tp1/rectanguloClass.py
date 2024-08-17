class Rectangulo:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return (self.alto) * 2 + (self.ancho) * 2
    
    def info(self):
        print(f"El ancho es: {self.ancho} ")
        print(f"El alto es: {self.alto} ")
    
rectangulo1 = Rectangulo(2, 4)
rectangulo2 = Rectangulo(3, 6)

#rectangulo1.info()

print(rectangulo1.area())
