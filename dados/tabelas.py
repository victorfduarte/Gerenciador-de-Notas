try:
    import dados.base_table as bt
    import dados.setter as st
except ImportError or ModuleNotFoundError:
    import base_table as bt
    import setter as st


class Materia(bt.TableClass):
    def __init__(self, ID: int, Nome: str, Prof: str, Dias: 'list[str]',
    Avaliacoes: 'dict[str]'):
        super().__init__()

        avaliacao_table = eval(Avaliacoes['table'], globals())
        avaliacao_value = Avaliacoes['pk']

        self.ID = bt.PrimaryKey(self, 'ID', ID)
        self.Nome = bt.Key('Nome', Nome)
        self.Prof = bt.Key('Prof', Prof)
        self.Dias = bt.Key('Dias', Dias)
        self.Avaliacoes = bt.ForeignKey(avaliacao_table, 'Avaliacoes', avaliacao_value)

        self.save()
    
    @classmethod
    def get_header(cls) -> 'tuple[str]':
        return 'ID', 'Nome', 'Prof', 'Dias', 'Avaliacoes'
    
    def get_all_values(self) -> tuple:
        return (
            self.ID.get(),
            self.Nome.get(),
            self.Prof.get(),
            self.Dias.get(),
            self.Avaliacoes.get(),
        )
    
    def save(self, commit=False):
        self.stage = {
            'ID': self.ID.get(),
            'Nome': self.Nome.get(),
            'Prof': self.Prof.get(),
            'Dias': self.Dias.get(),
            'Avaliacoes': {
                'table': 'Avaliacao',
                'pk': self.Avaliacoes.get(),
            }
        }
    
    def __repr__(self):
        return f'Materia(Nome = {self.Nome}, Avaliacoes = {self.Avaliacoes})'


class Avaliacao(bt.TableClass):
    def __init__(self, ID: int, Num_AV: int, Nota: float,
    Data: str, Materia: 'dict[str]'):
        super().__init__()

        materia_table = eval(Materia["table"], globals())
        materia_value = Materia["pk"]

        self.ID = bt.PrimaryKey(self, 'ID', ID)
        self.Num_AV = bt.Key('Num_AV', Num_AV)
        self.Nota = bt.Key('Nota', Nota)
        self.Data = bt.Key('Data', Data)
        self.Materia = bt.ForeignKey(materia_table, 'Materia', materia_value)

        self.save()
    
    @classmethod
    def get_header(cls) -> 'tuple[str]':
        return 'ID', 'Num_AV', 'Nota', 'Data', 'Materia'
    
    def get_all_values(self) -> tuple:
        return (
            self.ID.get(),
            self.Num_AV.get(),
            self.Nota.get(),
            self.Data.get(),
            self.Materia.get(),
        )
    
    def save(self, commit=False):
        self.stage = {
            'ID': self.ID.get(),
            'Num_AV': self.Num_AV.get(),
            'Nota': self.Nota.get(),
            'Data': self.Data.get(),
            'Materia': {
                'table': 'Materia',
                'pk': self.Materia.get(),
            }
        }

    def __repr__(self):
        return f'Avaliacao(Num_AV = {self.Num_AV}, Materia = {self.Materia})'



if __name__ == '__main__':

    avaliacao_data = st.load('Avaliacao')['values']
    materia_data = st.load('Materia')['values']

    a1 = Avaliacao(**avaliacao_data[0])
    a2 = Avaliacao(**avaliacao_data[1])

    m1 = Materia(**materia_data[1])
    m2 = Materia(**materia_data[2])

    Avaliacao.show_regs()
    Materia.show_regs()


