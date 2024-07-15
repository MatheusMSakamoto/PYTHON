#FAÇA UM PROGRAMA QUE RECEBA O NUMERO DE AVALIAÇÕES E USAR COMO CONTADOR E DEPOIS IMPRIMIR A MEDIA DO ALUNO

n=int(input("Digite o número de avaliações: "))
i=0
soma=0
while i < n:
    soma += int(input("Digite a nota: "))
    i+=1
media= soma/n
print(media)

#EXEMPLO DOIS

n=int(input("Digite o número de notas: "))
cont=0
notas=[]
while cont < n:
    notas.append(int(input("Digite a nota: ")))
    cont = cont+1
media=sum(notas)/len(notas)
print(media)

#EXEMPLO TRÊS

n=int(input("digite a nota: "))
soma = 0 
for i in range(n): #RANGE É INTERVALO
    soma+=int(input("digite a nota: "))
media=soma/n
print(media)
