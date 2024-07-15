
# 1 - Classe Pessoa: Crie uma classe que modele uma pessoa. Esta classe deve possuir os seguintes atributos:​

# Nome​

# Idade​

# Endereço​

# A classe deve ter os seguintes métodos:​

# Mostrar nome;​

# Alterar a idade;​

# Imprimir endereço.​sss



class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco


    def get_Nome(self): 
        print(f"Olá {self.nome}")
    
    def set_Idade(self, novaIdade):
        self.idade= novaIdade

    def get_Idade(self): 
        print(f"Sua idade é {self.idade}")

    def get_Endereco(self):
        print(f"Seu endereço é {self.endereco}")




nome_pessoa= input("Digite seu nome: ")
idade= int(input("Digite sua idade: "))
endereco= input("Digite seu endereço: ")


x= Pessoa(nome_pessoa,idade,endereco)

x.get_Nome()
x.get_Idade()
x.get_Endereco()

print(f"Trocande de idade {idade} para 34")
print("."*50)

x.set_Idade(34)
x.get_Idade()
