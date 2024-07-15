
# da conta, o nome do cliente e o saldo atual da conta. Crie uma classe que modele um Conta-Corrente.​

# Nome; Sobrenome; Horas_trabalhadas; Valor_hora;​

# A classe deve ter o seguintes métodos:​

# O método nomeCompleto deve escrever na tela o atributo nome concatenado ao atributo sobrenome.​

# O método calcularSalario faz o cálculo de quanto o funcionário irá receber no mês, multiplicando o atributo horasTrabalhadas pelo atributo valorPorHora. Em seguida, escreve o valor na tela.​

# O método incrementarHoras adiciona um valor passado por parâmetro ao valor já existente no atributo valorPorHora.​



class Funcionario:
    def __init__(self,nome,sobrenome,horas_trabalhadas,valor_hora):
        self.nome= nome
        self.sobrenome= sobrenome
        self.horas_trabalhadas= horas_trabalhadas
        self.valor_hora= valor_hora


    def get_Nome_Completo(self):
        print(F"{self.nome} {self.sobrenome}")

    def get_Salario_mes(self):
        salario= (self.horas_trabalhadas*self.valor_hora)*20
        print(f"O salrio é {salario}R$")

    def set_valor_Hora(self, adicao_valor_hora):
        self.valor_hora+= adicao_valor_hora
        print(f"O valor por hora com a adição de {adicao_valor_hora}R$ é {self.valor_hora}R$")


nome_funcioario= input(f"Digite o nome do funcionário: ")
sobrenome_funcionário= input(f"Digite o sobrenome do funcionário: ")
horas_trabalhadas= int(input("Digite as horas trabalhadas por dia: "))
valor_por_hora= float(input("Digite o valor por horas trabalhadas: "))

funcionario_1= Funcionario(nome_funcioario,sobrenome_funcionário,horas_trabalhadas,valor_por_hora)


funcionario_1.get_Nome_Completo()
funcionario_1.get_Salario_mes()
funcionario_1.set_valor_Hora(40)
funcionario_1.get_Salario_mes()
