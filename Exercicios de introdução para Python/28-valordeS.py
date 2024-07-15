#ESCREVA UM PROGRAMA QUE CALCULE E ESCREVA O VALOR DE S
# S=1/1+3/2+5/3+7/4...99/50
numerador = 1
denominador = 1

S = 0.0

while numerador <= 99 and denominador <= 50:
    S += numerador / denominador
    numerador += 2
    denominador += 1

print(f"O valor de S é: {S}")