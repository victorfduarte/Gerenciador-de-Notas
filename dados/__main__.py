from . import settings
import sys
import os
import json
import inspect

settings['show_log'] = False

from . import tabelas
from . import manager


def set_stream(args, force=False):
    table = settings['streams'].get(args[3], ValueError)
    
    if not force:
        if table != ValueError:
            print('O stream com esta classe já foi definido')
            print('Deseja refazer com este novo arquivo?[s/n]: ')

            if input().lower() != 's':
                exit()
    
    settings['streams'][args[3]] = args[2]

    with open('dados/settings.json', 'w', encoding='utf-8') as file:
        filestr = json.dumps(settings, indent=4, ensure_ascii=False)
        file.write(filestr)



def init_json_table(args):
    if len(args) < 4:
        print('Número de argumentos inválido.')
        print('Entre com o nome do arquivo e o nome da tabela')
        exit()
    
    file_json = args[2]
    tabela_nome = args[3]

    tabela = dict(inspect.getmembers(tabelas)).get(tabela_nome, ValueError)

    if tabela == ValueError:
        print('A tabela especificada não existe!')
        exit()

    if os.path.isfile(f'dados/jsons/{file_json}'):
        print(f'O arquivo {file_json} já existe.')
        print('Deseja sobrescrever e zerar o arquivo? [s/n]: ', end='')

        if input().lower() != 's':
            print('Operação Cancelada')
            exit()

    struct = {
        'header': tabela._header,
        'values':[]
    }

    with open(f'dados/jsons/{file_json}', 'x', encoding='utf-8') as file:
        filestr = json.dumps(struct, indent=4)
        file.write(filestr)
    
    set_stream(args, True)



if len(sys.argv) < 2:
    print('Digite algum comando ou help para conhecer os comandos')
    exit()

if sys.argv[1] == 'init_json_table':
    init_json_table(sys.argv)

elif sys.argv[1] == 'set_stream':
    set_stream(sys.argv)

else:
    print('comando desconhecido')
