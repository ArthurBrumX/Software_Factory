class operacao():
    def __init__(self):
        self.a = float(input("Digite o primeiro numero: "))
        self.b = float(input("Digite outro numero: "))

    def soma(self):
        print (self.a+self.b)

    def multiplicacao(self):
        print (self.a*self.b)

    def divisao(self):
        print (self.a/self.b)



op = operacao()
op.soma()
