# DESENVOLVA O DIAGRAMA DE CLASSES E IMPLEMENTA EM PYTHON, O SEGUINTE CASO:

# UMA CLASSE PARA REPRESENTAR UMA CALCULADORA QUE REALIZA AS OPERAÇÕES BÁSICAS (ADIÇÃO, SUBTRAÇÃO, MULTIPLICAÇÃO E DIVISÃO), 
# CRIAR NO MÍNIMO DOIS OBJETOS.


class calculadora ():
    def __init__(self):
        self.valor_1 = int(input("Digite um Numero: "))
        self.valor_2 = int(input("Digite Outro Numero: "))
    
    def adicao(self):
        adicao = self.valor_1 + self.valor_2
        print("A soma dos Número é:",adicao)

    def subtracao(self):
        subtracao = self.valor_1 - self.valor_2
        print("A subtração dos Número é:" ,subtracao)

    def multiplicacao(self):
        multiplicacao = self.valor_1 * self.valor_2
        print("A miltiplicação dos Número é:" ,multiplicacao)

    def divisao(self):
        divisao = self.valor_1 / self.valor_2
        print("A divisao dos Número é:" ,divisao)


calculo = calculadora()

calculo.adicao()
calculo.subtracao()
calculo.multiplicacao()
calculo.divisao()


