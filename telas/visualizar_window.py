import PySimpleGUI as sg
from telas import adicionar_notas_window
from telas import adicionar_materia_window

def create():
    notas = [(1, 10.0), (2, 5.0)]

    font_normal = ('Arial', 17)
    font_bolder = ('Arial', 17, 'bold')
    font_button = ('Arial', 14)
    font_title = ('Arial', 20, 'bold')

    head = ['Av.', 'Nota', 'Data']
    valores = [
        ['1°', '10,0', '10 Mai 2022'],
        ['2°', '8,0', '10 Out 2022'],
    ]

    layout = [
        [sg.Push(), sg.Push(), sg.Text('Matéria', font=font_title, border_width=25),
         sg.Push(), sg.Button('Voltar', font=font_button, key='-BACK-')],
        [sg.Text('Professor(a):', font=font_normal),
         sg.Text('Alexandre', font=font_bolder, )],
        [sg.HorizontalSeparator()],
        [sg.Text('Seg', font=font_normal, key='-SEG-', border_width=6), sg.Push(),
         sg.Text('Ter', font=font_normal, key='-TER-', border_width=6), sg.Push(),
         sg.Text('Qua', font=font_normal, key='-QUA-', border_width=6), sg.Push(),
         sg.Text('Qui', font=font_normal, key='-QUI-', border_width=6), sg.Push(),
         sg.Text('Sex', font=font_normal, key='-SEX-', border_width=6)],
        [sg.HorizontalSeparator()],
        [sg.Table(
            valores, head, font=font_normal, hide_vertical_scroll=True, expand_x=True,
            num_rows=6, col_widths=(5, 6, 11), auto_size_columns=False,
            enable_click_events=True, key='-TABLE-'
        )],
        [sg.Text('Média das notas:', font=font_normal,), sg.Text('', font=font_normal)],
        [sg.Button('Editar Matéria', font=font_button, key='-EDIT_MAT-'),
         sg.Button('Adicionar Nota', font=font_button,key='-EDIT_NOTA-')],
    ]

    window = sg.Window('Visualizar Matéria', layout, element_padding=7, modal=True)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            window.close()
            return True
        if event == '-BACK-':
            break
        elif event == '-EDIT_MAT-':
            adicionar_materia_window.create(True)
        elif event == '-EDIT_NOTA-':
            adicionar_notas_window.create()
        elif event == '-TABLE-':
            adicionar_notas_window.create(True)

    window.close()
    return False


if __name__ == '__main__':
    create()