# 80 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idade_1 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista
idade_2 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista
idade_3 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista
idade_4 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista
idade_5 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista

altura_1 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista
altura_2 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista
altura_3 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista
altura_4 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista
altura_5 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista

pessoa_1 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista
pessoa_2 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista
pessoa_3 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista
pessoa_4 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista
pessoa_5 = []
    # Vetor
        # Comando para armazenar informacoes como uma lista

contador = 0
    # Nome Da Variável = contador.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

while (contador < 1):
    
    print ("=" * 60)

    armazenamento_1 = int(input("* Digite a Idade Da 1° Pessoa: "))
        # Nome Da Variável = armazenamento_1.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

    armazenamento_2 = float(input("* Digite a Altura Da 1° Pessoa: "))
        # Nome Da Variável = armazenamento_2.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    contador += 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    idade_1.append(armazenamento_1)
        # Append = Acrecentar

    altura_1.append(armazenamento_2)
        # Append = Acrecentar

while (contador < 2):

    print ("=" * 60)

    armazenamento_1 = int(input("* Digite a Idade Da 2° Pessoa: "))
        # Nome Da Variável = armazenamento_1.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

    armazenamento_2 = float(input("* Digite a Altura Da 2° Pessoa: "))
        # Nome Da Variável = armazenamento_2.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    contador += 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    idade_2.append(armazenamento_1)
        # Append = Acrecentar

    altura_2.append(armazenamento_2)
        # Append = Acrecentar

while (contador < 3):

    print ("=" * 60)

    armazenamento_1 = int(input("* Digite a Idade Da 3° Pessoa: "))
        # Nome Da Variável = armazenamento_1.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

    armazenamento_2 = float(input("* Digite a Altura Da 3° Pessoa: "))
        # Nome Da Variável = armazenamento_2.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    contador += 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    idade_3.append(armazenamento_1)
        # Append = Acrecentar

    altura_3.append(armazenamento_2)
        # Append = Acrecentar

while (contador < 4):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    print ("=" * 60)

    armazenamento_1 = int(input("* Digite a Idade Da 4° Pessoa: "))
        # Nome Da Variável = armazenamento_1.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

    armazenamento_2 = float(input("* Digite a Altura Da 4° Pessoa: "))
        # Nome Da Variável = armazenamento_2.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    contador += 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    idade_4.append(armazenamento_1)
        # Append = Acrecentar

    altura_4.append(armazenamento_2)
        # Append = Acrecentar

while (contador < 5):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    print ("=" * 60)

    armazenamento_1 = int(input("* Digite a Idade Da 5° Pessoa: "))
        # Nome Da Variável = armazenamento_1.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

    armazenamento_2 = float(input("* Digite a Altura Da 5° Pessoa: "))
        # Nome Da Variável = armazenamento_2.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    contador += 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    idade_5.append(armazenamento_1)
        # Append = Acrecentar

    altura_5.append(armazenamento_2)
        # Append = Acrecentar

print ("=" * 60)

print ("*** Pessoas ***")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("- A idade Da 5° pessoa Digitada é de: {}".format(idade_5))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- A altura da 5° pessoa Digitada é de: {}".format(altura_5))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

print ("- A idade Da 4° pessoa Digitada é de: {}".format(idade_4))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- A altura da 4° pessoa Digitada é de: {}".format(altura_4))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

print ("- A idade Da 3° pessoa Digitada é de: {}".format(idade_3))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- A altura da 3° pessoa Digitada é de: {}".format(altura_3))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

print ("- A idade Da 2° pessoa Digitada é de: {}".format(idade_2))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- A altura da 2° pessoa Digitada é de: {}".format(altura_2))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

print ("- A idade Da 1° pessoa Digitada é de: {}".format(idade_1))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- A altura da 1° pessoa Digitada é de: {}".format(altura_1))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)












