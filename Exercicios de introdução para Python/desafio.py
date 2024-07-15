qntd_notas = {}
qntd_notas=int(input("Digite a quantidade de notas: "))
soma=0
cont=0
while cont < qntd_notas:
    notas=float(input("Digite suas notas: "))
    if notas < 0 and notas > 10:
        print("Valor digitado inválido")
        break
    else:
        print(notas)
        soma+=notas
        cont+=1
        media=soma/qntd_notas
print("A média das suas notas é: ", media)
print(qntd_notas)
