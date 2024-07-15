class Pessoa:
    def __init__(self,Matricula,Nome,Idade):
        self.cadastro=Matricula
        self.nome=Nome
        self.idade=Idade

    def getDados(self):
        print(self.cadastro)
        print(self.nome)
        print(self.idade)
