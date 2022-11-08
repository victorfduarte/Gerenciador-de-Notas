from telas import main_window
from dados.manager import Manager

gbd = Manager()
print(gbd.load_from_json('Materia'))
print(gbd.load_from_json('Avaliacao'))

main_window.create(gbd)

print(gbd.save_table('Materia'))
print(gbd.save_table('Avaliacao'))