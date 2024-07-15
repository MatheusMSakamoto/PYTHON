#LEIA UM NUMERO REAL E SE FOR POSITIVO IMPRIMA RAIZ QUADRADA CASO NÃO IMPRIMA INVALIDO
import math
num1=float(input("Digite um número real: "))
if(num1 >= 0 ):
    calculo1=(math.sqrt(num1))
    print(f"A Raiz desse número é : {calculo1}")
elif(num1<0):
    print("O numero é inválido")
