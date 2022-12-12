import json
from . import base_table as bt


def save(filename: str, struct: dict):
    print(struct)
    with open(f'dados/jsons/{filename}.json', 'w', encoding='utf-8') as file:
        text = json.dumps(struct, ensure_ascii=False)
        print(text)
        file.write(text)


def load(filename: str) -> dict:
    content = ''
    try:
        with open(f'dados/jsons/{filename}', 'r', encoding='utf-8') as file:
            content = file.read()
        return json.loads(content)
    except FileNotFoundError:
        return ValueError(f'O arquivo {filename} não existe')


def mount(table: 'bt.Table', struct: dict):
    registros: 'list[list]' = struct['values']
    for reg in registros:
        pack = dict(zip(struct['header'], reg))
        print('Nova instância: ', end='')
        print(table.init_from_db(**pack))


def dismount(table: 'bt.Table') -> dict:
    list_regs: 'list[list]' = []
    registros = table.get_elements()

    for reg in registros:
        list_regs.append(list(reg.to_dict().values()))
    
    struct = {
        'header': table.get_header(),
        'values': list_regs
    }
    
    return struct