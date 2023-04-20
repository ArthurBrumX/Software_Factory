# 1 - Faça um algoritmo que leia o nome, a idade, o sexo, o endereço e o telefone. Posteriormente imprima o resultado de cada variável linha abaixo de linha.

print ("=" * 40)

print ("* Seja Bem-Vindo Usuário!")
print ("* Porfavor, complete As Informações a Baixo: ")
    # Boas vindas ao usuário.

print ("=" * 40)

nome = input("Qual é o seu nome: ")
    # Nome Da Variável = nome.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

sexo = input("Qual é o seu sexo [M/F]: ")
    # Nome Da Variável = sexo.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

rua = input("Qual o nome da rua da sua residencia: ")
    # Nome Da Variável = rua.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

numero = int(input("Qual o numero da residencia: "))
    # Nome Da Variável = numero.
    # Tipo Da Variável = Int (inteiro)
        # Ex: 1, 34, -67, 92, -145.
    # Função = Entrada De Dados.

telefone = int(input("Qual o telefone para contato: "))
    # Nome Da Variável = telefone.
    # Tipo Da Variável = Int (Inteiro).
        # Ex: 5, 9, -12, -838, 71, 80.
    # Função = Entrada De Dados.

print ("=" * 40)

print ("Voçê se chama {}, é do sexo {}, mora na rua {} {}°, e o seu Telefone pra contato é o {}!".format(nome, sexo, rua, numero, telefone))
    # Apresentado As Informações Na Tela Para o Usuário Confirmar.
    # .format = formata o texto, alocando o valor de uma varivel no espaço: {}
        # Ex: .format(Nome_da_Variavel)

print ("=" * 40)

print("Informações Armazenadas No Sitema!")
print("Obrigado pelas informações {}! Até a Proxima!".format(nome))
    # Despedida Para o Usuário!

print ("=" * 40)