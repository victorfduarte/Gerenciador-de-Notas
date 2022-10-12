
import inspect

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
        self.Nome = Nome
        self.Prof = Prof
        self.Dias = Dias
        self.Avalicoes = bt.ForeignKey(avaliacao_table, 'Avaliacoes', avaliacao_value)
    
    def __repr__(self):
        return f'Materia(Nome = {self.Nome}, Avaliacoes = {self.Avalicoes})'


class Avaliacao(bt.TableClass):
    def __init__(self, ID: int, Num_AV: int, Nota: float,
    Data: str, Materia: 'dict[str]'):
        super().__init__()

        materia_table = eval(Materia["table"], globals())
        materia_value = Materia["pk"]

        self.ID = bt.PrimaryKey(self, 'ID', ID)
        self.Num_AV = Num_AV
        self.Nota = Nota
        self.Data = Data
        self.Materia = bt.ForeignKey(materia_table, 'Materia', materia_value)

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


