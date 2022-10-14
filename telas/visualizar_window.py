import PySimpleGUI as sg
from telas import adicionar_notas_window
from telas import adicionar_materia_window
from dados.base_table import TableClass
from dados.manager import Manager


def create(gbd: Manager, nome_materia: str):
    
    materia = gbd.get_table('Materia').get_elements_by('Nome', nome_materia)[0]
    dias = getattr(materia, 'Dias').get()

    checked = sg.theme_button_color_background()
    unchecked = sg.theme_text_element_background_color()

    head = ['Av.', 'Nota', 'Data']
    valores = []

    for reg in getattr(materia, 'Avaliacoes').get():
        attrs = gbd.get_table('Avaliacao').get_element_by_pk(reg).to_dict()
        formato = (
            f'{attrs["Num_AV"]}°',
            f'{attrs["Nota"]}',
            f'{attrs["Data"]}',
        )
        valores.append(formato)

    font_normal = ('Arial', 17)
    font_bolder = ('Arial', 17, 'bold')
    font_button = ('Arial', 14)
    font_title = ('Arial', 20, 'bold')
    size_label_dia = (3, 1)

    layout = [
        [sg.Push(), sg.Push(), sg.Text(
            nome_materia, font=font_title, border_width=25
         ), sg.Push(), sg.Button('Voltar', font=font_button, key='-BACK-')],
        [sg.Text('Professor(a):', font=font_normal),
         sg.Text(getattr(materia, 'Prof').get(), font=font_bolder, )],
        [sg.HorizontalSeparator()],
        [sg.Push(),
         sg.Text(
            'Seg', font=font_normal, key='-SEG-', border_width=8, pad=3,
            size=size_label_dia, justification='c',
            background_color = checked if 'SEG' in dias else unchecked
         ), sg.Push(),
         sg.Text(
            'Ter', font=font_normal, key='-TER-', border_width=8, pad=3,
            size=size_label_dia, justification='c',
            background_color = checked if 'TER' in dias else unchecked
         ), sg.Push(),
         sg.Text(
            'Qua', font=font_normal, key='-QUA-', border_width=8, pad=3,
            size=size_label_dia, justification='c',
            background_color = checked if 'QUA' in dias else unchecked
         ), sg.Push(),
         sg.Text(
            'Qui', font=font_normal, key='-QUI-', border_width=8, pad=3,
            size=size_label_dia, justification='c',
            background_color = checked if 'QUI' in dias else unchecked
         ), sg.Push(),
         sg.Text(
            'Sex', font=font_normal, key='-SEX-', border_width=8, pad=3,
            size=size_label_dia, justification='c',
            background_color = checked if 'SEX' in dias else unchecked
         ), sg.Push()],
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

    '''
    text_dias = ('-SEG-', '-TER-', '-QUA-', '-QUI-', '-SEX-')
    for dia in getattr(materia, 'Dias'):
        for text_dia in text_dias:
            if dia == text_dia.strip('-'):
                window[text_dia].update(background_color=sg.theme_button_color()[1])
                break
    '''
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