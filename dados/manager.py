
import inspect

from . import tabelas as tbl
from . import base_table as bt
from . import setter as setter

class Manager:
    tabelas: 'dict[str, bt.Table]' = dict(
            (c for c in inspect.getmembers(tbl, inspect.isclass))
        )
    streams: 'dict[bt.Table, str]'= {}
    

    @classmethod
    def set_stream(cls, table: 'bt.Table', filename: str):
        if table not in cls.streams.keys():
            cls.streams.setdefault(table, filename)

    @classmethod
    def load_from_json(cls, table: 'bt.Table') -> 'ValueError | None':
        filename = cls.streams.get(table, None)

        if filename == None:
            return ValueError('o argumento filename nunca foi definido antes')

        file_dict = setter.load(filename)
        print(f'{file_dict=}')

        if type(file_dict) == ValueError:
            return file_dict
        
        setter.mount(table, file_dict)
    
    @classmethod
    def save_table(cls, table: 'bt.Table'):
        struct = setter.dismount(table)

        file_name = cls.streams.get(table, None)            
        
        if file_name == None:
            return ValueError('o argumento filename nunca foi definido antes')

        setter.save(file_name, struct)

    @classmethod
    def get_table(cls, name: str) -> 'bt.Table':
        table = cls.tabelas.get(name, None)

        if table == None:
            return NameError(f'A tabela {name} não existe')
        return table



if __name__ == '__main__':
    m = Manager()
    m.load_from_json('Avaliacao')
    m.load_from_json('Materia')

    print(m.get_table('Materia').filter_by('Nome', 'Português'))
    