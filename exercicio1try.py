#Escreva um programa Python que solicite ao usuário que insira um inteiro e gere uma exceção ValueError se a entrada não for um inteiro válido.​


try:
     x=int(input("Digite um número: ")) 
     print(x)
except:
    print("Valor inválido. Tente novamente")