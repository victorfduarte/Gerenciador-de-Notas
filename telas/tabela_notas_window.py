import PySimpleGUI as sg


def create():
    values = [
        ['Português', '8.0', '8.0', '--', '8.0', '8.0', '--']
    ]

    head = ['Matérias', '1°', '2°', 'R1', '3°', '4°', 'RF']

    font_normal = ('Arial', 17)
    font_button = ('Arial', 14)
    font_title = ('Arial', 20, 'bold')

    layout = [
        [sg.Table(
            values=values,
            headings=head,
            auto_size_columns=True,
            hide_vertical_scroll=True,
            num_rows=13,
            font=font_normal,
            justification='center'),
        ]
    ]

    window = sg.Window('Tabela de Notas', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == '__main__':
    create()