from . import base_table as bt
from . import fields
from . import setter as st


class Avaliacao(bt.Table):
    num_AV = fields.Field()
    nota = fields.Field()
    data = fields.Field()
    
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


class Materia(bt.Table):
    nome = fields.Field()
    prof = fields.Field()
    dias = fields.Field()
    avaliacoes = fields.ForeignKey(Avaliacao)
    
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


class A(bt.Table):
    num_av = fields.Field()
    data = fields.Field()
    pass


if __name__ == '__main__':

    avaliacao_data = st.load('Avaliacao')['values']
    materia_data = st.load('Materia')['values']

    a1 = Avaliacao(**avaliacao_data[0])
    a2 = Avaliacao(**avaliacao_data[1])

    m1 = Materia(**materia_data[1])
    m2 = Materia(**materia_data[2])

    Avaliacao.show_regs()
    Materia.show_regs()


