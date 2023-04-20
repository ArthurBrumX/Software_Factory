#ATIVIDADE - 1

# DESENVOLVA O DIAGRAMA DE CLASSES E IMPLEMENTA EM PYTHON, O SEGUINTE CASO:

# UMA CLASSE CHAMADA "PESSOA" QUE TERÁ OS SEGUINTES ATRIBUTOS: NOME, IDADE E ALTURA. ALÉM DISSO, TEREMOS UM MÉTODO
# CHAMADO "IMPRIMIR_INFORMACOES" QUE IRÁ IMPRIMIR OS VALORES DOS ATRIBUTOS DA PESSOA NA TELA (CRIAR NO MÍNIMO DOIS OBJETOS).

class pessoa():
    def __init__(self):
        self.nome = input("Digite Seu nome: ")
        self.idade = int(input("Digite Sua Idade: "))
        self.altura = float(input("Digite Sua Altura: "))

    def imprimir_informacoes(self):

        print(self.nome)
        print(self.idade)
        print(self.altura)

humano = pessoa()
humano.imprimir_informacoes()

        
    
        
