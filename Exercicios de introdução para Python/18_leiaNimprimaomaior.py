#LEIA UMA CERTA QNTD DE NUMEROS E IMPRIMA O MAIOR DELES,O USUARIO FORNECERÁ A QNTD DE NUMEROS
qntd=int(input("Digite a quantidade de números: "))
num=[]

while qntd > len(num):
    num.append(int(input("Digite o número: ")))

print(num)
print(max(num))