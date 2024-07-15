#CRIE UM PROGRAMA QUE DADOS DOIS NÚMEROS INTEIROS MOSTRE NA TELA O MAIOR DELES E O VALOR DA DIFERENÇA ENTRE ELES
num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))
 
if(num1>num2):
    diferença=(num1-num2)
    print(f"o Maior é {num1} e a diferença entre eles é de {diferença}")

elif(num2>num1):
    diferença2=(num2-num1)
    print(f"O Maior é {num2} e a diferença entre eles é de {diferença2}")