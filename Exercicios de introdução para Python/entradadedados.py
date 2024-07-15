#FAÇA UM PROGRAMA QUE RECEBA 3 DANOS E INFORME QUAL TIPO DE VARIAVEL É (INT, FLOAT OU STRING)
dado1=input("Digite: ")
dado2=int(input("Digite de novo: "))
dado3=float(input("Digite mais uma vez: "))

if(isinstance(dado1,str)):
    print("String")
if(isinstance(dado2,int)):
    print("inteiro")
if(isinstance(dado3,float)):
    print("float")
