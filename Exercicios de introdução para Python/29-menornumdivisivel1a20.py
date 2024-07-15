#Crie um programa que calcule o menor número divisível por cada um dos números de 1 a 20? 
#Ex: 2520 e o menor número que pode ser dividido por cada um dos números de 1 a 10, sem 
#sobrar resto
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_multiple(numbers):
    if len(numbers) == 0:
        return 1
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm(result, number)
    return result

numbers = list(range(1, 21))
# Calcula o menor número divisível por todos os números de 1 a 20
result = lcm_multiple(numbers)
print(f"O menor número divisível por cada um dos números de 1 a 20 é: {result}")