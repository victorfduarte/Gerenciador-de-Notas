import PySimpleGUI as sg

def create(edit: bool=False):
    avs = [1, 2]
    materias = ['Português', 'Matemática']

    font_normal = ('Arial', 17)
    font_button = ('Arial', 14)
    font_title = ('Arial', 20, 'bold')

    layout = [
        [sg.Push(), sg.Text(
            'EDITANDO' if edit else'NOVA NOTA', font=font_title, border_width=25
         ), sg.Push()],
        [sg.Text('Nota:', font=font_normal),
         sg.Input(key='-NOTA-', size=(5, 1), font=font_normal), sg.Push(),
         sg.Text('Avaliação:', font=font_normal),
         sg.Combo(avs, key='-AV-', size=(3, 1), font=font_normal)],
        [sg.Text('Matéria:', font=font_normal),
         sg.Combo(materias, key='-MAT-', expand_x=True, font=font_normal)],
        [sg.Input(key='-DATA-', size=(21, 1), font=font_normal), sg.Push(),
         sg.CalendarButton('Data', '-DATA-', font=font_button, format='%a, %d %b %Y',
         locale='pt-BR')],
        [sg.HorizontalSeparator()],
        [sg.Button('Confirmar', key='-OK-', font=font_button),
         sg.Button('Cancelar', key='-CANCEL-', font=font_button)]
    ]
    

    window = sg.Window(
        'Editar Notas', layout, element_padding=7,
        element_justification='lef', modal=True
    )

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WINDOW_CLOSED or event == '-CANCEL-':
            break
        elif event == '-EDIT-':
            window['-INPUT_AV-'].update(visible=False)
            window['-COMBO_AV-'].update(visible=True)
        elif event == '-NEW-':
            window['-INPUT_AV-'].update(visible=True)
            window['-COMBO_AV-'].update(visible=False)
    
    window.close()


if __name__ == '__main__':
    create()