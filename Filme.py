class Filme:
    def __init__(self,nome,duracao):
        self.nome=nome #ATRIBUTO PUBLICO
        self.__duracao=duracao # ATRIBUTO PRIVADO 2 underline ("__")

    def Play(self):
        print(f"{self.nome} Começou! ...")
    
    #QUANDO SE PRIVA ATRIBUTOS É NECESSARIO CRIAR SETTERS AND GETTERS PARA AS ALTERAÇOES E RODABILIDADE DO CODIGO
    def setNome(self,novonome):
        self.__nome=novonome
    def getDuracao(self):
        return self.__duracao

#subclasse

class Drama(Filme):
    def __init__(self,nome,duracao,ator):
        super().__init__(nome,duracao)
        self.ator=ator

filme1=Filme("Duro de Matar",185)
filme1.nome="Duro de cozinhar"
print(filme1.getDuracao())
