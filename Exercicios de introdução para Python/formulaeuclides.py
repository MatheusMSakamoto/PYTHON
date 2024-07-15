#DESAFIO
#RECEBA 4 NUMEROS DE ENTRADA, X E Y SENDO OS PRIMEIROS, DE UM PONTO EM UM PLANO CARTESIANO
#OS DOIS ULTIMOS DEVEM CORRESPONDER A X E Y DE OUTRO PONTO NO MESMO PLANO CARTESIANO
import math
num1x=float(input("Digite o primeiro numero: "))
num1y=float(input("Digite o segundo numero: "))
num2x=float(input("Digite o terceiro numero: "))
num2y=float(input("Digite o quarto numero: "))
distanciaentreosdoispontos= pow((num1x-num2x), 2) + pow((num1y - num2y), 2)
raiz=math.sqrt(distanciaentreosdoispontos)
print(f"A distância entre os dois pontos é {distanciaentreosdoispontos}")
if raiz >=10:
    print(f"Longe na saída.")
else:
    print("Perto da saída.")
    