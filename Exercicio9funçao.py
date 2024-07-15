def cilindro(altura,raio):
    v = 3.14159 * (raio ** 2) *altura
    print(f"O volume do cilindro é: {v}")

alt = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))

cilindro(alt,raio)