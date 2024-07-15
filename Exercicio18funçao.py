import random

def sorteia():
    numeros_sorteados = []
    for _ in range(5):
        numeros_sorteados.append(random.randint(1, 100))  # Adiciona número sorteado à lista
    return numeros_sorteados  # Retorna a lista de números sorteados

numeros_sorteados = sorteia()
print(f'Números sorteados: {numeros_sorteados}')

def soma_par(numeros_sorteados):
    soma = 0
    for num in numeros_sorteados:
         if num % 2 == 0:
              soma += num
    return soma

soma_pares = soma_par(numeros_sorteados)
print(f"Soma dos números pares sorteados é: {soma_pares}")