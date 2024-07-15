#CRIE UM PROGRAMA QUE LEIA UM NUMERO INTEIRO N E IMPRIMA N PRIMEIROS NUMEROS NATURAIS IMPARES
num=(int(input("Digite um número: ")))
i=1
while i < num:
    print(i)
    i+=2



num=(int(input("Digite um número: ")))
for i in range(1, num, 2):
    print(i)

