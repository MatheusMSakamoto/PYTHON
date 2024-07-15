#ESCREVA UM PROGRAMA QUE LEIA 10 NUMEROS E ESCREVA O MENOR VALOR LIDO E O MAIOR
lista_num=[]
while(len(lista_num))<10:
    num=int(input("Digite um numero: "))
    lista_num.append(num)
    res=(sum(lista_num))
print(res)


n=10
i=0
soma=0
while i < n:
    soma += int(input("Digite um número: "))
    i+=1
print(soma)