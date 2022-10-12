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


def mount(self, cls: TableClass, struct: dict):
    header: 'list[str]' = struct['header']
    values: 'list[dict[str]]' = struct['values']

    for datadict in values:
        #print(datadict)
        c = cls(**datadict)

def dismount(self) -> dict:
    ...