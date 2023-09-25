# 4 - Desenvolva um sistema simulando um banco 24 horas em Python, utilizando Programação Orientada a Objetos (POO). 
# O sistema deve permitir a criação e manipulação de contas bancárias, saques e depósitos em caixas eletrônicos. 
# Além disso, cada conta bancária terá um limite diário de saque. 

from ClassesBanco import banco24Hrs

cliente_1 = banco24Hrs(123,"Bruno Costa","123","Rua abc","12/03/94",7957.89)
cliente_2 = banco24Hrs(456,"Marcos Roney","456","Rua def","13/04/95", 4276.56)
cliente_3 = banco24Hrs(789,"Julio Rodriges","789","Rua ghi","14/05/96", 500)
cliente_4 = banco24Hrs(101112,"Fernanda jc","101112","Rua jkl","15/06/97", 950)
cliente_5 = banco24Hrs(131415,"Isabela Optvb","131415","Rua mno","16/07/98", 150)

contasUsuarios = [
    cliente_1,
    cliente_2,
    cliente_3,
    cliente_4,
    cliente_5
    ]

pergunta = input("Já tem uma Conta [S/N]: ")

if pergunta == "s" or pergunta == "S":
    conta = int(input("Digite o Numero da sua Conta Bancaria: "))

# ===============================================================================================================

    if conta == cliente_1.numeroConta:
        print(f"Seja Bem-Vindo {cliente_1.nomeCompleto}")
        print (
            "1 - Sacar\n",
            "2 - Depósitar\n"
            )
        
        operacao = int(input("Qual Operacao Deseja Realizar: "))

        while operacao == 1 or operacao == 2:

            if operacao == 1:
                # O limite diario de saque será de 60% em cima do valor total da conta
                cliente_1.Saques()
                print (
                    "1 - Sacar\n",
                    "2 - Depósitar\n",
                    "3 - Sair"
                    )
                operacao = int(input("Qual Operacao Deseja Realizar: "))

            if operacao == 2:
                cliente_1.Deposito()
                print (
                    "1 - Sacar\n",
                    "2 - Depósitar\n",
                    "3 - Sair"
                    )
                operacao = int(input("Qual Operacao Deseja Realizar: "))

            if operacao >= 3:
                print("Voce Escolheu Sair! Volte Sempre!")
# ===============================================================================================================

    elif conta == cliente_2.numeroConta:
        print(f"Seja Bem-Vindo {cliente_2.nomeCompleto}")
        print (
            "1 - Sacar\n",
            "2 - Depósitar\n"
            )
        
        operacao = int(input("Qual Operacao Deseja Realizar: "))

        while operacao == 1 or operacao == 2:

            if operacao == 1:
                # O limite diario de saque será de 60% em cima do valor total da conta
                cliente_2.Saques()
                print (
                    "1 - Sacar\n",
                    "2 - Depósitar\n",
                    "3 - Sair"
                    )
                operacao = int(input("Qual Operacao Deseja Realizar: "))

            if operacao == 2:
                cliente_2.Deposito()
                print (
                    "1 - Sacar\n",
                    "2 - Depósitar\n",
                    "3 - Sair"
                    )
                operacao = int(input("Qual Operacao Deseja Realizar: "))

            if operacao >= 3:
                print("Voce Escolheu Sair! Volte Sempre!")
# ===============================================================================================================

    elif conta == cliente_3.numeroConta:
        print(f"Seja Bem-Vindo {cliente_3.nomeCompleto}")
        print (
            "1 - Sacar\n",
            "2 - Depósitar\n"
            )
        
        operacao = int(input("Qual Operacao Deseja Realizar: "))

        while operacao == 1 or operacao == 2:

            if operacao == 1:
                # O limite diario de saque será de 60% em cima do valor total da conta
                cliente_3.Saques()
                print (
                    "1 - Sacar\n",
                    "2 - Depósitar\n",
                    "3 - Sair"
                    )
                operacao = int(input("Qual Operacao Deseja Realizar: "))

            if operacao == 2:
                cliente_3.Deposito()
                print (
                    "1 - Sacar\n",
                    "2 - Depósitar\n",
                    "3 - Sair"
                    )
                operacao = int(input("Qual Operacao Deseja Realizar: "))

            if operacao >= 3:
                print("Voce Escolheu Sair! Volte Sempre!")
# ===============================================================================================================

    elif conta == cliente_4.numeroConta:
        print(f"Seja Bem-Vindo {cliente_4.nomeCompleto}")
        print (
            "1 - Sacar\n",
            "2 - Depósitar\n"
            )
        
        operacao = int(input("Qual Operacao Deseja Realizar: "))

        while operacao == 1 or operacao == 2:

            if operacao == 1:
                # O limite diario de saque será de 60% em cima do valor total da conta
                cliente_4.Saques()
                print (
                    "1 - Sacar\n",
                    "2 - Depósitar\n",
                    "3 - Sair"
                    )
                operacao = int(input("Qual Operacao Deseja Realizar: "))

            if operacao == 2:
                cliente_4.Deposito()
                print (
                    "1 - Sacar\n",
                    "2 - Depósitar\n",
                    "3 - Sair"
                    )
                operacao = int(input("Qual Operacao Deseja Realizar: "))

            if operacao >= 3:
                print("Voce Escolheu Sair! Volte Sempre!")
# ===============================================================================================================

    elif conta == cliente_5.numeroConta:
        print(f"Seja Bem-Vindo {cliente_5.nomeCompleto}")
        print (
            "1 - Sacar\n",
            "2 - Depósitar\n"
            )
        
        operacao = int(input("Qual Operacao Deseja Realizar: "))

        while operacao == 1 or operacao == 2:

            if operacao == 1:
                # O limite diario de saque será de 60% em cima do valor total da conta
                cliente_5.Saques()
                print (
                    "1 - Sacar\n",
                    "2 - Depósitar\n",
                    "3 - Sair"
                    )
                operacao = int(input("Qual Operacao Deseja Realizar: "))

            if operacao == 2:
                cliente_5.Deposito()
                print (
                    "1 - Sacar\n",
                    "2 - Depósitar\n",
                    "3 - Sair"
                    )
                operacao = int(input("Qual Operacao Deseja Realizar: "))

            if operacao >= 3:
                print("Voce Escolheu Sair! Volte Sempre!")

    # =============================================================================================================================================================

elif pergunta == "n" or pergunta == "N":
    conta = input("Deseja Criar uma Conta [S/N]: ")

    if conta == "s" or conta == "S":
        novoCliente = banco24Hrs(
        novoNumeroConta = int(input("Digite o numero da sua nova Conta: ")),
        nomeCompleto = input("Digite o Seu Nome Completo: "),
        telefone = int(input("Digite o seu Numero de Telefone: ")),
        endereco = input("Digite o Nome Da Sua Residencia: "),
        dataNasc = int(input("Digite sua Data De Nascimento: ")),
        saldoInicialConta = float(input("Digite a Quantidade Inicial De Dinheiro que Irá Deixar: R$"))
        )
        
        novoCliente.append(novoCliente)

    elif conta == "n" or conta == "N":
        print("Entao Nao Podemos Continuar, Tenha um bom dia!")


# nao consegui de forma alguma criar um novo cliente, peço desculpas ;-;