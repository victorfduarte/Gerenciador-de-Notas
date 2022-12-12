from . import base_table as bt
from . import fields
from . import setter as st


class Avaliacao(bt.Table):
    num_av = fields.Field()
    nota = fields.Field()
    data = fields.Field()    

    def __repr__(self):
        return f'Avaliacao(num_av = {self.num_av}, Materia = {self.Materia})'


class Materia(bt.Table):
    nome = fields.Field()
    prof = fields.Field()
    dias = fields.Field()
    avaliacoes = fields.ForeignKey(Avaliacao)
    
    def __repr__(self):
        return f'Materia(Nome = {self.Nome}, Avaliacoes = {self.Avaliacoes})'


if __name__ == '__main__':

    avaliacao_data = st.load('Avaliacao')['values']

    a1 = Avaliacao(**avaliacao_data[0])
    a2 = Avaliacao(**avaliacao_data[1])

    Avaliacao.show_regs()


