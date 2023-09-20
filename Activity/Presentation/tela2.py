from PySimpleGUI import Window, Button

layout = [
    [Button('Botão 1'), Button('Coluna 1')],
    [Button('Botão 2'), Button('Coluna 2')],
    [Button('Botão 3'), Button('Coluna 3')],
    [Button('Botão 4'), Button('Coluna 4')],
    [Button('Botão 5'), Button('Coluna 5')],
    [Text('Aperte o Botao 3: '), Button('Botão 3')],
]

Window = Window(
    'Janela de exemplo',
    layout=layout
)

Window.read() # vai ler qualquer interacao com widget que aconter 
Window.clase()