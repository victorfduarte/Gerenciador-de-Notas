from telas import main_window
from dados.manager import Manager
from dados.tabelas import Materia, Avaliacao

print('Status de carregamento:')
Manager.set_stream(Materia, 'Materia.json')
Manager.set_stream(Avaliacao, 'Avaliacao.json')

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