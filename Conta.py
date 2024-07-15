
# 4 - Classe Conta: Um banco mantém contas de clientes armazenando o número da conta, o nome do cliente e o saldo atual da conta. Crie uma classe que modele um Conta-Corrente.​

# Nome;​

# CPF;​

# Numero;​

# Saldo;​

# A classe deve ter o seguintes métodos:​

# Depositar()​

# Sacar()  -  OBS: somente enquanto a conta possuir saldo positivo​

# Imprimir saldo()​



class Conta:
    def __init__(self,nome,CPF,numero,saldo= 1000):
        self.nome= nome
        self.CPF= CPF
        self.numero= numero
        self.saldo= saldo
    

    def Depositar(self, novo_deposito):
        self.saldo+= novo_deposito
        print(f"Saldo atual é {self.saldo}R$")
    
    def Sacar(self, retirar_saldo):
        if self.saldo < 0:
            print(f"Sem saldo")
        else:
            self.saldo=  self.saldo-retirar_saldo
            print(f"O saldo atual é de {self.saldo}R$")
            
    
    def get_Saldo(self):
        print(F"Seu saldo é {self.saldo}R$")



nome_pessoa_conta= input(f"Digite seu nome: ")
CPF= int(input(f"Digite seu CPF: "))
numero= int(input("Digite o numêro da conta: "))

conta_1= Conta(nome_pessoa_conta,CPF,numero)


depositar_conta= float(input("Digite valor deposito: "))
conta_1.Depositar(depositar_conta)
print("."*100)

sacar_conta= float(input("Digite valor que quer sacar: "))
conta_1.Sacar(sacar_conta)

conta_1.get_Saldo()