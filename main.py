import inspect

from telas import main_window
from dados.manager import Manager
from dados import tabelas
from dados.tabelas import Materia, Avaliacao
from dados import settings

print('Status de carregamento:')
tables = dict(inspect.getmembers(tabelas, inspect.isclass))
print(tables)

for table_name, file in settings['streams'].items():
    Manager.set_stream(tables[table_name], file)

status_mat = Manager.load_from_json(Materia)
status_ava = Manager.load_from_json(Avaliacao)

print('Status de Materia:', status_mat)
print('Status de Avaliacao:', status_ava)

print('Rodando...')
status = main_window.create()
print('Status final:', status)

print('Status de salvamento final:')
Manager.save_table(Materia)
Manager.save_table(Avaliacao)
print('Status final: OK')

print('Finalizou!')