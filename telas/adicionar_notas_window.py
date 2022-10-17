import PySimpleGUI as sg
from dados.manager import Manager
from dados.tabelas import Avaliacao

def create(gbd: Manager, edit: bool = False, avaliacao: Avaliacao = None,
nome_materia: str = None):
    nota = ''
    aval = ''
    avs = [1, 2, 3, 4]
    materia = ''
    materias = list(
        map(lambda e: e.get_value('Nome'), gbd.get_table('Materia').get_elements())
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
            pass
    
    window.close()


if __name__ == '__main__':
    create(False, nota=8.0)