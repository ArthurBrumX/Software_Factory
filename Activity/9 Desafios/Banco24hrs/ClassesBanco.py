# 4 - Desenvolva um sistema simulando um banco 24 horas em Python, utilizando Programação Orientada a Objetos (POO). 
# O sistema deve permitir a criação e manipulação de contas bancárias, saques e depósitos em caixas eletrônicos. 
# Além disso, cada conta bancária terá um limite diário de saque. 

class banco24Hrs:
    def __init__(self,numeroConta,nomeCompleto,telefone,endereco,dataNasc,saldoConta):
        self.numeroConta = numeroConta
        self.nomeCompleto = nomeCompleto
        self.telefone = telefone
        self.endereco = endereco
        self.dataNasc = dataNasc
        self.saldoConta = saldoConta

    def CriarConta(self,numeroConta,nomeCompleto,telefone,endereco,dataNasc,saldoConta):
        self.numeroConta = numeroConta
        self.nomeCompleto = nomeCompleto
        self.telefone = telefone
        self.endereco = endereco
        self.dataNasc = dataNasc
        self.saldoConta = saldoConta

    def Saques(self):
        saqueDiario = self.saldoConta * 60 / 100
        sacar = float(input("Quanto Deseja Sacar: R$ "))
        if sacar > saqueDiario:
            print ("NEGADO! Este valor Atigiu o limite de Saque Diario!")
        elif sacar <= saqueDiario:
            self.saldoConta = self.saldoConta - sacar
            print (f"Voce Sacou R${sacar}")
            print (f"Seu Saldo Agora é de R${self.saldoConta}")

    def Deposito(self):
        depositar = float(input("Quanto Deseja Depósitar: R$"))
        self.saldoConta = self.saldoConta + depositar
        print(f"Voçê Depositou R${self.saldoConta}!!")
        print(f"Seu Salto total Agora é de R${self.saldoConta}!!")