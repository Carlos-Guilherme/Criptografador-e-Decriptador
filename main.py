import cryptocode
import PySimpleGUI as sg
import os
import pyaes



login = open('login.txt', 'r') # abre o arquivo login.txt em modo leitura
login_txt = login.readline() # lê o arquivo de texto na primeira linha e guarda ela na variavel "login_txt"
login = login_txt # é criado uma variavel e armazenado o dado extraido do arquivo de texto, no momento ainda criptografado

senha = open('senha.txt', 'r')
senha_txt = senha.readline()
senha = senha_txt


def login_invalido():
    sg.theme('DarkPurple4')
    
    result = [
        [sg.Text('Login invalido!')]
    ]

    layout = [
        [sg.Frame('', layout = result)],
    ]
    return sg.Window('Login invalido', layout = layout, finalize = True)


def tela_login():
    sg.theme('DarkPurple4')
    
    result = [
        [sg.Text('Login', size = (5)), sg.Input(key='input_login', size = (31, 76))],
        [sg.Text('Senha', size = (5)), sg.Input(key='input_senha', password_char='*', size = (31, 76))],
        [sg.Button(f'Login', size = (34))],
        [sg.Button(f'Mudar Senha', size = (34))]
        
    ]

    layout = [
        [sg.Frame('', layout = result)],
    ]
    return sg.Window('Login', layout = layout, finalize = True)

janela = tela_login()

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Login':
        input_login = valores['input_login'] # pega valores de login e armazena numa variavel
        input_senha = valores['input_senha']
        login_decript = cryptocode.decrypt(login, input_login)
        senha_decript = cryptocode.decrypt(senha, input_senha)
        if login_decript == 'login' and senha_decript == 'senha':
            import lock_files
            lock_files.lock_and_unlock() # aqui ele ja mostra um menu para criptografar e descrptografar com PysimpleGui
        else:
            login_invalido()
    elif eventos == 'Mudar Senha':
        janela.close()
        from change_pass import mudar_senha
        mudar_senha.change_pass(senha)
    elif eventos == 'Criar Acesso':
        # (EM CRIAÇÃO) criar um metodo para criar acessos
        break
