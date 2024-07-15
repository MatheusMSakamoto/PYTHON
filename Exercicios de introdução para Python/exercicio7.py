#RECEBA UM NUMERO INTEIRO POSITIVO E IMPRIMA OS PRIMEIROS NUMEROS IMPARES NATURAIS 

n=int(input("Digite um número: "))
cont=0
imp=1
while cont < n :
    print(imp)
    imp+=2
    cont+=1

#EXEMPLO DOIS

num=int(input("Digite um número: "))
for i in range(1,num,2):
    print(f"{i}")