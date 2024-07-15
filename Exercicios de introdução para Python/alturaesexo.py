#RECEBA A ALTURA E O SEXO DE UMA PESSOA E CALCULE O PESO IDEAL
alt=float(input("Qual a sua altura? "))
sexo=input("Digite o seu sexo: ")
if(sexo=="M"):
    homem=(72.7*alt)-58
    print(f"Seu peso ideal é {homem}")
elif(sexo=="F"):
    mulher=(62.1*alt)-44.7
    print(f"Seu peso ideal é {mulher}")
    