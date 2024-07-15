# 10 - Classe Transporte: Crie uma super classe Transporte e suas respectivas subclasses,
# sendo Terrestre e uma terceira subclasse de transporte Automóvel, modele tipos de transportes de acordo com a imagem abaixo:


class Transporte():
    def __init__(self,modelo,ano,peso,cor,capacidade_de_tranporte):
        self.modelo=modelo
        self.ano=ano
        self.cor=cor
        self.peso=peso
        self.capacidade_de_transporte= capacidade_de_tranporte
 


class Terrestre(Transporte):
    def __init__(self, modelo, ano, peso, cor, capacidade_de_tranporte,numero_rodas):
        super().__init__(modelo, ano, peso, cor, capacidade_de_tranporte)
        self.numero_rodas=numero_rodas



class Aereo(Transporte):
    def __init__(self, modelo, ano, peso, cor, capacidade_de_tranporte,numero_assas,capacidade_altura):
        super().__init__(modelo, ano, peso, cor, capacidade_de_tranporte)
        self.numero_assas=numero_assas
        self.capacidade_altura-capacidade_altura

class Aquatico(Transporte):
    def __init__(self, modelo, ano, peso, cor, capacidade_de_tranporte,modelo_motor):
        super().__init__(modelo, ano, peso, cor, capacidade_de_tranporte)
        self.modelo_motor=modelo_motor



class Automovel(Terrestre):
    def __init__(self, modelo, ano, peso, cor, capacidade_de_tranporte, numero_rodas,numero_portas,placa):
        super().__init__(modelo, ano, peso, cor, capacidade_de_tranporte, numero_rodas)
        self.numero_portas= numero_portas
        self.placa= placa
