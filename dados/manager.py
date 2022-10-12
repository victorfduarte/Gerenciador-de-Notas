
import inspect

try:
    import dados.tabelas as tbl
    import dados.setter as setter
except ImportError:
    import tabelas as tbl
    import setter


class Manager:
    def __init__(self):
        self.tabelas = dict((c for c in inspect.getmembers(tbl, inspect.isclass)))

    def load_from_json(self, filename: str):
        table = self.tabelas.get(filename, None)
        file_dict = setter.load(filename)

        if type(file_dict) == ValueError:
            return file_dict

        if table == None:
            return ValueError(f'Tabela {filename} não foi definida')
        
        registros = file_dict['values']
        for reg in registros:
            table(**reg)
            #table.show_regs()

    def get_table(self, name: str):
        table = self.tabelas.get(name, None)

        if table == None:
            return NameError(f'A tabela {name} não existe')
        return table

    '''
        self.filename = filename

        self.ownername = ''
        self.accounts: 'list[Conta]' = []

        #print(self.__load__(filename))
        self.mount(self.load(filename))
    

    def get_ownername(self) -> str:
        return self.ownername

    def get_elements(self) -> 'tuple[Conta]':
        return self.accounts

    def get_elements_by(self, **kwargs) -> 'tuple[Conta]':
        contas = []

        for conta in self.accounts:
            for key, value in kwargs.items():
                if conta.__getattribute__(key) != value:
                    break
            else:
                contas.append(conta)

        return contas

    def create_data(self, conta: Conta):
        ...
    '''

if __name__ == '__main__':
    m = Manager()
    m.load_from_json('Avaliacao')
    m.load_from_json('Materia')

    print(m.get_table('Materia').get_elements_by('Nome', 'Português'))
    