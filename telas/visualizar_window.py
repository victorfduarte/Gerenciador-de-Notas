import PySimpleGUI as sg
from telas import adicionar_notas_window
from telas import adicionar_materia_window
from telas import editar_nota_window
from dados.base_table import TableClass
from dados.manager import Manager


def create(nome_materia: str):
    
    materia = gbd.get_table('Materia').get_elements_by(Nome=nome_materia)[0]
    print(materia.get_all_values())
    dias = materia.get_value('Dias').get()

    checked = sg.theme_button_color_background()
    unchecked = sg.theme_text_element_background_color()

    head = ['Av.', 'Nota', 'Data']
    valores = []

    fk = materia.get_value('Avaliacoes')
    print(f'{fk=}')
    for reg in fk.get():
        attrs = fk.get_table().get_element_by_pk(reg).to_dict()
        print(attrs)
        formato = (
            f'{attrs["Num_AV"]}°',
            f'{attrs["Nota"]:.1f}',
            f'{attrs["Data"]}',
        )
        valores.append(formato)
    
    valores.sort(key=lambda reg: int(reg[0][0]))

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
            enable_events=True, key='-TABLE-'
        )],
        [sg.Text('Média das notas:', font=font_normal,), sg.Text('', font=font_normal)],
        [sg.Button('Editar Matéria', font=font_button, key='-EDIT_MAT-'),
         sg.Button('Adicionar Nota', font=font_button,key='-ADD_NOTA-')],
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
        elif event == '-ADD_NOTA-':
            adicionar_notas_window.create(gbd, materia)

            valores = []

            fk = materia.get_value('Avaliacoes')
            print(f'{fk.get()=}')
            for reg in fk.get():
                attrs = fk.get_table().get_element_by_pk(reg).to_dict()
                print(attrs)
                formato = (
                    f'{attrs["Num_AV"]}°',
                    f'{attrs["Nota"]:.1f}',
                    f'{attrs["Data"]}',
                )
                valores.append(formato)
            
            valores.sort(key=lambda reg: int(reg[0][0]))
            
            window['-TABLE-'].update(values=valores)

        elif event == '-TABLE-':
            row_selected = values['-TABLE-'][0]

            num_av = int(valores[row_selected][0][0])
            materia_id = materia.get_pk().get()

            print(f'{num_av=}')
            print(f'{materia_id=}')
            print(
                gbd.get_table('Avaliacao').get_elements_by(
                    Num_AV=num_av, Materia=materia_id
                )
            )

            aval = gbd.get_table('Avaliacao').get_elements_by(
                Num_AV=num_av, Materia=materia_id
            )[0]
            print(aval)

            editar_nota_window.create(gbd, materia, aval)

            valores[row_selected] = (
                f'{aval.get_value("Num_AV").get()}°',
                f'{aval.get_value("Nota").get():.1f}',
                f'{aval.get_value("Data").get()}',
            )

            window['-TABLE-'].update(values=valores)


    window.close()
    return False


if __name__ == '__main__':
    create()