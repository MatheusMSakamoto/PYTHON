# 6 - Classe Funcionário: Crie uma super classe que modele um Funcionário genérico. Esta classe deve possuir os seguintes atributos:​
# Nome;​Matricula;​Salario;​Método:Bater_ponto(): deve criar uma lista de pontos do funcionário, pode ser booleana 0 ou 1;​
# Subclasses:​
# Defina as subclasses de Funcionário, exemplo Vendedor e Gerente. Após a criação das subclasses você deve criar atributos e métodos específicos de cada subclasse;​

class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def bater_ponto(self, ponto):
        if ponto in [0, 1]:
            self.pontos.append(ponto)
        else:
            raise ValueError("Ponto deve ser 0 (ausente) ou 1 (presente)")
        
class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao
        self.vendas = 0

    def registrar_venda(self, valor):
        self.vendas += valor
        self.salario += valor * self.comissao

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, bonus):
        super().__init__(nome, matricula, salario)
        self.bonus = bonus
        self.subordinados = []

    def adicionar_subordinado(self, funcionario):
        if isinstance(funcionario, Funcionario):
            self.subordinados.append(funcionario)
        else:
            raise ValueError("O subordinado deve ser uma instância da classe Funcionario")

    def calcular_bonus(self):
        return self.salario + (self.bonus * len(self.subordinados))

vendedor = Vendedor("João", 1234, 2000.0, 0.05)
vendedor.bater_ponto(1)
vendedor.registrar_venda(1000)

gerente = Gerente("Maria", 5678, 5000.0, 500)
gerente.bater_ponto(1)
gerente.adicionar_subordinado(vendedor)

print(f"Salário do vendedor: {vendedor.salario}")
print(f"Salário do gerente com bônus: {gerente.calcular_bonus()}")
