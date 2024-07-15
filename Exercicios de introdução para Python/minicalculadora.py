#CRIE UMA CALCULADORA QUE MOSTRE MENU COM 4 OPÇOES DE OPERAÇOES
#O USUARIO ESCOLHE UMA DAS OPÇÕES E O SEU PROGRAMA PEDE DOIS VALORES NUMERICOS
operaçao=(input("Digite a operação que deseja realizar: "))
num1=float(input("Digite o numero:"))
num2=float(input("Digite o outro numero: "))
if(operaçao== "+"):
    res=num1+num2
    print(f" O resultado é {res}")

elif(operaçao=="-"):
    res=num1-num2
    print(f"O Resultado é {res}")
elif(operaçao=="*"):
    res=num1*num2
    print(f"O Resultado é {res}")
elif(operaçao=="/"):
    res=num1/num2
    print(f"O Resultado é {res}")