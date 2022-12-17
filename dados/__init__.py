__all__ = ['manager', 'tabelas']

import json

settings: dict

with open('dados/settings.json', 'r', encoding='utf-8') as file:
    filestr = file.read()
    settings = json.loads(filestr)

from .manager import Manager