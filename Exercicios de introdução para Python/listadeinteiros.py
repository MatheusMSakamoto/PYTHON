lista=[25,30,35,40,47]
print(len(lista))
lista.append(5.18)
lista.append(3.28)
lista.append(1.1)
lista.append(4.55)
lista.append(42.15)
print(len(lista))
lista.pop()
lista.pop()
print(len(lista))
lista_ordenada=sorted(lista)
print(lista_ordenada)
print(max(lista))
print(min(lista))
lista_decrescente =sorted(lista,reverse=True)
print(lista_decrescente)
print(sum(lista))
media=(sum(lista)/len(lista))
print(media)
lista.insert(0, "VARIAVEL")
lista.insert(1, "ISQUEMICO")
print(lista)