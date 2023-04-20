# 77 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

print ("=" * 60)

print ("*** Contador De Consoantes ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

caract = []
    # Vetor
        # Comando para armazenar informacoes como uma lista

vogais = ["a","e","i","o","u"]
    # Vetor
        # Comando para armazenar informacoes como uma lista

contvogal = 0
    # Nome Da Variável = contvogal.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

x = 1
    # Nome Da Variável = x.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

while x <= 10:
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    entrada = input("* Caractere %d: " %x)
        # Nome Da Variável = entrada.
        # Tipo Da Variavel = Str (String).
        # Função = Atribuição De Valor.

    print ("=" * 60)

    x = x + 1
        # Nome Da Variável = x.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> x + 1

    caract.append(entrada)
        # Append = Acrecentar

    if entrada in vogais:

        contvogal = contvogal + 1
            # Nome Da Variável = contvogal.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> contvogal + 1

print ("- Consoantes: ",(len (caract)) - contvogal)
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)
   