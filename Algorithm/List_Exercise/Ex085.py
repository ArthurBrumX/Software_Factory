# 85 - Escrever um algoritmo para ler a quantidade de horas/aula de duas professor e o valor por hora recebido por cada uma. Mostrar na tela qual dos professores tem salário 
# total maior.

print ("=" * 60)

print ("*** Salário Professor! ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

horas_prof1 = float(input("* 1° Professor: Digite Quantas Horas Foram Trabalhadas: "))
    # Nome Da Variável = horas_prof1.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

valor_hora_1 = float(input("* 1° Professor: Digite o Valor Por Hora/Aula: R$"))
    # Nome Da Variável = valor_hora_1.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

print ("=" * 60)

horas_prof2 = float(input("* 2° Professor: Digite Quantas Horas Foraram Trabalhadas: "))
    # Nome Da Variável = horas_prof2.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

valor_horas_2 = float(input("* 2° professor: Digite o Valor Por Hora/Aula: R$"))
    # Nome Da Variável = valor_horas_2.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

print ("=" * 60)

val_dia_prof1 = horas_prof1 * valor_hora_1
    # Nome Da Variável = val_dia_prof1.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> horas_prof1 * (Valor da Variável: ) -> valor_hora_1

val_dia_prof2 = horas_prof2 * valor_horas_2
    # Nome Da Variável = val_dia_prof2.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> horas_prof2 * (Valor da Variável: ) -> valor_hora_2

print ("- O Valor Do Dia Trabalhado Do Professor N° 1 é De: R$ {}".format(val_dia_prof1))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- O Valor Do Dia Trabalhado Do Professor N° 2 é De: R$ {}".format(val_dia_prof2))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

sal_1 = val_dia_prof1 * 22
    # Nome Da Variável = sal_1.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> val_dia_prof1 * 22

sal_2 = val_dia_prof2 * 22
    # Nome Da Variável = sal_2.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> val_dia_prof2 * 22

print ("=" * 60)

print ("- O Salário Mensal Do Professor N° 1 é De: R${}".format(sal_1))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- O Salário Mensal Do Professor N° 2 é De: R${}".format(sal_2))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

if (sal_1 > sal_2):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- O Maior Salário é Do Professor N° 1")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

elif (sal_2 > sal_1):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- O Maior Salário é Do Professor N° 2")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("=" * 60)