import PySimpleGUI as sg
from dados import Manager
from dados.tabelas import Materia, Professor


def render_layout(
        btn_confirm_name: str = '', materia_nome: str = '', combo_prof: list = ...,
        obs_text: str  = '', font_button: tuple = None, font_normal: tuple = None
) -> list:
    if combo_prof == ...:
        combo_prof = []

    layout = [
        [sg.Push(), sg.Button(btn_confirm_name, font=font_button, key='-OK-')],
        [sg.HorizontalSeparator()],
        [sg.Text('Matéria:', font=font_normal), sg.Push(),
         sg.Input(materia_nome, key='-NOME-', font=font_normal, size=(15, 1))],
        [sg.Text('Professor(a):', font=font_normal), sg.Push(),
         sg.Combo(combo_prof, key='-PROF-', font=font_normal, size=(14, 1))],
        [sg.Text('Nota:', font=font_normal)],
        [sg.Multiline(obs_text, font=font_normal, key='-OBS-', size=(27, 6))],
    ]

    return layout


def create(edit: bool = False, materia: Materia = None):
    font_normal = ('Arial', 17)
    font_button = ('Arial', 14)
    font_title = ('Arial', 20, 'bold')

    professores = Professor.get_elements()
    prof_nomes = list(map(lambda e: e.nome, professores))

    layout: list

    if edit:
        layout = render_layout(
            'Editar',
            materia.nome,
            prof_nomes,
            materia.obs,
            font_button,
            font_normal
        )
    else:
        layout = render_layout(
            'Criar',
            combo_prof = prof_nomes,
            font_button = font_button,
            font_normal = font_normal
        )

    window = sg.Window(
        'Editar Nota' if edit else 'Criar Nota',
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
                sg.popup_ok('Especifique o nome nda matéria', title='Aviso')
                continue

            new_mat = Materia(
                nome=values['-NOME-']
            )
            new_mat.save()
            
            print('Criado e salvo')

            break 
    
    window.close()


if __name__ == '__main__':
    create()
    pass
