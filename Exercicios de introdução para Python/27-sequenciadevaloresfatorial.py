# Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo do 
# Fatorial: A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
num=int(input("Digite um número: "))
resultado=1
for i in range (1, num+1):
    resultado*=i
print(f"O Resultado da fatoração de {i} é {resultado}")
