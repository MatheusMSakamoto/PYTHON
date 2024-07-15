#LEIA UMA SEQUENCIA DE N INTEIROS E DETERMINE SE SÃO PARES OU IMPARES, INFORME O N DE DADOS LIDOS E VALORES PARES , TERMINA QUANDO DIGITAR 0

numeros_lidos = 0
numeros_pares = 0

while True:
    numero = int(input("Digite um número (digite 0 para parar): "))
#Verificando se o número é zero para encerrar o loop
    if numero == 0:
        break
#Contar  o número de dados lidos
    numeros_lidos += 1
#Verificando se o número é par
    if numero % 2 == 0:
        numeros_pares += 1

print("Número de valores pares:", numeros_pares)
print("Número de dados lidos:", numeros_lidos)
