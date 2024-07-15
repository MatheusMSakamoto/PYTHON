def verificar(num):
    if num > 0:
        print(f"1, positivo")
    elif num == 0:
        print(f"0, neutro")
    else:
        print(f"-1, negativo")

x = float(input("Digite o número: "))
verificar(x)