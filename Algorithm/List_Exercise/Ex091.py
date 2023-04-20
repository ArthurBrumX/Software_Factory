# 91 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 
# (que não deve ser armazenado). Após esta entrada de dados, faça:

# • Mostre a quantidade de valores que foram lidos;
# • Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# • Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# • Calcule e mostre a soma dos valores;
# • Calcule e mostre a média dos valores;
# • Calcule e mostre a quantidade de valores acima da média calculada;
# • Calcule e mostre a quantidade de valores abaixo de sete;
# • Encerre o programacom uma mensagem;

print ("=" * 60)

print ("*** Notas ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

nota_alta = 0
    # Nome Da Variável = nota_alta.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

nota_baixa = 0
    # Nome Da Variável = nota_baixa.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

calculo = 0
    # Nome Da Variável = calculo.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

contador = 0 
    # Nome Da Variável = contador.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

notas = []

while True:
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    nota = float(input("* Digite a Nota: "))
        # Nome Da Variável = nota.
        # Tipo Da Variavel = Float (Real).
        # Função = Atribuição De Valor.

    if nota == -1:
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        break
            # Break = Quebre
    
    else:
        # Else = SeNão
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        notas.append(nota)
            # Append = Acressentar

        contador += 1
            # Nome Da Variável = contador.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> contador + 1

        calculo += nota
            # Nome Da Variável = calculo.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> calculo + nota

        media = calculo / contador
            # Nome Da Variável = media.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> calculo / contador
       
        if nota < 7:
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            nota_baixa += 1
                # Nome Da Variável = nota_baixa.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> nota_baixa + 1

for c in range(len(notas)):
    # For = Para

    if notas[c] >= media:
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        nota_alta +=1
            # Nome Da Variável = nota_alta.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> nota_alta + 1

print("=" * 60)

print("A quantidades de notas digitadas foi: {}".format(contador))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print("=" * 60)

print('Notas em Ordem Crescente:')  
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

for c in range(len(notas)):
    # For = Para

    print(f'{notas[c]}')
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print("=" * 60)

notas.reverse()
print('Notas em Ordem Decrescente:')
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

for c in range(len(notas)):
    # For = Para

    print(f'{notas[c]}')
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print("=" * 60)

print("A soma das notas da {}".format(calculo))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print("A média das notas da {}".format(media))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print("Notas acima da media: {}".format(nota_alta))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print("Notas abaixo abaixo: {}".format(nota_baixa))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print("=" * 60)
