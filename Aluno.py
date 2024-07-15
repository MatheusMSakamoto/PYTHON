
# 3 - Classe Aluno: Crie uma classe que modele um aluno. Esta classe deve possuir os seguintes atributos:​

# Nome;​

# RA;​

# Nota 1, nota 2, nota 3, nota 4;​

# A classe deve ter o seguintes método:​

# Mostrar_situacao: (APROVADO / EXAME / REPROVADO). Considere que, nesse caso, a média final é calculada pela média aritmética simples de todas as notas e que o aluno é aprovado somente se obtiver média maior ou igual a sete. Exame entre 5 e 6.9. Reprovado abaixo de 5​

# A situação será retornada a partir das notas obtidas pelo aluno.​


class Aluno:
    def __init__(self,nome,RA,notas):
        self.nome= nome
        self.RA= RA
        self.notas= notas

    def Media_Aprovação(self):
        media= sum(self.notas)/4
        if media >= 7:
            print(f"O aluno {self.nome} >>> Aprovado")
        elif media > 5 and media < 6.9:
            print(f"O aluno {self.nome} >>> Exame")
        else:
            print(f"O aluno {self.nome} >>> Reprovado")



nome_aluno= input(f"Digite o nome do aluno: ")
RA_aluno= int(input(f"Digite o RA aluno: "))
notas= []

i=0

while i < 4:
    nota= float(input("Digite a nota do aluno: "))
    notas.append(nota)
    i+=1


aluno1= Aluno(nome_aluno,RA_aluno,notas)

aluno1.Media_Aprovação()








        

