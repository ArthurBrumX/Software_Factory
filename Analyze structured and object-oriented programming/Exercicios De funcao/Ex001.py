# 1 - CRIE UMA FUNÇÃO QUE RECEBE TRÊS NUMERO COMO PARÂMETRO E RETORNE A SOMA DELES

class operacao():
    def __init__(self):
        self.a = float(input("Digite o primeiro numero: "))
        self.b = float(input("Digite outro numero: "))
        self.c = float(input("Digite outro numero: "))

    def soma(self):
        print (self.a + self.b + self.c)

op = operacao()
op.soma()