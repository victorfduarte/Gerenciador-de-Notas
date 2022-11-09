import PySimpleGUI as sg
from dados.manager import Manager
from dados import tabelas

def create(
        gbd: Manager, materia: tabelas.Materia, avaliacao: tabelas.Avaliacao
) -> 'tuple[int, str, str]':

    avs = [1, 2, 3, 4]

    nota = avaliacao.get_value('Nota').get()
    aval = avaliacao.get_value('Num_AV').get()
    data = avaliacao.get_value('Data').get()
    

    font_normal = ('Arial', 17)
    font_button = ('Arial', 14)
    font_title = ('Arial', 20, 'bold')

    layout = [
        [sg.Push(), sg.Text('EDTIANDO', font=font_title, border_width=25), sg.Push()],
        [sg.Text('Nota:', font=font_normal),
         sg.Input(nota, key='-NOTA-', size=(5, 1), font=font_normal), sg.Push(),
         sg.Text('Avaliação:', font=font_normal),
         sg.Combo(avs, aval, key='-AV-', size=(3, 1), font=font_normal)],
        [sg.Input(data, key='-DATA-', size=(21, 1), font=font_normal), sg.Push(),
         sg.CalendarButton('Data', '-DATA-', font=font_button, format='%a, %d %b %Y',
         locale='pt-BR')],
        [sg.HorizontalSeparator()],
        [sg.Button('Confirmar', key='-OK-', font=font_button),
         sg.Button('Cancelar', key='-CANCEL-', font=font_button),
         sg.Push(),
         sg.Button('Deletar', key='-DELETE-', font=font_button, button_color='#c4302b')
        ]
    ]
    

    window = sg.Window(
        'Editar Notas', layout, element_padding=7, element_justification='lef',
        modal=True
    )

    while True:
        event, values = window.read()
        print(event, values)

        if event == sg.WINDOW_CLOSED or event == '-CANCEL-':
            break

        elif event == '-OK-':
            nota: str = values['-NOTA-']
            aval: str = values['-AV-']
            data: str = values['-DATA-']

            if not nota:
                sg.popup_ok('A nota deve ser especificada', title='Error')
                continue
            if not aval:
                sg.popup_ok('A avaliação deve ser especificada', title='Error')
                continue
            if not data:
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
                          
            avaliacao.set_value(Nota=nova_nota, Num_AV=aval, Data=data)
            avaliacao.save()

            sg.popup_ok('A matéria foi atualizada com sucesso')

            break          
    
    window.close()


if __name__ == '__main__':
    create(False, nota=8.0)