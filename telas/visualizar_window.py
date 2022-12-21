import PySimpleGUI as sg
from . import adicionar_notas_window
from . import editar_materia_window
from . import editar_nota_window
from dados import Manager
from dados.tabelas import Materia, Avaliacao, Professor

font_normal = ('Arial', 17)
font_bolder = ('Arial', 17, 'bold')
font_button = ('Arial', 14)
font_title = ('Arial', 20, 'bold')


def render(nome_materia, nome_prof, obs_mat, avs_head, avs_values):
    print(obs_mat)
    layout = [
        [sg.Text(
            nome_materia, font=font_title, key='-MAT_NOME-'
         ), sg.Push(), sg.Button('Voltar', font=font_button, key='-BACK-')],
        [sg.HorizontalSeparator()],
        [sg.Text('Professor(a):', font=font_normal),
         sg.Text(nome_prof, font=font_bolder, key='-PROF-')],
        [sg.Text('Obs:', font=font_normal)],
        [sg.Push(), sg.Button('Editar', font=font_button, key='-EDIT_MAT-')],
        [sg.HorizontalSeparator()],
        [sg.Table(
            avs_values, avs_head, font=font_normal, hide_vertical_scroll=True,
            expand_x=True, num_rows=6, col_widths=(5, 6, 11), auto_size_columns=False,
            enable_events=True, key='-TABLE-'
        )],
        [sg.Text('Média das notas:', font=font_normal,), sg.Text('', font=font_normal)],
        [sg.Button('Adicionar Nota', font=font_button,key='-ADD_NOTA-')],
    ]

    return layout


def create(materia: Materia):
    print(materia)
    print(materia.get_all_values())

    nome_materia = materia.nome
    prof = Professor.get_by_pk(materia.prof)
    nome_prof = prof.nome if prof else ''

    checked = sg.theme_button_color_background()
    unchecked = sg.theme_text_element_background_color()

    head = ['Nota', 'Data']
    valores = []

    avs = Avaliacao.filter_by(materia=materia.get_pk())
    print(f'{avs=}')
    for reg in avs:
        print(f'{reg=}')
        attrs = reg.to_dict()
        print(f'{attrs=}')
        formato = (
            f'{attrs["Nota"]:.1f}',
            f'{attrs["Data"]}',
        )
        valores.append(formato)
    
    # valores.sort(key=lambda reg: int(reg[0][0]))

    layout = render(
        nome_materia,
        nome_prof,
        materia.obs,
        head,
        valores
    )

    window = sg.Window(
        'Visualizar Matéria',
        layout,
        size=(360, 550),
        element_padding=7,
        modal=True
    )

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            window.close()
            return True
        if event == '-BACK-':
            break
        elif event == '-EDIT_MAT-':
            editar_materia_window.create(materia)

            nome_materia = materia.nome
            prof = Professor.get_by_pk(materia.prof) if materia.prof else None
            nome_prof = prof.nome if prof else ''

            window['-MAT_NOME-'].update(nome_materia)
            window['-PROF-'].update(nome_prof)

            print('Layout atualizado')

        elif event == '-ADD_NOTA-':
            adicionar_notas_window.create(Manager, materia)

            valores = []

            avs = Avaliacao.filter_by(materia=materia.get_pk())
            print(f'{avs=}')
            for reg in avs:
                print(f'{reg=}')
                attrs = reg.to_dict()
                print(f'{attrs=}')
                formato = (
                    f'{attrs["Nota"]:.1f}',
                    f'{attrs["Data"]}',
                )
                valores.append(formato)
            
            # valores.sort(key=lambda reg: int(reg[0][0]))
            
            window['-TABLE-'].update(values=valores)

        elif event == '-TABLE-':
            row_selected = values['-TABLE-'][0]

            num_av = int(valores[row_selected][0][0])
            materia_id = materia.get_pk().get()

            print(f'{num_av=}')
            print(f'{materia_id=}')
            print(
                Manager.get_table('Avaliacao').get_elements_by(
                    Num_AV=num_av, Materia=materia_id
                )
            )

            aval = Manager.get_table('Avaliacao').get_elements_by(
                Num_AV=num_av, Materia=materia_id
            )[0]
            print(aval)

            editar_nota_window.create(Manager, materia, aval)

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