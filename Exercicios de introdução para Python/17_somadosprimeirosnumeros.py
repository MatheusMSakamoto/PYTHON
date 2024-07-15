#LEIA UM NUMERO INTEIRO POSITIVO E CALCULE A SOMA DOS PRIMEIROS NUMEROS NATURAIS
num=(int(input("Digite um número: ")))
i=0
soma=0
while i <= num:
    print(i)
    soma+=i
    i+=1
print(soma)