#CRIE UM PROGRAMA QUE RECEBE DOIS NUMEROS 
#CALCULE A SOMA DOS NUMEROS PARES DESSE INTERVALO DE NUMEROS E A MULTIPLICAÇÃO DOS NUMEROS IMPARES DESSE INTERVALO AMBOS INCLUINDO OS DIGITADOS.
numero1=int(input("Digite um número: "))
numero2=int(input("Digite outro número: "))

soma_pares=0
mult_impar=1

numero_atual = min(numero1, numero2)
while numero_atual <= max(numero1, numero2):
    if numero_atual % 2 == 0:
        soma_pares+=numero_atual
    else:
        mult_impar*=numero_atual
    numero_atual+=1
print("A Soma dos números pares é: ", soma_pares)
print("A Multiplicação dos números ímpares é: ", mult_impar )