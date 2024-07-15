# 8 - Classe Imóvel: Uma Imobiliária precisa de um sistema que controle o aluguel de seus Imóveis. 
# Para isto você deve definir em um módulo a super classe Imóvel com os seguintes atributos:​
# InscricaoMunicipal; Valor_aluguel; IPTU;​# Método:# obter_parcela_IPTU();​# Set_valor_aluguel();​# Subclasses:​
# Defina as subclasses de Imóvel sendo: Casa, Condomínio; Apartamento; Terreno e Chácara;​
# Defina os atributos específicos para cada sub classe, exemplo: piscina, sala_de_estar, ​
# Quartos, churrasqueira, área m², elevador, área_de_lazer,   .

class Imovel():
    def __init__(self,InscricaoMunicipal,Valor_aluguel,IPTU):
        self.InscricaoMunicipal= InscricaoMunicipal
        self.Valor_aluguel = Valor_aluguel
        self.IPTU= IPTU

    def getIPTU(self):
        print(f"O valor do IPTU é {self.IPTU}R$")

    def setValor_Aluguel(self,novo_aluguel):
        self.Valor_aluguel= novo_aluguel

class Case(Imovel):
    def __init__(self, InscricaoMunicipal, Valor_aluguel, IPTU,churasqueira,sala_de_estar,quarto):
        super().__init__(InscricaoMunicipal, Valor_aluguel, IPTU)
        self.churasqueira= churasqueira
        self.sala_de_estar=sala_de_estar
        self.quarto= quarto

class Apartamento(Imovel):
    def __init__(self, InscricaoMunicipal, Valor_aluguel, IPTU,nome_porteiro,modelo_elevador,numero_apt):
        super().__init__(InscricaoMunicipal, Valor_aluguel, IPTU)
        self.nome_porteiro= nome_porteiro
        self.modelo_elevador= modelo_elevador
        self.numero_apt=numero_apt

class Terreno(Imovel):
    def __init__(self, InscricaoMunicipal, Valor_aluguel, IPTU,metros_quadrados):
        super().__init__(InscricaoMunicipal, Valor_aluguel, IPTU)
        self.metros_quadrados=metros_quadrados

class Chacarra(Imovel):
    def __init__(self, InscricaoMunicipal, Valor_aluguel, IPTU,piscina,gado):
        super().__init__(InscricaoMunicipal, Valor_aluguel, IPTU)
        self.piscina= piscina
        self.gado=gado