import cryptocode
import os
import PySimpleGUI as sg


login = open('login.txt', 'r') # abre o arquivo login.txt em modo leitura
login_txt = login.readline() # lê o arquivo de texto na primeira linha e guarda ela na variavel "login_txt"
login = login_txt

def senha_trocada():
    sg.theme('DarkPurple4')
        
    result = [
        [sg.Text('Senha alterada com sucesso!')]
    ]

    layout = [
        [sg.Frame('', layout = result, size = (300, 75))],
    ]
    return sg.Window('Senha alterada!', layout = layout, finalize = True)

def senha_igual():
    sg.theme('DarkPurple4')
        
    result = [
        [sg.Text('As senhas são iguais')]
    ]

    layout = [
        [sg.Frame('', layout = result, size = (300, 75))],
    ]
    return sg.Window('Senhas iguais!', layout = layout, finalize = True)

def login_ou_senha_incorreto():
    sg.theme('DarkPurple4')
        
    result = [
        [sg.Text('Login ou Senha incorreto!')]
    ]

    layout = [
        [sg.Frame('', layout = result, size = (300, 75))],
    ]
    return sg.Window('Senha incorreta!', layout = layout, finalize = True)

class mudar_senha():
    def tela_mudar_senha1():
        sg.theme('DarkPurple4')
        
        result = [
            [sg.Text('Login:', size = (10)), sg.Input(key='login', size = (30, 76))],
            [sg.Text('Senha atual:', size = (10)), sg.Input(key='senha_atual', size = (30, 76))],
            [sg.Text('Senha nova:', size = (10)), sg.Input(key='senha_nova', size = (30, 76))],
            [sg.Button('Alterar Senha', size = (38))]
        ]

        layout = [
            [sg.Frame('', layout = result)],
        ]
        return sg.Window('Mudar Senha', layout = layout, finalize = True)

    global janela
    janela = tela_mudar_senha1()
    eventos, valores = janela.read()
    global senha_atual
    senha_atual = valores['senha_atual']
    global senha_nova
    senha_nova = valores['senha_nova']
    global input_login
    input_login = valores['login'] # precisamos criar uma validação de login para saber se ele é existente
    
    
    def change_pass(senha):
        senha_decript = cryptocode.decrypt(senha, senha_atual)
        login_decript = cryptocode.decrypt(login, input_login)
        if senha_decript == 'senha' and login_decript == 'login':
            nova_senha_encript = cryptocode.encrypt('senha', senha_nova)
            senha = open('senha.txt', 'r')
            senha.close()
            os.remove('senha.txt')
            senha = open('senha.txt', 'a')
            if senha_atual == senha_nova:
                janela = senha_igual()
                while True:
                    eventos, valores = janela.read()
                    if eventos == sg.WINDOW_CLOSED:
                        break
                    else:
                        break
            elif senha_atual and senha_nova != '': # caso o cliente coloque o valor direferente de uma str vazia
                senha.write(nova_senha_encript)
                janela = senha_trocada()
                while True:
                    eventos, valores = janela.read()
                    if eventos == sg.WINDOW_CLOSED:
                        break
                    else:
                        break
        else:
            janela = login_ou_senha_incorreto()
            while True:
                eventos, valores = janela.read()
                if eventos == sg.WINDOW_CLOSED:
                    break
                else:
                    break
            
