#ESCREVA UM PROGRAMA QUE LEIA 10 NUMEROS INTEIROS E IMPRIMA SUA MEDIA
n=10
i=0
soma=0
while i < n:
    soma += int(input("Digite um número: "))
    i+=1
media= soma/n
print(media)