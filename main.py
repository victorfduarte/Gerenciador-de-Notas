from dados.manager import Manager
from dados.tabelas import Materia

Manager.set_stream(Materia, 'Materia.json')

print('Status de carregamento:')
print('Status final:', Manager.load_from_json(Materia))

print(Materia.regs[1].get_all_values())

print(Materia.filter_by(nome='Português'))
