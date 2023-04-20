# 27 - O departamento de Educação Física deseja informatizar este setor e colocou à disposição os seguintes dados de 50 alunos:

# Matrícula, sexo (M, F), altura (cm) e status físico (1–bom, 2–regular, 3–ruim)

# Estes dados deverão ser lidos através de uma unidade de entrada qualquer.

# Calcular e imprimir:

# a) A quantidade de alunos do sexo feminino com altura superior a 170 cm.

# b) A % de alunos do sexo masculino (em relação ao total de alunos do sexo masculino) cujo status físico seja bom.

print ("=" * 60)

print ("*** Departamento De Educação Fisica ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("** Caixa **")
    # Apresentação Ao Usuário.

print ("=" * 60)


aluno = 0
    # Nome Da Variável = aluno.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

total_de_mulheres = 0
    # Nome Da Variável = total_de_mulheres.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

total_de_mulheres_altas = 0
    # Nome Da Variável = total_de_mulheres_altas.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

total_de_homens = 0
    # Nome Da Variável = total_de_homens.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

# ================================

bons = 0
    # Nome Da Variável = bons.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

porcentagem = 0
    # Nome Da Variável = porcentagem.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

# ================================


while aluno < 2:
    # while = enquanto
        # enquanto Essa Condição não for Atendida, Execute o Código Abaixo.

    sexo = input("* Digite seu sexo: ")
        # Nome Da Variável = sexo.
        # Tipo Da Variavel = Str (String).
        # Função = Entrada De Dados.

    altura = float(input("* Digite a altura: "))
        # Nome Da Variável = altura.
        # Tipo Da Variavel = Float (Real).
        # Função = Entrada De Dados.

    status = int(input("* Digite o status: "))
        # Nome Da Variável = status.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Entrada De Dados.

    if (sexo == "F") or (sexo == "f") or (sexo == "Feminino") or (sexo == "feminino"):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        if (altura >= 1.70):
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            total_de_mulheres = total_de_mulheres + 1
                # Nome Da Variável = total_de_mulheres.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> total_mulheres + 1 

            total_de_mulheres_altas = total_de_mulheres_altas + 1
                # Nome Da Variável = total_de_mulheres_altas.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> total_mulheres + 1 

        elif (altura < 1.70):
            # Elif = Senão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
            
            total_de_mulheres = total_de_mulheres + 1
                # Nome Da Variável = total_de_mulheres.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> total_mulheres + 1 

    elif (sexo == "M") or (sexo == "m") or (sexo == "Masculino") or (sexo == "masculino"):
        # Elif = Senão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        if (status == 1):
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            bons = bons + 1
                # Nome Da Variável = bons.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> bons + 1 

            porcentagem = total_de_homens * 50 / 100
                # Nome Da Variável = porcentagem.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> total_de_homens * 50 / 100

            total_de_homens = total_de_homens + 1
                # Nome Da Variável = total_de_homens.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> total_de_homens + 1 

        elif (status != 1 ):
            # Elif = Senão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            total_de_homens = total_de_homens + 1
                # Nome Da Variável = total_de_homens.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> total_de_homens + 1 

    aluno = aluno + 1
        # Nome Da Variável = alunos.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> aluno + 1 

print ("=" * 60)

print ("- Total de mulheres altas: {}!!".format(total_de_mulheres_altas))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Total de homens {}!!".format(porcentagem))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)