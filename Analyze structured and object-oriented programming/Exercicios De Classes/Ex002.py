# ATIVIDADE - 2

# DESENVOLVA O DIAGRAMA DE CLASSES E IMPLEMENTA EM PYTHON, O SEGUINTE CASO: 
# UMA CLASSE TERÁ UM ATRIBUTO "RAIO" E DOIS MÉTODOS: 
# UM PARA CALCULAR A ÁREA DO CÍRCULO E OUTRO PARA CALCULAR O PERÍMETRO ( CRIAR NO MÍNIMO DOIS OBJETOS).

class raio():

    def __init__(self):
        self.pi = 3.14
        self.raio_circulo = float(input("* Digite o raio do circulo: "))

    def area(self):
        self.area = self.pi * self.raio_circulo * self.raio_circulo
        print("- A area é de: {}".format(self.area))

    def perimetro(self):
        self.perimetro = 2 * self.pi * self.raio_circulo
        print("- O perimetro é de: {}".format(self.perimetro))
        # P = 2 * pi * raio

circulo = raio()
circulo.area()
circulo.perimetro()