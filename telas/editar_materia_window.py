import PySimpleGUI as sg
from dados import Manager
from dados.tabelas import Materia, Professor


def create(materia: 'Materia'):
    font_normal = ('Arial', 17)
    font_button = ('Arial', 14)
    font_title = ('Arial', 20, 'bold')

    professores = Professor.get_elements()
    prof_nomes = list(map(lambda e: e.nome, professores))

    professor = Professor.get_by_pk(materia.id)
    prof_nome = professor.nome if professor else ''

    mat_nomes = list(map(lambda e: e.nome, Materia.get_elements()))

    layout = layout = [
        [sg.Push(),
         sg.Button('Deletar', font=font_button, key='-DEL-', button_color='#c4302b'),
         sg.Button('Editar', font=font_button, key='-OK-')],
        [sg.HorizontalSeparator()],
        [sg.Text('Matéria:', font=font_normal), sg.Push(),
         sg.Input(materia.nome, key='-NOME-', font=font_normal, size=(15, 1))],
        [sg.Text('Professor(a):', font=font_normal), sg.Push(),
         sg.Combo(prof_nomes, prof_nome, key='-PROF-', font=font_normal, size=(14, 1))],
        [sg.Text('Nota:', font=font_normal)],
        [sg.Multiline(materia.obs, font=font_normal, key='-OBS-', size=(27, 6))],
    ]

    window = sg.Window(
        'Editar Matéria',
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

            if values['-NOME-'] != materia.nome and values['-NOME-'] in mat_nomes:
                sg.popup_ok('Este nome já existe, coloque outro', title='Aviso')
                continue
            
            print(values['-PROF-'])
            print(f'{prof_nomes=}')
            
            if values['-PROF-'] and values['-PROF-'] not in prof_nomes:
                sg.popup_ok('Coloque o nome de um professor cadastrado', title='Aviso')
                continue
            
            materia.nome = values['-NOME-']
            materia.prof = values['-PROF-'] if values['-PROF-'] else None
            materia.obs = values['-OBS-']

            materia.save() 
            
            print('Alterado e salvo com sucesso')
            

            break

    print('Fechando Edit')
    window.close()


if __name__ == '__main__':
    create()
    pass
