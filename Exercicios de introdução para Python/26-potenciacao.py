#ELABORE PRA FAZER CALCULO DE POTENCIAÇÃO OU SEJA X^Y
#APRESENTE O RESULTADO DO CALCULO SEM UTILIZAR OS OPERADORES **. UTILIZE ESTRUTURA DE REPETIÇÃO
def calcular_potencia(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado

x = int(input("Digite o valor da base (x): "))
y = int(input("Digite o valor do expoente (y): "))
#CALCULO PARA POTENCIA
resultado = calcular_potencia(x, y)

print(f"{x}^{y} = {resultado}")