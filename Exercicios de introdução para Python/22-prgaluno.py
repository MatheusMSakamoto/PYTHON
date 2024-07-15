#ALUNO INTRODUZIR PELO TECLADO, UMA SEQUENCIA DE NOTAS(VALIDAS NO INTERVALO DE 0 A 10) E MOSTRE NA TELA COMO RESULTADO
#A MEDIA ARITMETICA, O NUMERO DE NOTAS COM QUE O ALUNO  PRETENDA EFETUAR O CALCULO NÃO FORNECIDO
# PROG TERMINA QUANDO FOR INTRODUZIDO UMA NOTA QUE N SEJA VALIDA.
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