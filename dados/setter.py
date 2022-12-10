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
        with open(f'dados/jsons/{filename}.json', 'r', encoding='utf-8') as file:
            content = file.read()
        return json.loads(content)
    except FileNotFoundError:
        return ValueError(f'O arquivo {filename} não existe')


def mount(table: 'bt.Table', struct: dict):
    registros: 'list[dict[str]]' = struct['values']
    for reg in registros:
        print('Nova instância: ', table.init_from_db(**reg))


def dismount(table: 'bt.Table') -> dict:
    list_regs: 'list[dict[str]]' = []
    registros = table.get_elements()

    for reg in registros:
        list_regs.append(reg.to_dict())
    
    struct = {
        'header': table.get_header(),
        'values': list_regs
    }
    
    return struct