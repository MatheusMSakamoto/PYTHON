def lista_organizadora():
    lista_palavras=['10','9','8','7','6','5','4','3','2','1']
    for indice, i in enumerate(lista_palavras, start=1):
        print(f' {indice} = {i}')
lista_organizadora()
#---------------------------------------------------------------------
def imprime(lista):
    cont=0
    while cont < len(lista):
        print(f"{cont+1} {lista[cont]}")
        cont+=1
listadecompra=['mamao','castanha','mel','uva','banana','detergente','pera','carvão','pastel','sabonete']
imprime(listadecompra)