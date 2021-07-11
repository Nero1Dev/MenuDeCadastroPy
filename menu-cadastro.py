import PySimpleGUI
import pyautogui

# Layout
PySimpleGUI.theme('Reddit')
layout = [
    [PySimpleGUI.Text('Usuário:'),PySimpleGUI.Input(key='usuario',size=(20, 1))],
    [PySimpleGUI.Text('Senha:  '),PySimpleGUI.Input(key='senha',password_char='*',size=(20, 1))],
    [PySimpleGUI.Checkbox('Salvar o Login?')],
    [PySimpleGUI.Button('Entrar')]
]
# Janela
janela = PySimpleGUI.Window('Tela de Login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == PySimpleGUI.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Usuario' and valores['senha'] == '1234':
            pyautogui.alert('Olá, Login efetuado com sucesso')
            
        else:
            pyautogui.alert('Usuário ou Senha incorretos! Tente novamente')        
