import PySimpleGUI as sg

class telaPython:
    def __init__(self):
        # layout
        layout = [
            [sg.Text('Nome'),sg.Input()],
            [sg.Text('Idade'),sg.Input()],
            [sg.Checkbox('Gmail'), sg.Checkbox('Outlook'), sg.Checkbox('Yahoo')],
            [sg.Button('Enviar Dados')],
        ]
        # janela
        janela = sg.Window("Dados do usuario").layout(layout)
        # Extrair os dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print (self.values)

tela = telaPython()
tela.Iniciar()