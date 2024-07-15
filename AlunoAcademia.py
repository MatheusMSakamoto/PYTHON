# 8 - Classe Aluno_Academia: Uma academia mantem registro de seus alunos e precisa armazenar os seguintes atributos:​

# Nome, Idade, Peso, Altura, Mensalidade (valor default: R$ 120,00)​

# A academia faz um desconto especial para menores de idade, portanto, é necessário saber distinguir entre um aluno maior e menor. 
# Além disso, a academia também tem interesse em acompanhar o desempenho de seus alunos, por isso, ela também necessita 
# conhecer o índice de massa corporal (IMC) deles, para isso a classe deve ter os seguintes métodos:​

# Calcular_IMC()​

# Obter_valor_mensalidade()​




class Aluno_Academia():
    def __init__(self,Nome,Idade,Peso,Altura,Mensalidade=120):
        self.Nome= Nome
        self.Peso= Peso
        self.Idade = Idade
        self.Altura=Altura
        self.Mensalidade= Mensalidade
        self.aplicaDesconto()

    def aplicaDesconto(self):
        if self.Idade < 18:
            self.Mensalidade -= self.Mensalidade * 0.20

    def get_IMC(self):
        calculo_imc= self.Peso/(self.Altura**2)
        if calculo_imc < 17:
            print(f"Muito abixo do peso")
        elif calculo_imc >= 17 and calculo_imc <= 18.49:
            print(f"Abaixo do peso")
        elif calculo_imc  >= 18.5 and calculo_imc <= 24.99:
            print(f"Peso normal")
        elif calculo_imc >= 25 and calculo_imc <= 29.99:
            print(f"Acima do peso")
        elif calculo_imc >= 30 and calculo_imc <= 34.99:
            print(f"Obesidade I")
        elif calculo_imc >=35 and calculo_imc <= 39.99:
            print(f"Obesidade II (severa)")
        else: 
            print(f"Obesidade III(mórbida)")




nome= input("Digite o nome do aluno:  ")
idade= int(input("Digite a idade do aluno: "))
peso= float(input("Digite o peso do aluno: "))
altura= float(input("Digite a altura do aluno: "))

aluno_1= Aluno_Academia(nome,idade,peso,altura)

aluno_1.get_IMC()
print(f"O valor a ser aplicado para esse aluno é {aluno_1.Mensalidade} R$")