numeros = [12,33,44,7,28,30,15.8,8,107]
frutas=["Pêra","Maça","Uva","Banana"]
print(len(numeros))
print(numeros[1])
print(frutas[2])
#print(sum) - soma de todos os numeros
#print(max / min ) - maior numero e menor numero
print(numeros[1] + numeros[4])
#SORTED - comando de ordem crescente para numeros
lista_ordenada=sorted(numeros)
print(lista_ordenada)
#sorted(lista,reverse=True) para colocar em ordem decrescente
sorted(numeros,reverse=True)
print(numeros)
#media dos numeros = sum(lista) / len(listas)
print("MÉDIA", sum(numeros)/len(numeros))
#indice - index posição do numero
indice = numeros.index(28)
print(indice)
#para deletar os ultimos  itens = lista.pop(numero)
numeros.pop()
print(len(numeros))
#inserir um numero na lista/ colocar a posição e ,
numeros.insert(0, 16)
print(numeros)
#adicionar um numero na lista , automaticamente vai pro final da lista 
numeros.append(51)
print(numeros)
#PARA IMPRIMIR ITENS NA FRUTAS for = para / item = conteudo da lista.
for item in frutas:
    print(item)
