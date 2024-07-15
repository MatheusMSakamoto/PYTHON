#CRIE UM PROGRAMA COM INTERVALOR DE 0 A 100, CALCULE E MOSTRE A SOMA DOS 50 NUM PARES.

soma = 0
contador = 0
numero = 0

while contador < 51:
    if numero % 2 == 0:
        soma += numero
        contador += 1
    numero += 1

print("A soma dos 50 primeiros números pares de 0 a 100 é:", soma)