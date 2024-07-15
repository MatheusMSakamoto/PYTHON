#RECEBA TRÊS NÚMEROS INTEIROS E IMPRIMA CRESCENTE SE ELES ESTIVEREM EM ORDEM CRESCENTE, CASO CONTRARIO IMPRIMA QUE NAO ESTA EM ORDEM CRESCENTE
num1=int(input("Digite um número: "))
num2=int(input("Digite um número: "))
num3=int(input("Digite um número: "))
if(num1<num2 and num2<num3):
    print(f"Estão em ordem crescente.\n{num1},{num2},{num3}")
else:
    print("Não estão em ordem crescente.")