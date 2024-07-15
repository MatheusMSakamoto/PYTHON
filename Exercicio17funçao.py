def contador(num):
    i = 1
    while i <= num:
        print('*' *  i)
        i += 1
    i = num - 1
    while i >= 1:
        print('*' * i)
        i -= 1
num = int(input("Digite o número: "))
contador(num)