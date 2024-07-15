#Crie uma função que receba dois números como parâmetros e mostre a potência do número elevado a n vezes
def Pot(num1,num2):
    for i in range(1,num2+1):
        print(f"{num1}**{i}={num1**i}")

Pot(2,3)
#----------------------------------------
