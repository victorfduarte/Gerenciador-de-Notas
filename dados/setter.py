import json

try:
    from dados.base_table import TableClass
except ImportError:
    from base_table import TableClass


def save(filename: str, struct: dict):
    with open(filename, 'w') as file:
        file.write(json.dumps(struct))


def load(filename: str) -> dict:
    content = ''
    try:
        with open(f'dados/jsons/{filename}.json', 'r', encoding='utf-8') as file:
            content = file.read()
        return json.loads(content)
    except FileNotFoundError:
        return ValueError(f'O arquivo {filename} não existe')


def mount(table: TableClass, struct: dict):
    registros: 'list[dict[str]]' = struct['values']
    for reg in registros:
        table(**reg)


def dismount(table: TableClass) -> dict:
    list_regs: 'list[dict[str]]' = []
    registros = TableClass.get_elements()

    for reg in registros:
        list_regs.append(reg.to_dict())
    
    struct = {
        'header': TableClass.get_header(),
        'values': list_regs
    }
    
    return struct