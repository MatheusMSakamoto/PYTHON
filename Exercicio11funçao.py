def calculadora(n1,n2,simbolo):
    if simbolo == '+':
        res = n1 + n2
        print(res)
    if simbolo == '-':
        res = n1 - n2
        print(res)
    if simbolo == '*':
        res = n1 * n2
        print(res)
    if simbolo == '/':
        res = n1 / n2
        print(res)

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

while True:
    print("Escolha: ")
    print ("'+' para somar")
    print ("'-' para subtrair")
    print ("'*' para multiplicar")
    print ("'/' para dividir")
    simbolo = input("Digite o símobolo para realizar a conta: ")

    calculadora(n1,n2,simbolo)
    
    break