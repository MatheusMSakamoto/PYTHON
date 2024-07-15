# 4 - Classe Passagem: Crie uma super classe que modele uma Passagem. Esta classe deve possuir os seguintes atributos:​
# Preco;​# Assento;​# Método:​# alterar_preco() e escolher_assento();​
# Subclasses:​
# Defina a subclasse PassagemBus e PassagemAviao com os seguintes atributos: portaodeembarque e checkin para classe PassagemAviao, placa e leito par PassagemBus;​
# Crie um novo método específico para cada subclasse. Ex: decolar() e abastecer()

class Passagem():
    def __init__(self,preco,assento):
        self.preco= preco
        self.assento= assento

    
    def setPreco(self,novo_preco):
        self.preco= novo_preco

    def Escolher_Assento():
        passagens= {}
        passagens["assento_1"] = int(input("Digte o assento desejado: "))
        return passagens
    
class PassagemBus(Passagem):
    def __init__(self, preco, assento,placa,leito):
        super().__init__(preco, assento)
        self.placa= placa
        self.leito= leito

    def Abastecer(self):
        print(f"Abastecendo...")

class PassagemAviao(Passagem):
    def __init__(self,preco,assento,portaoembarque,chekin):
        super().__init__(preco, assento)
        self.portaoembarque= portaoembarque
        self.chekin= chekin

    def Decolar(self):
        print(f"O avião irar decolar{100*"."}Decolando!!!")

    def Chegar_Chekin(self,confirmar_chekin):
        if confirmar_chekin == True:
            print("Chekin Válido")
        elif confirmar_chekin == False:
            print("Chekin Inválido")

pessoa1= PassagemBus(500,15,4567,15)
pessoa1.Abastecer()
pessoa2= PassagemAviao(600,15,3,True)
pessoa2.Decolar()
pessoa2.Chegar_Chekin(False)