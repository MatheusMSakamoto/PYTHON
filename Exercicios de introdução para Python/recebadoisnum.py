#RECEBA DOIS NÚMEROS E MOSTRE O MAIOR , SE FOREM IGUAIS IMPRIMA QUE SÃO IGUAIS
num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))
 
if(num1>num2):
        print(f"o Maior é {num1}")

elif(num2>num1):
       print(f"O Maior é {num2}")
elif(num1==num2):
        print("Os numeros são iguais.")