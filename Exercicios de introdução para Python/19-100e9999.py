#ESCREVA UM N INTEIRO ENTRE 100 E 9999 E IMPRIMA CADA UM DOS ALGARISMOS QUE COMPOE O NUM
numero = int(input("Digite um número inteiro entre 100 e 9999: "))

if numero < 100 or numero > 9999:
    print("Número fora do intervalo especificado.")
else:
    print("Os algarismos do número", numero, "são:")
# Loop para extrair os algarismos
while numero > 0:
# Obtendo o último dígito do número
        algarismo = numero % 10
        print(algarismo)
# Removendo o último dígito do número
        numero //= 10