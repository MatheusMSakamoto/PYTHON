# 3 - Classe Ingresso: Crie uma super classe que modele um Ingresso. Esta classe deve possuir os seguintes atributos:​
# Preco;​# Setor;​# Método:​# alterar_preco() e mostrar_setor();​
# Subclasses:​# Defina a subclasse ingressoVIP com os seguintes atributos: camarote, open_bar, open_food, estacionamento -> todos booleanos, True ou False;​
# Acrescente os métodos pegar_bebida() e acessar_camarote();
class Ingresso():
    def __init__(self,Preco,Setor):
        self.Preco=Preco
        self.Setor=Setor
    
    def SetPreco(self,novo_preco):
        self.preco = novo_preco
    
    def getSetor(self):
        return print(f"Vá para o setor {self.Setor}")
    
class IngressoVip(Ingresso):
    def __init__(self, Preco, Setor,camarote,open_bar,open_food,open_estacionamento):
        super().__init__(Preco, Setor)
        self.camarote= camarote
        self.open_bar= open_bar
        self.open_food= open_food
        self.estacionamento= open_estacionamento

    def Pagar_bebida(self):
        print(f"Pague a Bebida")
    def Acessar_camarote(self):
        print("Acesando Camarote")

pessoa1= IngressoVip(100,5,True,False,True,True)

pessoa1.Acessar_camarote()
pessoa1.getSetor()
pessoa1.Pagar_bebida()
pessoa1.SetPreco(150)
print(pessoa1.Setor)
print(pessoa1.preco)