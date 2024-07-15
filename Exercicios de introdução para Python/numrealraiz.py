#LEIA UM NUMERO REAL E IMPRIMA SE FOR POSITIVO A RAIZ QUADRADA SE FOR NEGATIVO IMPRIMA O NUMERO AO QUADRADO
import math
num1=float(input("Digite um número real: "))
if(num1 >= 0 ):
    calculo1=(math.sqrt(num1))
    print(f"A Raiz desse número é : {calculo1}")
elif(num1<0):
    calculo2=(num1*num1)
    print(f"O valor ao quadrado do número é : ")