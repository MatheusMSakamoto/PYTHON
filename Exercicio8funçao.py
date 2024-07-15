def converter(celsius):
    F = celsius * (9.0/5.0) + 32.0
    print(f"Temperatura em Fahrenheit é {F}")

celsius =  float(input("Digite o a temperatura em graus celsius: "))
converter(celsius)