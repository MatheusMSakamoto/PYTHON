#LEIA UM NUMERO, CASO SEJA POSITIVO CALCULE E MOSTRE O NUMERO DIGITADO AO QUADRADO E A RAIZ QUADRADA DO NUMERO DIGITADO
import math
num1=float(input("Digite um número real: "))
if(num1 >= 0 ):
    calculo1=(math.sqrt(num1))
    calculo2=(num1*num1)
    print(f"A Raiz desse número é : {calculo1} e o número ao quadrado é : {calculo2}")