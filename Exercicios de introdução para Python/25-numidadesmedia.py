#LEIA UM N INDETERMINADO DE IDADES ATÉ DIGITAR 0 E CALCULE A IDADE MÉDIA DO GRUPO
idades = []

while True:
    idade = int(input("Digite uma idade (ou 0 para sair): "))
    if idade == 0:
        break
    idades.append(idade)
soma_idades = sum(idades)
quantidade_idades = len(idades)
if quantidade_idades > 0:
    media_idades = soma_idades / quantidade_idades
    print("A idade média do grupo é:", media_idades)
else:
    print("Nenhuma idade foi inserida.")

#EXEMPLO 2 
soma=0
i=0
while True:
    n=int(input("Digite uma idade(ou 0 para finalizar): "))
    if n ==0:
        break
    elif n > 0:
        soma+=n
        i+=1
        media= soma/i
print(media)