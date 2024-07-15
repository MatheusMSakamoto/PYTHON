#LEIA UM NUMERO INT E CALCULE A SOMA DOS DIVISORES DESSE NÚM, EXCETO ELE
#EX A soma dos divisores do número 66 é:
n=int(input("Número: "))
soma=0
for i in range(1,n):
    if n % i ==0:
        soma+=i
print("A soma dos divisores desse número será de: ", soma)

#EXEMPLO COM WHILE
n=int(input("Digite um número: "))
i=1
soma=0
while n > 0:
    n-=2
    if n % i ==0:
        print(i)
        soma+=i
    i+=1
print(soma)
 #EXEMPLO 3 
num=int(input("Digite um número: "))
divisores=[]
i=num
while i > 0:
    if i==num:
        i=i-1
    elif num % i == 0:
        divisores.append(i)
        i=i-1
    else:
        i=i-1
print(divisores)
print(sum(divisores))

