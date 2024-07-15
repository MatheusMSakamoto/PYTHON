#LEIA E SOME TODOS OS NUMEROS NATURAIS ABAIXO DE 1000 QUE SÃO MULTIPLOS DE 3 OU 5.
# numero = 1
# multiplos = []

# while numero < 1000:
#     if numero % 3 == 0 or numero % 5 == 0:
#         multiplos.append(numero)
#     numero += 1

# print(multiplos)

soma = 0
numero = 0

while numero < 1000:
    if numero % 3 == 0 or numero % 5 == 0:
        soma += numero
    numero += 1

print("A soma dos números naturais abaixo de 1000 que são múltiplos de 3 ou 5 é:", soma)