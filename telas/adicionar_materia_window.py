import PySimpleGUI as sg
from dados import Manager
from dados.tabelas import Materia, Professor


def create():
    font_normal = ('Arial', 17)
    font_button = ('Arial', 14)
    font_title = ('Arial', 20, 'bold')

    professores = Professor.get_elements()
    prof_nomes = list(map(lambda e: e.nome, professores))

    layout = [
        [sg.Push(), sg.Button('Criar', font=font_button, key='-OK-')],
        [sg.HorizontalSeparator()],
        [sg.Text('Matéria:', font=font_normal), sg.Push(),
         sg.Input(key='-NOME-', font=font_normal, size=(15, 1))],
        [sg.Text('Professor(a):', font=font_normal), sg.Push(),
         sg.Combo(prof_nomes, key='-PROF-', font=font_normal, size=(14, 1))],
        [sg.Text('Nota:', font=font_normal)],
        [sg.Multiline(font=font_normal, key='-OBS-', size=(27, 6))],
    ]

    window = sg.Window(
        'Criar Matéria',
        layout,
        element_padding=7,
        element_justification='l',
        modal=True
    )

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WINDOW_CLOSED or event == '-CANCEL-':
            break

        if event == '-OK-':
            if values['-NOME-'].strip() == '':
                sg.popup_ok('Especifique o nome da matéria', title='Aviso')
                continue

            new_mat = Materia(
                nome=values['-NOME-'],
                obs=values['-OBS-']
            )
            new_mat.save()
            
            print('Criado e salvo')

            break 
    
    window.close()


if __name__ == '__main__':
    create()
    pass
