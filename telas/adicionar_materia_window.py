import PySimpleGUI as sg

def create(edit: bool=False):
    avs = [1, 2]

    font_normal = ('Arial', 17)
    font_button = ('Arial', 14)
    font_title = ('Arial', 20, 'bold')

    layout = [
        [sg.Push(), sg.Text(
            'EDITANDO' if edit else 'NOVA MATÉRIA', font=font_title, border_width=25
        ), sg.Push()],
        [sg.Text('Matéria:', font=font_normal), sg.Push(),
         sg.Input(key='-NOME-', font=font_normal, size=(15, 1))],
        [sg.Text('Professor(a):', font=font_normal), sg.Push(),
         sg.Input(key='-PROF-', font=font_normal, size=(15, 1))],
        [sg.Checkbox('S', font=font_normal, key='-SEG-'), sg.Push(),
         sg.Checkbox('T', font=font_normal, key='-TER-'), sg.Push(),
         sg.Checkbox('Q', font=font_normal, key='-QUA-'), sg.Push(),
         sg.Checkbox('Q', font=font_normal, key='-QUI-'), sg.Push(),
         sg.Checkbox('S', font=font_normal, key='-SEX-')],
        [sg.HorizontalSeparator()],
        [sg.Button('Confirmar', font=font_button, key='-OK-'),
         sg.Button('Cancelar', font=font_button, key='-CANCEL-')]
    ]

    window = sg.Window(
        'Editar Notas', layout, element_padding=7, element_justification='l',
        modal=True
    )

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WINDOW_CLOSED or event == '-CANCEL-':
            break
    
    window.close()


if __name__ == '__main__':
    create()
    pass
