def calcular_notas(n1,n2,n3,letra):
    if letra == 'A':
        soma = (n1 + n2 + n3) / 3
        print(f"\nA média aritmética das notas é: {soma}")
    elif letra == 'P':
        somap = (n1*5) + (n2*3) + (n3*2) / (5+3+2)
        print(f"\nmédia ponderada, com pesos 5, 3 e 2 é: {somap}")

while True:

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    letra = input("Digite A para ver a média aritimetica ou P para a ponderada: ")

    calcular_notas(n1,n2,n3,letra)
    
    continuar = input("\nDeseja calcular novamente? (S/N): ")
    if continuar != 'S':
        break