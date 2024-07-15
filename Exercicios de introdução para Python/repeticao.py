#PARA IMPRIMIR ITENS NA FRUTAS for = para / item = conteudo da lista.
frutas=["Maça","Banana","Pitaya","Goiaba","Framboesa","Acerola"]
for item in frutas:
    print(item)

#-----------------------------------------------------------------------

#ESTRUTURAS DE REPETIÇÃO - WHILE / FOR
#exemplo 1
contador=0
while contador<5:
    print(contador)
contador=contador+1

#exemplo 2
x=0
soma=0
while x<=10:
    soma=soma + x
    x=x+1
print(soma)
#-----------------------------------------------------------------------

#WHILE - BREAK / AVALIA UMA EXPRESSÃO E EXECUTA UM BLOCO  ATÉ AVALIAR COM FALSO
numeros=[2,3,4,11,5]
i=0
#Parando/encerrando o loop, se 11 for encontrado 
while i <len(numeros):
    if numeros[i]==11:
        print('Encontramos o número 11!')
        break
    else:
        i=i+1
        