import json
from . import base_table as bt


def save(filename: str, struct: dict):
    print(f'{struct=}')
    with open(f'dados/jsons/{filename}', 'w', encoding='utf-8') as file:
        text = json.dumps(struct, ensure_ascii=False, indent=4)
        print(f'{text=}')
        file.write(text)


def load(filename: str) -> dict:
    content = ''
    try:
        with open(f'dados/jsons/{filename}', 'r', encoding='utf-8') as file:
            content = file.read()
            print(f'{content=}')
        return json.loads(content)
    except FileNotFoundError:
        return ValueError(f'O arquivo {filename} não existe')


def mount(table: 'bt.Table', struct: dict):
    registros: 'list[list]' = struct['values']
    for reg in registros:
        pack = dict(zip(struct['header'], reg))
        print('Nova instância: ', end='')
        new_reg = table.init_from_db(**pack)
        print(new_reg)
        new_reg.save()


def dismount(table: 'bt.Table') -> dict:
    list_regs = list(
        map(
            lambda reg: tuple(reg.to_dict().values()),
            table.get_elements()
        )
    )
    
    struct = {
        'header': table.get_header(),
        'values': list_regs
    }
    
    return struct