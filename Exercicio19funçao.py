def triangulo(num):
    for i in range(num):
        print(' ' * (num - i - 1) + '*' * (2 * i + 1))

num = int(input("Digite o número: "))

triangulo(num)