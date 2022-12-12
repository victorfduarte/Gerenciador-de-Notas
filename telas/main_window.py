import PySimpleGUI as sg
from telas import visualizar_window
from telas import adicionar_materia_window
from telas import tabela_notas_window
from dados.manager import Manager

def create():
    table_materia = Manager.get_table('Materia')
    nomes_materias = list(map(
        lambda e: e.get_value('Nome').get(), table_materia.get_elements()
    ))

    font_normal = ('Arial', 17)
    font_button = ('Arial', 14)
    font_title = ('Arial', 20, 'bold')

    layout = [
        [sg.Push(), sg.Text('Gerenciador de Notas', font=font_title, border_width=25),
         sg.Push()],
        [sg.Text('Matérias', font=font_normal), sg.Push(),
         sg.Button('Visualizar', font=font_button, key='-VIEW-'),
         sg.Button('Adicionar', font=font_button, key='-ADD-')],
        [sg.Listbox(
            nomes_materias, nomes_materias[0], key='-LIST_MATERIAS-', font=font_normal,
            size=(None, 8), expand_x=True
        )],
        [sg.Button('Mostrar Tabela de Notas', font=font_button, key='-TABLE-')]
    ]

    window = sg.Window('Gerenciador de Notas', layout, element_padding=7)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-VIEW-':
            window.hide()
            visualizar_window.create(Manager, values['-LIST_MATERIAS-'][0])
            window.un_hide()
        elif event == '-ADD-':
            adicionar_materia_window.create()
        elif event == '-TABLE-':
            tabela_notas_window.create()

    window.close()


if __name__ == '__main__':
    create()