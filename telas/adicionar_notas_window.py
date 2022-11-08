import PySimpleGUI as sg
from dados.manager import Manager
from dados.tabelas import Avaliacao

def create(
        gbd: Manager, edit: bool = False, avaliacao: Avaliacao = None,
        nome_materia: str = None
) -> 'tuple[int, str, str]':
    nota = ''
    aval = ''
    avs = [1, 2, 3, 4]
    materia = nome_materia
    materias = list(
        map(lambda e: e.get_value('Nome').get(), gbd.get_table('Materia').get_elements())
    )
    data = ''
    header = 'NOVA NOTA'
    title = 'Adicionar Nota'

    if edit:
        nota = avaliacao.get_value('Nota').get()
        aval = avaliacao.get_value('Num_AV').get()
        materia = nome_materia
        data = avaliacao.get_value('Data').get()
        header = 'EDITANDO'
        title = 'Editar Notas'
    

    font_normal = ('Arial', 17)
    font_button = ('Arial', 14)
    font_title = ('Arial', 20, 'bold')

    layout = [
        [sg.Push(), sg.Text(header, font=font_title, border_width=25), sg.Push()],
        [sg.Text('Nota:', font=font_normal),
         sg.Input(nota, key='-NOTA-', size=(5, 1), font=font_normal), sg.Push(),
         sg.Text('Avaliação:', font=font_normal),
         sg.Combo(avs, aval, key='-AV-', size=(3, 1), font=font_normal)],
        [sg.Text('Matéria:', font=font_normal),
         sg.Combo(materias, materia, key='-MAT-', expand_x=True, font=font_normal)],
        [sg.Input(data, key='-DATA-', size=(21, 1), font=font_normal), sg.Push(),
         sg.CalendarButton('Data', '-DATA-', font=font_button, format='%a, %d %b %Y',
         locale='pt-BR')],
        [sg.HorizontalSeparator()],
        [sg.Button('Confirmar', key='-OK-', font=font_button),
         sg.Button('Cancelar', key='-CANCEL-', font=font_button)]
    ]
    

    window = sg.Window(
        title, layout, element_padding=7, element_justification='lef', modal=True
    )

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WINDOW_CLOSED or event == '-CANCEL-':
            break
        elif event == '-OK-':
            nota: str = values['-NOTA-']
            aval: str = values['-AV-']
            materia: str = values['-MAT-']
            data: str = values['-DATA-']

            if not nota:
                sg.popup_ok('A nota deve ser especificada', title='Error')
                continue
            elif not aval:
                sg.popup_ok('A avaliação deve ser especificada', title='Error')
                continue
            elif not materia:
                sg.popup_ok('A materia deve ser especificada', title='Error')
                continue
            elif not data:
                sg.popup_ok('A data deve ser especificada', title='Error')
                continue
            
            try:
                nova_nota = round(float(nota), 1)
                if nova_nota < 0:
                    print('inválido')
                    sg.popup_ok('A nota deve ser um número válido', title='Error')
                    continue
            except ValueError:
                sg.popup_ok('A nota deve ser um número', title='Error')
                continue
            
            if int(aval) not in (1, 2, 3, 4):
                sg.popup_ok('A avaliação deve um valor válido', title='Error')
                continue
            elif materia not in materias:
                sg.popup_ok('A materia deve ser um valor listado', title='Error')
                continue

            materia_id = gbd.get_table('Materia').get_elements_by(Nome=materia)[0].get_pk().get()
            
            avaliacao.set_value(Nota=nova_nota, Num_AV=aval, Materia=materia_id, Data=data)
            avaliacao.save()

            sg.popup_ok('A matéria foi atualizada com sucesso')

            break
    
    window.close()


if __name__ == '__main__':
    create(False, nota=8.0)