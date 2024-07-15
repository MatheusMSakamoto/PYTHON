#ESCREVA 10 NUM POSITIVOS IGNORANDO OS NEGATIVOS E IMPRIMA SUA MÉDIA
n=10
i=0
soma=0
while i < n:
    soma += int(input("Digite um número: "))
    i+=1
media= soma/n
print(media)
