import PySimpleGUI as sg
import glob

def main():
    sg.theme('DarkPurple4')
    
    result = [
        [sg.Text('DIGITE O NOME DO ARQUIVO:')], 
        [sg.Input(key = 'arquivo', size = 40)],
        [sg.Button('INDEXAR ARQUIVO', size = (35))],
        [sg.Button('LISTAR ARQUIVOS', size = 35)],
        [sg.Button('CRIPTOGRAFAR', size = (16)), sg.Button('DESCRIPTOGRAFAR', size = (17))],
        
    ]

    layout = [
        [sg.Frame('', layout = result, key = 'container')],
    ]
    return sg.Window('Listagem', layout = layout, finalize = True)
janela = main()


class lock_and_unlock():

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        elif eventos == 'CRIPTOGRAFAR':
            file_name = valores['arquivo']
            if file_name in glob.glob('*.*'):
                from lock import lock_or_unlock
                lock_or_unlock.lock(file_name)
                janela.extend_layout(janela['container'], [[sg.Text(f'O arquivo "{file_name}" foi Criptografado')]])
            else:
                print('esse arquivo não existe')
        elif eventos == 'DESCRIPTOGRAFAR':
            file_name = valores['arquivo']
            if file_name in glob.glob('*.*'):
                from lock import lock_or_unlock
                lock_or_unlock.unlock(file_name)
                janela.extend_layout(janela['container'], [[sg.Text(f'O arquivo "{file_name}" foi Descriptografado')]])
            else:
                print('esse arquivo não existe')
        elif eventos == 'LISTAR ARQUIVOS':
            for file in glob.glob('*.*'):
                janela.extend_layout(janela['container'], [[sg.Text(file)]])
        elif eventos == 'INDEXAR ARQUIVO':
            file_name = valores['arquivo']
            if file_name in glob.glob('*.*'):
                janela.extend_layout(janela['container'], [[sg.Text(f'"{file_name}" FOI INDEXADO')]])
            else:
                print('esse arquivo não existe')
        
    
            
