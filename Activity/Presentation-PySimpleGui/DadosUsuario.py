import PySimpleGUI as sg
#Importando a biblioteca
class telaPython:
    def __init__(self):
        # layout
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais Provedores de e-mail são aceitos: ')],
            [sg.Checkbox('Gmail',key='gmail'), sg.Checkbox('outlook',key='outlook'), sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita Cartao')],
            [sg.Radio('Sim','Cartoes',key='aceitacartao'), sg.Radio('Não','Cartoes',key='naoaceitacartao')],
            [sg.Button('Enviar Dados')],
        ]
        # janela
        self.janela = sg.Window("Dados do usuario").layout(layout)
        # Extrair os dados da tela

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitacartao']
            nao_aceita_cartao = self.values['naoaceitacartao']

            print (f'nome: {nome}')
            print (f'idade: {idade}')
            print (f'Aceita gmail: {aceita_gmail}')
            print (f'Aceita outlook: {aceita_outlook}')
            print (f'Aceita yahoo: {aceita_yahoo}')
            print (f'Aceita Cartao: {aceita_cartao}')
            print (f'Nao aceita Cartao: {nao_aceita_cartao}')

tela = telaPython()
tela.Iniciar()